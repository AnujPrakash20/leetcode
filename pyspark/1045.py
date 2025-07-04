from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Initialize Spark session
spark = SparkSession.builder.appName("CreateCustomerProductDF").getOrCreate()

# Customer data
customer_data = [
    (1, 5),
    (2, 6),
    (3, 5),
    (3, 6),
    (1, 6)
]
customer_columns = ["customer_id", "product_key"]

# Product data
product_data = [
    (5,),
    (6,)
]
product_columns = ["product_key"]

# Create DataFrames
customer_df = spark.createDataFrame(customer_data, customer_columns)
product_df = spark.createDataFrame(product_data, product_columns)

# Show results
print("Customer DataFrame:")
customer_df.show()

print("Product DataFrame:")
product_df.show()

product_df = product_df.agg(count_distinct(col("product_key")).alias("cnt")).collect()[0]["cnt"]

customer_df = customer_df.groupBy(col("customer_id")).agg(count_distinct(col("product_key")).alias("total_count"))

customer_df = customer_df.filter(col("total_count") == product_df).select(col("customer_id"))

customer_df.show()
print(product_df)