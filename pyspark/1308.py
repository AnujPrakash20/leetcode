from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder.appName("1308").getOrCreate()

# Define schema
schema = ["player_name","gender","day","score_points"]

# Data
data = [
    ("Aron", "F", "2020-01-01", 17),
    ("Alice", "F", "2020-01-07", 23),
    ("Bajrang", "M", "2020-01-07", 7),
    ("Khali", "M", "2019-12-25", 11),
    ("Slaman", "M", "2019-12-30", 13),
    ("Joe", "M", "2019-12-31", 3),
    ("Jose", "M", "2019-12-18", 2),
    ("Priya", "F", "2019-12-31", 23),
    ("Priyanka", "F", "2019-12-30", 17)
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

windowSpec = Window.partitionBy(col("gender")).orderBy(col("day"))
df = df.withColumn("total",sum(col("score_points")).over(windowSpec)) \
       .select("gender","day","total")

# Show the DataFrame
df.show()
