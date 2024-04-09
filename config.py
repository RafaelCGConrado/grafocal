from sqlalchemy import create_engine

df_query_result = None

flag_data_loaded = None

opt_source = None
opt_destination = None 
opt_timestamp = None

engine = create_engine('postgresql://rafael:rafael@localhost:5432/mydb') 
connection = engine.connect()