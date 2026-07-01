import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,substr
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
schema= StructType([StructField("EMPID",IntegerType()),StructField("EMPNAME",StringType()),StructField("SALARY",IntegerType()),StructField("JOB_NAME",StringType()),StructField("DEPTID",IntegerType())])
employee_s3_csv=session.read.options({"ON_ERROR":"CONTINUE","SKIP_HEADER":1}).schema(schema).csv('@my_s3_stage/emp_csv_files/emp1.csv')
employee_s3_csv.show()
copied_into_result=employee_s3_csv.copy_into_table("emp_csv_tbl",target_columns=["EMPID","EMPNAME","SALARY","JOB_NAME","DEPTID"],force=True,on_error="CONTINUE")
copied_into_result=employee_s3_csv.copy_into_table("emp_csv_tbl",target_columns=["EMPID","EMPNAME","SALARY","JOB_NAME","DEPTID"],transformations=[col("$1"),substr("$2",1,2),"$3","$4","$5"],force=True,on_error="CONTINUE")
copied_into_result
copied_into_result=session.createDataFrame(copied_into_result)
copied_into_result.show()
