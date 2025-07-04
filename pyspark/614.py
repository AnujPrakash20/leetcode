from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
        .appName("MyApp") \
        .getOrCreate()

follow_data = [
    ("Alice","Bob"),
    ("Bob","Cena"),
    ("Bob","Donald"),
    ("Donald","Edward")
]

follow_columns = ["followee","follower"]

follow_df = spark.createDataFrame(follow_data,follow_columns)

follower_df = follow_df.select(follow_df.follower)

# follow_df.join(follower_df,follow_df.followee == follower_df.follower,how="inner")

filtered_df = follow_df.join(follower_df, follow_df.followee == follower_df.follower, "inner")

filtered_df = filtered_df.groupBy(col("followee")) \
                         .agg(count(col("followee")).alias("cnt")) \
                         .select(col("followee"),col("cnt")) \
                         .orderBy(col("followee"))
filtered_df.show()