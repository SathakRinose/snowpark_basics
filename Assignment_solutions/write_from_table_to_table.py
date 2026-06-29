import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
customer=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER")
customer=customer.select("C_NAME").filter(col("C_NATIONKEY")=="23")
customer.show()
customwrt=customer.write.mode("append").save_as_table("DEMO_DB.PUBLIC.SNOW_CUSTOMER")
customer_df=session.table("DEMO_DB.PUBLIC.SNOW_CUSTOMER")
customer_df.show()