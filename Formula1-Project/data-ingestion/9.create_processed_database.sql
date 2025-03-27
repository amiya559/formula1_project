-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS f1_processed
LOCATION "/mnt/formula1dl/processed"

-- COMMAND ----------

describe database extended f1_processed;

-- COMMAND ----------

