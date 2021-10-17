Command 1
MATCH (a:Person)-[r:SPOUSE]-(b:Person)
WHERE a.name CONTAINS 'Velaryon' AND b.culture = 'Valyrian'
return a, b
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/1.PNG?raw=true "Title")

Command 2
MATCH (a:Person)
WHERE a.name CONTAINS 'Blackfyre' 
return a   
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/2.PNG?raw=true "Title")

Command 3
MATCH (a:Person)
WHERE a.culture = 'Valyrian' 
return a 
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/3.PNG?raw=true "Title")

Command 4
MATCH (b:House)-[r:SWORN_TO]->(a:House)
WHERE a.name CONTAINS "Tyrell"
return a,b
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/4.PNG?raw=true "Title")

Command 5
MATCH (a:House)-[r:LED_BY]->(b:Person) 
WHERE a.region = "The Vale" 
return a,b
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/5.PNG?raw=true "Title")

Command 6
MATCH (a:House) 
WHERE a.region = "Iron Islands" 
return a
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/6.PNG?raw=true "Title")

Command 7
MATCH (a:House) 
WHERE a.coatOfArms CONTAINS "horse" 
return a
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/7.PNG?raw=true "Title")

Command 8
MATCH (a:House) 
WHERE a.coatOfArms CONTAINS "on a sky-blue" OR a.coatOfArms CONTAINS "on a blue" 
return a
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/8.PNG?raw=true "Title")

Command 9
MATCH (a:House)-[r:FOUNDED_BY]->(b:Person) 
WHERE a.region = "The North" 
return a,b
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/9.PNG?raw=true "Title")

Command 10
MATCH (a:Person)
WHERE a.culture = 'Valyrian' AND NOT a.name CONTAINS "Velaryon" AND NOT a.name CONTAINS "Targaryen"
return a
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/10.PNG?raw=true "Title")

Command 11
MATCH (b:House)-[r1:LED_BY]->(a:Person),(c:Person)-[r2:HEIR_TO]->(b:House)
WHERE b.region = "Dorne"
return a,b,c
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/11.PNG?raw=true "Title")

Command 12
MATCH (c:Seat)-[r1:SEAT_OF]->(b:House),(b:House)-[r2:IN_REGION]->(a:Region)
WHERE a.name = "The Stormlands"
return a,b,c
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/12.PNG?raw=true "Title")

Command 13
MATCH (c:Seat)-[r:SEAT_OF]->(b:House)
WHERE c.name = "Harrenhal"
return b,c
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/13.PNG?raw=true "Title")

Command 14
MATCH (b:House)
WHERE b.name CONTAINS "Qoherys"
return b
![Alt text](https://github.com/Katushka-Induktivnosti/High-load-systems/blob/main/14.PNG?raw=true "Title")
