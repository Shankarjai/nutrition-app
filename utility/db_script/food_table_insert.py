## this file is to initilize the food_table with base column 

import mysql.connector; 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="food"
)

cursor = mydb.cursor();

# SQL query to create the table 'food_items'
create_table_query = """
INSERT INTO `food` (`usda_id`,`food_id`, `food_name`, `food_category`, `water`, `kcal`, `protein`, 
`Tryptophan`, `Threonine`, `Isoleucine`, `Leucine`, `Lysine`, `Methionine`, `Cystine`,
`Phenylalanine`, `Tyrosine`, `Valine`, `Arginine`, `Histidine`, `Alanine`, 
`Aspartic_acid`, `Glutamic_acid`, `Glycine`, `Proline`, `Serine`, `Fat`, 
`ala`, `epa`, `dpa`, `dha`, `omega6`, `omega3`, `Carb`, `Fiber`, `Sugar`,
`Ca`, `Fe`, `Mg`, `P`, `K`, `Na`, `Zn`, `Cu`, `Mn`, `Se`, `V_c`, `B1`,
`B2`, `B3`, `B6`, `B9`, `B12`, `V_a`, `V_e`, `V_k`, `tsFat`, `tmsFat`,
`tpusFat`, `transFat`, `cholest`, `caffine`, `alcho`, `hydroxyproline`, 
`laz`, `V_d`, `sucrose`, `glucose`, `frutose`, `lactose`, `maltose`, 
`galctose`, `strach`) VALUES ('55565','1', 'Apple', 'Fruit', '1', '1', '1', '1', 
'1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '11', '1', '1', 
'1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 
'1', '1', '1', '1', '11', '1', '1', '1', '1.0', '1.0', '1.0', '1.0', 
'1.0', '1.0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
'1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');

"""

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes
mydb.commit()

# Close the cursor and mydb
cursor.close()
mydb.close()

print("inserted dummy food in FOOD table successfully", mydb );
