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
            name = json_file['name'];
            id = json_file['id'];
            sql_get = f"""SELECT * FROM `json` WHERE `id` = {id}""";
            # print(name)
            mycursor.execute(sql_get);
            myresult = mycursor.fetchall();
            if(len(myresult) > 0):
                print(f'{name}{id} data exist')
            else:
                sql_insert = f"""INSERT INTO `json` (`id`, `value`) VALUES ('{id}', '{json_dump}'); """;

                mycursor.execute(sql_insert);               
                mydb.commit();
                print(f"Done inserting {id},{name}")
                
