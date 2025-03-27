-- Databricks notebook source
drop database if exists f1_processed cascade;

-- COMMAND ----------

create database if not exists f1_processed
location 'abfss://processed@formula1dlamiya.dfs.core.windows.net/f1_processed';

-- COMMAND ----------

drop database if exists f1_presentaion cascade;

-- COMMAND ----------

create database if not exists f1_presentaion
location 'abfss://presentation@formula1dlamiya.dfs.core.windows.net/f1_presentation';