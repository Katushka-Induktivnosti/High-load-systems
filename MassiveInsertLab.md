import pymongo
import time

try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    if (client):
        db = client["db"]
        col = db["lab_adv2"]

        list = []

        for i in range (1, 100000):
            list.append({ "_id": i, "value": "qwerty"})
        print("Insertion begins...")
        start_time = time.time()

        x = col.insert_many(list)

        print("--- %s seconds ---" % (time.time() - start_time))

except (Exception) as error:
    print(error)


finally:
    print("Insert finished")

![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/Mongo1.PNG?raw=true "Title")

import pymongo
import time

try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    if (client):
        db = client["db"]
        col = db["lab_adv2"]

        print("Insertion begins...")
        start_time = time.time()

        for i in range (1, 100000):
            list = [{ "_id": i, "value": "qwerty"}]
            x = col.insert_many(list)

        print("--- %s seconds ---" % (time.time() - start_time))

except (Exception) as error:
    print(error)


finally:
    print("Insert finished")
    
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/Mongo2.PNG?raw=true "Title")  
    
from cassandra.cluster import Cluster
import time

try:
    cluster = Cluster(['127.0.0.1'], port = '9042')
    session = cluster.connect()
    session.set_keyspace('lab_adv2')
    cluster.connect()

    if (session):

        print("Insertion begins...")
        start_time = time.time()

        for i in range(1, 100000):
            rows = session.execute("INSERT INTO values (value, type, id) VALUES (%s, %s, %s);", ("qwerty", i, i))
        
        print("--- %s seconds ---" % (time.time() - start_time))

except (Exception) as error:
    print(error)

finally:
    print("Insert finished")
    
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/Cassandra.PNG?raw=true "Title")
