import snowflake.snowpark.functions
from snowflake.snowpark import Session,Window
from snowflake.snowpark.functions import col,max,min,avg,sum,count,round,rank
connection_parameters = {"account":"TMRKOTV-GE73803","user":"SathakRinose","password":"Treselle@367$%","role":"ACCOUNTADMIN","warehouse":"COMPUTE_WH","database":"DEMO_DB","schema":"PUBLIC"}
session=Session.builder.configs(connection_parameters).create()
customer=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER")
orders=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS")
lineitem=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM")
cust_orders=customer.join(orders,customer.C_CUSTKEY==orders.O_CUSTKEY,"inner")
cust_orders_line=cust_orders.join(lineitem,cust_orders.O_ORDERKEY==lineitem.L_ORDERKEY,"inner")
cust_orders_line=cust_orders_line.select("c_custkey","c_name")
cust_orders_line.show()
customer.join(orders,customer["c_custkey"]==orders["o_custkey"],"inner").join(lineitem,lineitem["l_orderkey"]==orders["o_orderkey"],"inner").select("c_custkey","c_name").show()
#using in operator
supplier=session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER")
supplier_inner=supplier.select("s_suppkey","s__nationkey").filter(col("s_nationkey")==17)
supplier.filter(supplier["s_suppkey"].in_(supplier_inner.select("s_suppkey"))).show()
