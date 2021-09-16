import psycopg2
from psycopg2 import pool
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def incert_value(p,y):
    ps_connection = p.getconn()
    ps_cursor = ps_connection.cursor()
    ps_cursor.execute("INSERT INTO test (id, value) VALUES (%s, %s);", (y, "qwerty"))
    ps_connection.commit()
    ps_cursor.close()
    p.putconn(ps_connection)
   


try:
    PostgreSQL = psycopg2.pool.ThreadedConnectionPool(1,20, user="root", 
                                               password="1q2w3e4r%T", 
                                               host="192.168.1.105", 
                                               port="5432", 
                                               database="lab1")

    if (PostgreSQL):
        print("Connection pool created successfully using ThreadConnectionPool")

        values = list(i for i in range(20))
        print("successfully recived connection from connection pool")
        
        start_time = time.time()

        for j in range (0,100000,20):
            with ThreadPoolExecutor(max_workers=20) as pool:
                transaction = [pool.submit(incert_value(PostgreSQL, j+i)) for i in values]
          

        print("Number of threads:20")
        print("--- %s seconds ---" % (time.time() - start_time))


except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if PostgreSQL:
        print("Put away a PostgreSQL connection")
        PostgreSQL.closeall
    print("PostgreSQL connection pool is closed")
    time.sleep(60)