import os
import sys
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
sys.path.append("C:/Users/Hp/AppData/Local/Python/pythoncore-3.14-64/Lib")
from generic_code import  code_library  
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}


session=code_library.snowconnection(connection_parameters)