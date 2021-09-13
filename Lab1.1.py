import psycopg2
from psycopg2 import pool
import time

try:
    PostgreSQL = psycopg2.pool.SimpleConnectionPool(1, 20, user="root", 
                                               password="1q2w3e4r%T", 
                                               host="192.168.1.105", 
                                               port="5432", 
                                               database="lab1")

    if (PostgreSQL):
        print("Connection pool created successfully")

    ps_connection = PostgreSQL.getconn()

    if (ps_connection):
        print("successfully recived connection from connection pool")
        ps_cursor = ps_connection.cursor()
        start_time = time.time()
        for i in range (0,100000):
            ps_cursor.execute("INSERT INTO test (id, value) VALUES (%s, %s);", (i, "qwerty"))
            ps_connection.commit()
        ps_cursor.close()
        PostgreSQL.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

        print("--- %s seconds ---" % (time.time() - start_time))


except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if PostgreSQL:
        PostgreSQL.closeall
    print("PostgreSQL connection pool is closed")
            
            

    