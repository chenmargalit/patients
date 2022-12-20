import psycopg2
import time

# password should come form env file

def connect_to_db():
    conn = psycopg2.connect( 
        host="db",
        port="5432",
        database="patients",
        user="postgres",
        password="postgres"
        )
    return conn

for i in range(3):
    conn = connect_to_db()
    if conn: break
    else:
        time.sleep(1)



cur = conn.cursor()
