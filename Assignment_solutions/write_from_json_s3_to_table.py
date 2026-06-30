import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
emp_json_s3=session.read.json('@my_s3_stage/emp_json_files/emp.json')

emp_json_s3=emp_json_s3.select(col("$1").as_("json_col"))
emp_json_s3.write.mode("overwrite").save_as_table("demo_db.public.json_book")
emp_json_s3=emp_json_s3.select_expr("$1:EMPID","$1:EMPNAME","$1:SALARY","$1:JOB_NAME","$1:DEPTID")
emp_json_s3=emp_json_s3.select(col("$1:EMPID").as_("empid"),col("$1:EMPNAME").as_("empname"),col("$1:JOB_NAME").as_("JOB_NAME"),col("$1:DEPTID").as_("DEPTID"),col("$1:SALARY").as_("SALARY"))
emp_json_s3.write.mode("overwrite").save_as_table("demo_db.public.emp_json_parsed")