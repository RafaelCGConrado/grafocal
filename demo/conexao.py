
import pandas as pd
import numpy as np
import pandas.io.sql as psql

from sqlalchemy import create_engine

engine = create_engine('postgresql://rafael:rafael@localhost:5432/incordb') 
connection = engine.connect()

