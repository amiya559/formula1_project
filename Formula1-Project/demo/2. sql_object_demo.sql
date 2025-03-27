-- Databricks notebook source
-- MAGIC %run "../includes/configuration"

-- COMMAND ----------

create database if not exists demo;

-- COMMAND ----------

show databases

-- COMMAND ----------

describe database extended demo;

-- COMMAND ----------

show tables in default;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC display(race_result_df)

-- COMMAND ----------

-- MAGIC %python
-- MAGIC race_result_df.write.format("parquet").mode("overwrite").saveAsTable("demo.race_result_python")

-- COMMAND ----------

use demo;

-- COMMAND ----------

create table if not exists demo.race_result_sql as select * from demo.race_result_python;

-- COMMAND ----------

select current_database();

-- COMMAND ----------

