from sqlalchemy import create_engine

df_query_result = None

flag_data_loaded = None

engine = create_engine('postgresql://rafael:rafael@localhost:5432/mydb') 
connection = engine.connect()