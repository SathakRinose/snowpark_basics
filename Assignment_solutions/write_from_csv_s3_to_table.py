import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
schema= StructType([StructField("EMPID",IntegerType()),StructField("EMPNAME",StringType()),StructField("SALARY",IntegerType()),StructField("JOB_NAME",StringType()),StructField("DEPTID",IntegerType())])
employee_s3_csv=session.read.options({"ON_ERROR":"CONTINUE"}).schema(schema).csv('@my_s3_stage/emp_csv_files/emp1.csv')
employee_s3_csv.show()
employee_s3_csv.write.mode("overwrite").save_as_table("emp_csv_tbl")
