## this file is to initilize the food_table with base column 

import mysql.connector; 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="food"
)

cursor = mydb.cursor(); 

# SQL query to create the table 'nutrients'
create_table_query = """

CREATE TABLE IF NOT EXISTS `food`.`nutrients` (
`id` INT NOT NULL AUTO_INCREMENT , 
`name` VARCHAR(255) NOT NULL , 
`desc` TEXT NOT NULL , 
PRIMARY KEY (`id`)) ENGINE = InnoDB;     

"""
# Execute the query to create the table
cursor.execute(create_table_query)

# SQL query to create the table 'nutrient_pros'
create_table_query = """

CREATE TABLE IF NOT EXISTS `food`.`nutrient_pros` (
`pro_id` INT NOT NULL AUTO_INCREMENT ,
`nutrient_id` INT NOT NULL,  
`pro` TEXT NOT NULL ,
`refer` VARCHAR(255) NOT NULL,
PRIMARY KEY (`pro_id`),
FOREIGN KEY (`nutrient_id`) REFERENCES `nutrients`(`id`) ON DELETE CASCADE 
) ENGINE = InnoDB;     

"""
# Execute the query to create the table
cursor.execute(create_table_query)

# SQL query to create the table 'nutrient_cons'
create_table_query = """

CREATE TABLE IF NOT EXISTS `food`.`nutrient_cons` (
`con_id` INT NOT NULL AUTO_INCREMENT ,
`nutrient_id` INT NOT NULL , 
`con` TEXT NOT NULL , 
`refer` VARCHAR(255) NOT NULL,
PRIMARY KEY (`con_id`),
FOREIGN KEY (`nutrient_id`) REFERENCES `nutrients`(`id`) ON DELETE CASCADE  
) ENGINE = InnoDB;     

"""
# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes
mydb.commit()


# Close the cursor and mydb
cursor.close()
mydb.close()

print("Nutrients, pros and cons TABLE created successfully", mydb );
