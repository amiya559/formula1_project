# Databricks notebook source
formula1dl_account_key = dbutils.secrets.get("formula1-scope", "formula1dlamiya-account-key")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.formula1dlamiya.dfs.core.windows.net", 
               formula1dl_account_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlamiya.dfs.core.windows.net/"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlamiya.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

