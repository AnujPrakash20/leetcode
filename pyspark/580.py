from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a Spark session
spark = SparkSession.builder \
    .appName("StudentDepartmentExample") \
    .getOrCreate()

# -----------------------
# Student Table
# -----------------------
student_data = [
    (1, "Jack", "M", 1),
    (2, "Jane", "F", 1),
    (3, "Mark", "M", 2)
]

student_columns = ["student_id", "student_name", "gender", "dept_id"]

student_df = spark.createDataFrame(student_data, student_columns)

# -----------------------
# Department Table
# -----------------------
department_data = [
    (1, "Engineering"),
    (2, "Science"),
    (3, "Law")
]

department_columns = ["dept_id", "dept_name"]

department_df = spark.createDataFrame(department_data, department_columns)

# Show the DataFrames
print("Student DataFrame:")
student_df.show()

print("Department DataFrame:")
department_df.show()

print("Output:")
joined_df = department_df.join(student_df, on='dept_id',how="left").groupBy("dept_name").agg(coalesce(count("student_name"), lit(0)).alias("student_number")).orderBy(desc("student_number"), "dept_name")

joined_df.show()