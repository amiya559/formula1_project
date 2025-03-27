# Databricks notebook source
spark.conf.set("fs.azure.account.auth.type.formula1dlamiya.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dlamiya.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dlamiya.dfs.core.windows.net", "sp=rl&st=2025-01-16T06:43:26Z&se=2025-01-16T14:43:26Z&spr=https&sv=2022-11-02&sr=c&sig=jo8IT%2FPXKS9T%2FsaqdKbaSufFdl3r%2F2cHwUedS1Fq8qM%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlamiya.dfs.core.windows.net/"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlamiya.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

