
#Testando conexao com uma database genérica

import psycopg2

conn = psycopg2.connect(database="dbname",
                        host="dbhost",
                        users="dbuser",
                        password="dbpass",
                        port="dbport")

cursor = conn.cursor()
