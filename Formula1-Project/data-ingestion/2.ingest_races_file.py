# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

dbutils.widgets.text("p_file_date", "2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")

# COMMAND ----------

# MAGIC %run "../includes/configuration"

# COMMAND ----------

# MAGIC %run "../includes/common_functions"

# COMMAND ----------

# display(dbutils.fs.ls("abfss://raw@formula1dlamiya.dfs.core.windows.net/"))

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

races_schema = StructType(
    fields=[
        StructField("raceId", IntegerType(), False),
        StructField("year", IntegerType(), True),
        StructField("round", IntegerType(), True),
        StructField("circuitId", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("date", DateType(), True),
        StructField("time", StringType(), True),
        StructField("url", StringType(), True),
    ]
)

# COMMAND ----------

races_df = (
    spark.read.option("header", True)
    .schema(races_schema)
    .csv(f"{raw_folder_path}/{v_file_date}/races.csv")
)

# COMMAND ----------

from pyspark.sql.functions import col, concat, to_timestamp, lit, current_timestamp

# COMMAND ----------

races_with_timestamp_df = races_df.withColumn(
    "ingestion_date", current_timestamp()
).withColumn(
    "race_timestamp",
    to_timestamp(concat(col("date"), lit(" "), col("time")), "yyyy-MM-dd HH:mm:ss"),
)

# COMMAND ----------

races_selected_df = races_with_timestamp_df.select(
    col("raceId").alias("race_id"),
    col("year").alias("race_year"),
    col("round"),
    col("circuitId").alias("circuit_id"),
    col("name"),
    col("ingestion_date"),
    col("race_timestamp"),
)

# COMMAND ----------

races_selected_df.write.mode("overwrite").partitionBy("race_year").format("delta").saveAsTable("f1_processed.races")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from f1_processed.races;

# COMMAND ----------

# spark.read.parquet("abfss://processed@formula1dlamiya.dfs.core.windows.net/races").display()

# COMMAND ----------

dbutils.notebook.exit("Success")