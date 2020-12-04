import pytest
import pyspark.sql.functions as f
from datetime import datetime, timedelta
from pyspark.sql import SparkSession

class Test_temperatures(object):
    
    def test_data_is_recent(self):
        
        spark = SparkSession.builder.getOrCreate()

        silver_weather_temperatures_df = spark.read.load("/mnt/data/silver/weather/temperatures")

        print('most recent 10 records are:')
        silver_weather_temperatures_df.orderBy(f.col("date").desc()).show()

        yesterday_date = datetime.utcnow().date() -  timedelta(days=1)
        record_as_of_yesterday_df = silver_weather_temperatures_df.where(f.col("date") >= yesterday_date)

        yesterday_str = yesterday_date.strftime("%Y/%m/%d")
        print(f'checking records exist as of {yesterday_str}')

        assert record_as_of_yesterday_df.count() > 0, "records do not exist recently"


    def test_data_in_range(self):
        assert True == True