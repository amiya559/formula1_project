# Databricks notebook source
dbutils.fs.ls('/FileStore/tables')

# COMMAND ----------

display(spark.read.format('csv').options(header='true', inferSchema='true').load('/FileStore/tables/circuits.csv'))

# COMMAND ----------

