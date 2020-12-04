
import os
import json
from pyspark.sql import SparkSession
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def get_spark():
    return SparkSession.builder.appName("dataproc").getOrCreate()


def get_dbutils():
    spark = get_spark()
    if spark.conf.get("spark.databricks.service.client.enabled") == "true":
        from pyspark.dbutils import DBUtils
        return DBUtils(spark)
    else:
        import IPython
        return IPython.get_ipython().user_ns["dbutils"]

def is_local():
    spark = SparkSession.builder.getOrCreate()
    setting = spark.conf.get("spark.master")
    if "local" in setting:
        return True
    else:
        return False
