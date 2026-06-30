import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,max,min,avg,sum,count,round
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
supplier=session.table("snowflake_sample_data.tpch_sf1.supplier")
supplier_agg=supplier.select(min("s_acctbal"),max("s_acctbal"),avg("s_acctbal"))
supplier_agg=supplier.agg([("s_acctbal","min"),("s_acctbal","max"),("s_acctbal","avg")])
agg_input=[("s_acctbal","min"),("s_acctbal","max"),("s_acctbal","avg")]
supplier_agg=supplier.agg(agg_input)
supplier_agg.show()