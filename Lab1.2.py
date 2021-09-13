import psycopg2
from psycopg2 import pool
import time
import threading

def incert_value(x,y):
    x.execute("INSERT INTO test (id, value) VALUES (%s, %s);", (y, "qwerty"))


try:
    PostgreSQL = psycopg2.pool.ThreadedConnectionPool(1,20, user="root", 
                                               password="1q2w3e4r%T", 
                                               host="192.168.1.105", 
                                               port="5432", 
                                               database="lab1")

    if (PostgreSQL):
        print("Connection pool created successfully using ThreadConnectionPool")

    ps_connection = PostgreSQL.getconn()

    if (ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        start_time = time.time()
        for i in range (0, 100000, 100):
            for j in range (i, i+100):
                thread = threading.Thread(target=incert_value, args=(ps_cursor,j))
                thread.start()
                ps_connection.commit()
            
        thread.join()
        ps_cursor.close()
        print("Number of threads:100")
        print("--- %s seconds ---" % (time.time() - start_time))

        PostgreSQL.putconn(ps_connection)
        print("Put away a PostgreSQL connection")


except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if PostgreSQL:
        PostgreSQL.closeall
    print("PostgreSQL connection pool is closed")
    time.sleep(60)

