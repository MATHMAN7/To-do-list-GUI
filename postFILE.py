import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="To_do_list_database",
        user="postgres",
        password="DataisFire1374",
        port="5432"
    )
conn=psycopg2.connect(host="localhost",dbname="To_do_list_database",user="postgres",password="DataisFire1374",port="5432")
cur=conn.cursor()

#cur.execute("DELETE FROM tasks WHERE id BETWEEN 18 AND 29;")
#conn.commit()
