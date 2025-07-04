from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder \
        .appName("Test") \
        .getOrCreate()

#----------------
# Insurance Table
#----------------

insurance_data = [
    (1,10,5,10,10),
    (2,20,20,20,20),
    (3,10,30,20,20),
    (4,10,40,40,40)
]

insurance_column = ["p_id","tiv_2015","tiv_2016","lat","lon"]

insurance_df = spark.createDataFrame(insurance_data,insurance_column)

print("Insurance Dataframe: ")
# insurance_df.show()

windowSpec1 = Window.partitionBy("tiv_2015")
windowSpec2 = Window.partitionBy("lat","lon")

insurance_df = insurance_df.withColumn("flag1", count("*").over(windowSpec1))\
                           .withColumn("flag2", count("*").over(windowSpec2))

insurance_df = insurance_df.where((col("flag1") > 1) & (col("flag2") == 1)).agg(round(sum("tiv_2016"),2).alias("tiv_2016"))

insurance_df.show()