# # Write your MySQL query statement below
# WITH CTE AS(
# SELECT *,
# ROW_NUMBER() OVER() as r_no
# FROM Point2D
# ),
# CTE2 AS(
# SELECT t1.x as x1, t1.y as y1,t2.x as x2,t2.y as y2,sqrt(power((t2.x - t1.x),2) + power((t2.y - t1.y),2)) as distance 
# FROM CTE t1
# JOIN CTE t2
# ON t1.r_no > t2.r_no
# )
# SELECT round(min(distance),2) as shortest
# FROM CTE2



# Point2D table:
# +----+----+
# | x  | y  |
# +----+----+
# | -1 | -1 |
# | 0  | 0  |
# | -1 | -2 |
# +----+----+

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder \
        .appName("Test") \
        .getOrCreate()

point_data = [
    (-1,-1),
    (0,0),
    (-1,-2)
]

point_columns = ["x","y"]

point_df = spark.createDataFrame(point_data,point_columns)

df_rno = point_df.rdd.zipWithIndex().toDF()

df_new = df_rno.select(
    col("_1.x").alias("x"),
    col("_1.y").alias("y"),
    (col("_2")+1).alias("r_no")
)

t1 = df_new.alias("t1")
t2 = df_new.alias("t2")

df_new = t1.join(t2, col("t1.r_no")>col("t2.r_no"))
df_new = df_new.withColumn("shortest",sqrt(pow(col("t1.x")-col("t2.x"), 2) + pow(col("t1.y")-col("t2.y"), 2)))

df_new = df_new.agg(round(min("shortest"),2).alias("shortest"))
df_new.show()
