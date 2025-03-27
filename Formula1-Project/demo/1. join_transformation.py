# Databricks notebook source
# MAGIC %run "../includes/configuration"

# COMMAND ----------

ciruits_df = spark.read.parquet(f"{processed_folder_path}/circuits")

# COMMAND ----------

races_df = spark.read.parquet(f"{processed_folder_path}/races").filter(f"race_year = 2019")

# COMMAND ----------

display(ciruits_df)

# COMMAND ----------

display(races_df)

# COMMAND ----------

race_circuit_df = ciruits_df.join(races_df, on="circuit_id", how="left")

# COMMAND ----------

display(race_circuit_df)

# COMMAND ----------

