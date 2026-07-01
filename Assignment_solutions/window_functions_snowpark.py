import snowflake.snowpark.functions
from snowflake.snowpark import Session,Window
from snowflake.snowpark.functions import col,max,min,avg,sum,count,round,rank
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
supplier=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER")
supplier_rank=supplier.select("s_name","s_acctbal",rank().over(Window.order_by("s_acctbal")).as_("RANK")).where(col("RANK")==1)
supplier_rank.show()