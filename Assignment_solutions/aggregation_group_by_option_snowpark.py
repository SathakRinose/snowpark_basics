import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,max,min,avg,sum,count,round
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
emp=session.table("demo_db.public.emp_csv_tbl")
emp_grp=emp.group_by("DEPTID")
emp_grp_cnt=emp_grp.count()
emp_grp_cnt.show()
supplier=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER")
supplier_min=supplier.select(min("s_acctbal").as_("min_acctbal"))
type(supplier_min)
acct_bal=supplier_min.collect()
min_bal=acct_bal[0][0]
supplier_name=supplier.select("s_name","s_acctbal").where(col("s_acctbal")==min_bal)
