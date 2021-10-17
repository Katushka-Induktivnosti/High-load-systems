Command 1
MATCH (a:Person)-[r:SPOUSE]-(b:Person)
WHERE a.name CONTAINS 'Velaryon' AND b.culture = 'Valyrian'
return a, b

Command 2
MATCH (a:Person)
WHERE a.name CONTAINS 'Blackfyre' 
return a   

Command 3
MATCH (a:Person)
WHERE a.culture = 'Valyrian' 
return a   

Command 4
MATCH (b:House)-[r:SWORN_TO]->(a:House)
WHERE a.name CONTAINS "Tyrell"
return a,b

Command 5
MATCH (a:House)-[r:LED_BY]->(b:Person) 
WHERE a.region = "The Vale" 
return a,b

Command 6
MATCH (a:House) 
WHERE a.region = "Iron Islands" 
return a

Command 7
MATCH (a:House) 
WHERE a.coatOfArms CONTAINS "horse" 
return a

Command 8
MATCH (a:House) 
WHERE a.coatOfArms CONTAINS "on a sky-blue" OR a.coatOfArms CONTAINS "on a blue" 
return a

Command 9
MATCH (a:House)-[r:FOUNDED_BY]->(b:Person) 
WHERE a.region = "The North" 
return a,b

Command 10
MATCH (a:Person)
WHERE a.culture = 'Valyrian' AND NOT a.name CONTAINS "Velaryon" AND NOT a.name CONTAINS "Targaryen"
return a

Command 11
MATCH (b:House)-[r1:LED_BY]->(a:Person),(c:Person)-[r2:HEIR_TO]->(b:House)
WHERE b.region = "Dorne"
return a,b,c

Command 12
MATCH (c:Seat)-[r1:SEAT_OF]->(b:House),(b:House)-[r2:IN_REGION]->(a:Region)
WHERE a.name = "The Stormlands"
return a,b,c

Command 13
MATCH (c:Seat)-[r:SEAT_OF]->(b:House)
WHERE c.name = "Harrenhal"
return b,c

Command 14
MATCH (b:House)
WHERE b.name CONTAINS "Qoherys"
return b
