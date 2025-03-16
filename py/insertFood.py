import os 
import json
import mysql.connector; 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="food"
)

mycursor = mydb.cursor();

path = r"C:\xampp\htdocs\nutri\foodJson";

# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# # prints all files
# print(dir_list)

os.chdir(path);

for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".json"): 
        file_path = f"{path}\{file}"
  
        # call read text file function 
        with open(file_path, 'r') as f:
            json_file = json.load(f)
            json_dump = json.dumps(json_file).replace("'","").replace('u00c2','');
            name = json_file['name'].replace("'","");
            usda_id = json_file['id'];

            sql_get = f"""SELECT * FROM `food` WHERE `usda_id` = {usda_id}""";
            # print(name)
            mycursor.execute(sql_get);
            myresult = mycursor.fetchall();
            if(len(myresult) > 0):
                print(f'{name} {usda_id} data exist')
            else:
                sql_insert = f"""INSERT INTO `food` (`usda_id`, `food_name`, `food_category`, `water`, `kcal`, `protein`, 
                    `Tryptophan`, `Threonine`, `Isoleucine`, `Leucine`, `Lysine`, `Methionine`, `Cystine`,
                    `Phenylalanine`, `Tyrosine`, `Valine`, `Arginine`, `Histidine`, `Alanine`, 
                    `Aspartic_acid`, `Glutamic_acid`, `Glycine`, `Proline`, `Serine`, `Fat`, 
                    `ala`, `epa`, `dpa`, `dha`, `omega6`, `omega3`, `Carb`, `Fiber`, `Sugar`,
                    `Ca`, `Fe`, `Mg`, `P`, `K`, `Na`, `Zn`, `Cu`, `Mn`, `Se`, `V_c`, `B1`,
                    `B2`, `B3`, `B6`, `B9`, `B12`, `V_a`, `V_e`, `V_k`, `tsFat`, `tmsFat`,
                    `tpusFat`, `transFat`, `cholest`, `caffine`, `alcho`, `hydroxyproline`, 
                    `laz`, `V_d`, `sucrose`, `glucose`, `frutose`, `lactose`, `maltose`, 
                    `galctose`, `strach`) 
                    
                    VALUES ('{usda_id}','{name}', 'Fruit', '1', '1', '1', '1', 
                    '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '11', '1', '1', 
                    '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 
                    '1', '1', '1', '1', '11', '1', '1', '1', '1.0', '1.0', '1.0', '1.0', 
                    '1.0', '1.0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                    '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'); """;  

                mycursor.execute(sql_insert);               
                mydb.commit();
                print(f"Done inserting {usda_id} , {name}") 
                
