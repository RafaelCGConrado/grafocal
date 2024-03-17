
#Testando conexao com uma database genérica
# Formato:
# Connection format: %sql dialect+driver://username:password@host:port/database
# engine = create_engine('postgresql://postgres:pgadmin@localhost/Alunos15')

import pandas as pd
import numpy as np
import pandas.io.sql as psql

from sqlalchemy import create_engine

engine = create_engine('postgresql://rafael:rafael@localhost:5432/mydb') 
connection = engine.connect()

carrosStat = psql.read_sql("SELECT * FROM cars", engine)
carrosStat.plot(x='brand', y='year', kind='barh')


def selecionaCriterios(valorUsuario):
    query = "SELECT * FROM cars WHERE brand = :marca"
    param = {'marca': valorUsuario}
    df = psql.read_sql(query, engine, params=param)
    return stat
