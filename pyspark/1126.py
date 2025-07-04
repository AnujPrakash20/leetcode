from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("EventsExample").getOrCreate()

# Define data
data = [
    (1, "reviews", 7),
    (3, "reviews", 3),
    (1, "ads", 11),
    (2, "ads", 7),
    (3, "ads", 6),
    (1, "page views", 3),
    (2, "page views", 12)
]

# Define schema
schema = StructType([
    StructField("business_id", IntegerType(), True),
    StructField("event_type", StringType(), True),
    StructField("occurrences", IntegerType(), True)
])

# Create DataFrame
events_df = spark.createDataFrame(data, schema)

windowSpec = Window.partitionBy(col("event_type"))
events_df = events_df.withColumn("event_avg",avg(col("occurrences")).over(windowSpec)).orderBy(col("business_id")) \
                     .withColumn("flag",expr('CASE WHEN occurrences > event_avg THEN 1 ELSE 0 END')) \
                     .groupBy(col("business_id")).agg(sum(col("flag")).alias("sum")) \
                     .filter(col("sum") >= 2) \
                     .select(col("business_id"))

# Show the DataFrame
events_df.show()
