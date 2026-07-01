import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
employee_s3_json=session.read.json('@my_s3_stage/emp_json_files/emp.json')
employee_s3_json.show()
employee_s3_json=employee_s3_json.select_expr("$1:EMPID","$1:EMPNAME","$1:DEPTID").show()

employee_s3_json.schema