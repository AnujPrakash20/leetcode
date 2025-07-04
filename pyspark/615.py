from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

#Start Spark session
spark = SparkSession.builder.appName("615.py").getOrCreate()

#Define columns for payments table
payments_columns = ["id","employee_id","amount","pay_date"]

#Data for payments
payments_data = [
    (1, 1, 9000, "2017/03/31"),
    (2, 2, 6000, "2017/03/31"),
    (3, 3, 10000, "2017/03/31"),
    (4, 1, 7000, "2017/02/28"),
    (5, 2, 6000, "2017/02/28"),
    (6, 3, 8000, "2017/02/28")
]

#Create DataFrame for payments
payments_df = spark.createDataFrame(payments_data, payments_columns)

# Optionally, convert pay_date to proper DateType
from pyspark.sql.functions import to_date
payments_df = payments_df.withColumn("pay_date", to_date("pay_date", "yyyy/MM/dd"))

#Define columns and data for employee table

employee_columns = ["employee_id","department_id"]

employee_data = [
    (1, 1),
    (2, 2),
    (3, 2)
]

#Create DataFrame for employee
employee_df = spark.createDataFrame(employee_data, employee_columns)

# Show both DataFrames
print("Payments DataFrame:")
payments_df.show()

print("Employee DataFrame:")
employee_df.show()


joined_df = payments_df.join(employee_df,on="employee_id",how="inner")

windowSpec1 = Window.partitionBy(date_format("pay_date","yyyy-MM"))
windowSpec2 = Window.partitionBy("department_id",date_format("pay_date","yyyy-MM"))

joined_df = joined_df.withColumn("avg_total",avg("amount").over(windowSpec1)) \
                     .withColumn("avg_dept",avg("amount").over(windowSpec2)) \
                     .withColumn("comparision",when(col("avg_dept") > col("avg_total"),"higher")\
                                 .when(col("avg_dept") < col("avg_total"),"lower")\
                                 .otherwise("same") \
                                ) \
                    .groupBy(date_format("pay_date","yyyy-MM").alias("pay_date"),"department_id").agg(expr("first(comparision)").alias("comparision"))
                                               

joined_df.show()