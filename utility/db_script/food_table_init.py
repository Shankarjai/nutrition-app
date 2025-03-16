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
CREATE TABLE IF NOT EXISTS `food`.`food` (
`usda_id` INT NOT NULL,
`food_id` INT NOT NULL AUTO_INCREMENT , 
`food_name` VARCHAR(255) NOT NULL ,
`food_category` VARCHAR(100) NOT NULL , 
`water` DECIMAL(10,2) NOT NULL, 
`kcal` DECIMAL(10,2) NOT NULL, 
`protein` DECIMAL(10,2) NOT NULL,
`Tryptophan` DECIMAL(10,2) NOT NULL, 
`Threonine` DECIMAL(10,2) NOT NULL,
`Isoleucine` DECIMAL(10,2) NOT NULL, 
`Leucine` DECIMAL(10,2) NOT NULL, 
`Lysine` DECIMAL(10,2) NOT NULL, 
`Methionine` DECIMAL(10,2) NOT NULL,
`Cystine` DECIMAL(10,2) NOT NULL, 
`Phenylalanine` DECIMAL(10,2) NOT NULL, 
`Tyrosine` DECIMAL(10,2) NOT NULL, 
`Valine` DECIMAL(10,2) NOT NULL, 
`Arginine` DECIMAL(10,2) NOT NULL, 
`Histidine` DECIMAL(10,2) NOT NULL, 
`Alanine` DECIMAL(10,2) NOT NULL, 
`Aspartic_acid` DECIMAL(10,2) NOT NULL, 
`Glutamic_acid` DECIMAL(10,2) NOT NULL, 
`Glycine` DECIMAL(10,2) NOT NULL, 
`Proline` DECIMAL(10,2) NOT NULL, 
`Serine` DECIMAL(10,2) NOT NULL, 
`Fat` DECIMAL(10,2) NOT NULL, 
`ala` DECIMAL(10,2) NOT NULL, 
`epa` DECIMAL(10,2) NOT NULL, 
`dpa` DECIMAL(10,2) NOT NULL, 
`dha` DECIMAL(10,2) NOT NULL, 
`omega6` DECIMAL(10,2) NOT NULL, 
`omega3` DECIMAL(10,2) NOT NULL, 
`Carb` DECIMAL(10,2) NOT NULL, 
`Fiber` DECIMAL(10,2) NOT NULL, 
`Sugar` DECIMAL(10,2) NOT NULL, 
`Ca` DECIMAL(10,2) NOT NULL, 
`Fe` DECIMAL(10,2) NOT NULL, 
`Mg` DECIMAL(10,2) NOT NULL, 
`P` DECIMAL(10,2) NOT NULL, 
`K` DECIMAL(10,2) NOT NULL, 
`Na` DECIMAL(10,2) NOT NULL,
`Zn` DECIMAL(10,2) NOT NULL, 
`Cu` DECIMAL(10,2) NOT NULL, 
`Mn` DECIMAL(10,2) NOT NULL, 
`Se` DECIMAL(10,2) NOT NULL, 
`V_c` DECIMAL(10,2) NOT NULL, 
`B1` DECIMAL(10,2) NOT NULL, 
`B2` DECIMAL(10,2) NOT NULL, 
`B3` DECIMAL(10,2) NOT NULL, 
`B6` DECIMAL(10,2) NOT NULL, 
`B9` DECIMAL(10,2) NOT NULL, 
`B12` DECIMAL(10,2) NOT NULL, 
`V_a` DECIMAL(10,2) NOT NULL, 
`V_e` DECIMAL(10,2) NOT NULL, 
`V_k` DECIMAL(10,2) NOT NULL, 
`tsFat` DECIMAL(10,2) NOT NULL, 
`tmsFat` DECIMAL(10,2) NOT NULL, 
`tpusFat` DECIMAL(10,2) NOT NULL, 
`transFat` DECIMAL(10,2) NOT NULL, 
`cholest` DECIMAL(10,2) NOT NULL, 
`caffine` DECIMAL(10,2) NOT NULL, 
`alcho` DECIMAL(10,2) NOT NULL, 
`hydroxyproline` DECIMAL(10,2) NOT NULL, 
`laz` DECIMAL(10,2) NOT NULL, 
`V_d` DECIMAL(10,2) NOT NULL, 
`sucrose` DECIMAL(10,2) NOT NULL, 
`glucose` DECIMAL(10,2) NOT NULL,
`frutose` DECIMAL(10,2) NOT NULL, 
`lactose` DECIMAL(10,2) NOT NULL, 
`maltose` DECIMAL(10,2) NOT NULL, 
`galctose` DECIMAL(10,2) NOT NULL, 
`strach` DECIMAL(10,2) NOT NULL,


PRIMARY KEY (`food_id`)) ENGINE = InnoDB; 
"""

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes
mydb.commit()

# Close the cursor and mydb
cursor.close()
mydb.close()

print("FOOD table created successfully", mydb );
