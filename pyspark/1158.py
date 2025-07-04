from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Example").getOrCreate()

from datetime import date

users_data = [
    (1, date(2018, 1, 1), "Lenovo"),
    (2, date(2018, 2, 9), "Samsung"),
    (3, date(2018, 1, 19), "LG"),
    (4, date(2018, 5, 21), "HP")
]

users_schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("join_date", DateType(), True),
    StructField("favorite_brand", StringType(), True)
])

users_df = spark.createDataFrame(users_data, schema=users_schema)

orders_data = [
    (1, date(2019, 8, 1), 4, 1, 2),
    (2, date(2018, 8, 2), 2, 1, 3),
    (3, date(2019, 8, 3), 3, 2, 3),
    (4, date(2018, 8, 4), 1, 4, 2),
    (5, date(2018, 8, 4), 1, 3, 4),
    (6, date(2019, 8, 5), 2, 2, 4)
]

orders_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("order_date", DateType(), True),
    StructField("item_id", IntegerType(), True),
    StructField("buyer_id", IntegerType(), True),
    StructField("seller_id", IntegerType(), True)
])

orders_df = spark.createDataFrame(orders_data, schema=orders_schema)


items_data = [
    (1, "Samsung"),
    (2, "Lenovo"),
    (3, "LG"),
    (4, "HP")
]

items_schema = StructType([
    StructField("item_id", IntegerType(), True),
    StructField("item_brand", StringType(), True)
])

items_df = spark.createDataFrame(items_data, schema=items_schema)


orders_2019 = orders_df.filter(year(col('order_date')) == 2019)

joined_df = users_df.join(orders_2019, col("user_id") == col("buyer_id"), how="left") \
                    .groupBy(col("user_id"), col("favorite_brand")) \
                    .agg(coalesce(count(col("buyer_id")), lit(0)).alias("orders_in_2019"))

joined_df.show()