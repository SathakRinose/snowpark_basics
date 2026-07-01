import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
schema=StructType([StructField("empid", IntegerType()),
             StructField("empname", StringType()),
             StructField("salary", IntegerType()),
            StructField("job", StringType()),
             StructField("deptid", IntegerType())])
employee_s3=session.read.options({"ON_ERROR":"CONTINUE","SKIP_HEADER":1}).schema(schema).csv("@my_s3_stage/emp_csv_files/emp1.csv")
employee_s3=employee_s3.cache_result()
                                 
employee_s3.is_cached
employee_s3.columns     
employee_s3=employee_s3.select("empid","empname","salary","job").filter(col("deptid")==10)      
employee_s3.show()                      
