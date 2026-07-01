import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
def snowconnection(connection_config):
    session=Session.builder.configs(connection_config).create()
    session_details=session.create_dataframe([[session._session_id,session.sql("select current_user();").collect()[0][0],str(session.get_current_warehouse()).replace('"',''),str(session.get_current_role()).replace('"','')]],schema=["session_id","user_name","warehouse","role"])
    session_details.write.mode("append").save_as_table("session_audit")
    return session

session=snowconnection(connection_parameters)
