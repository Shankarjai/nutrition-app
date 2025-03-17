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
            
            food_name = json_file['name'].replace("'","");
            usda_id = json_file['id'];
            food_category = json_file.get('group', '-');

            # # Water, Kcal, Protein, and Fat values are stored in nested dictionaries
            # water = json_file['water']['v']
            # kcal = json_file['Kcal']['v']
            # protein = json_file['Protein']['v']
            # fat = json_file['Fat']['v']
            # carb = json_file['Carb']['v']
            # fiber = json_file['Fiber']['v']
            # sugar = json_file['Sugar']['v']

            # # Sucrose, Glucose, Fructose, Lactose, Maltose, Galactose, Starch
            # sucrose = json_file['sucrose']['v']
            # glucose = json_file['glucose']['v']
            # fructose = json_file['frutose']['v']
            # lactose = json_file['lactose']['v']
            # maltose = json_file['maltose']['v']
            # galactose = json_file['galctose']['v']
            # starch = json_file['strach']['v']

            # # Minerals
            # ca = json_file['Ca']['v']
            # fe = json_file['Fe']['v']
            # mg = json_file['Mg']['v']
            # p = json_file['P']['v']
            # k = json_file['K']['v']
            # na = json_file['Na']['v']
            # zn = json_file['Zn']['v']
            # cu = json_file['Cu']['v']
            # mn = json_file['Mn']['v']
            # se = json_file['Se']['v']
            # v_c = json_file['V_c']['v']
            # b1 = json_file['B1']['v']
            # b2 = json_file['B2']['v']
            # b3 = json_file['B3']['v']
            # b6 = json_file['B6']['v']
            # b9 = json_file['B9']['v']
            # b12 = json_file['B12']['v']
            # v_a = json_file['V_a']['v']
            # v_e = json_file['V_e']['v']
            # v_k = json_file['V_k']['v']

            # # Additional compounds
            # tsFat = json_file['tsFat']['v']
            # tmsFat = json_file['tmsFat']['v']
            # tpusFat = json_file['tpusFat']['v']
            # omega6 = json_file['omega6']['v']
            # omega3 = json_file['omega3']['v']
            # epa = json_file['epa']['v']
            # dpa = json_file['dpa']['v']
            # dha = json_file['dha']['v']
            # transFat = json_file['transFat']['v']
            # cholest = json_file['cholest']['v']

            # # Amino acids
            # tryptophan = json_file['Tryptophan']['v']
            # threonine = json_file['Threonine']['v']
            # isoleucine = json_file['Isoleucine']['v']
            # leucine = json_file['Leucine']['v']
            # lysine = json_file['Lysine']['v']
            # methionine = json_file['Methionine']['v']
            # cystine = json_file['Cystine']['v']
            # phenylalanine = json_file['Phenylalanine']['v']
            # tyrosine = json_file['Tyrosine']['v']
            # valine = json_file['Valine']['v']
            # arginine = json_file['Arginine']['v']
            # histidine = json_file['Histidine']['v']
            # alanine = json_file['Alanine']['v']
            # aspartic_acid = json_file['Aspartic_acid']['v']
            # glutamic_acid = json_file['Glutamic_acid']['v']
            # glycine = json_file['Glycine']['v']
            # proline = json_file['Proline']['v']
            # serine = json_file['Serine']['v']
            # hydroxyproline = json_file['hydroxyproline']['v']


            # # Alcohol and Caffeine
            # alcohol = json_file['alcho']['v']
            # caffeine = json_file['caffine']['v']

            # # Vitamin D
            # v_d = json_file['V_d']['v']

            # # Other values
            # laz = json_file['laz']['v']

            water = json_file.get('water', {}).get('v', 0)
            kcal = json_file.get('Kcal', {}).get('v', 0)
            protein = json_file.get('Protein', {}).get('v', 0)
            tryptophan = json_file.get('Tryptophan', {}).get('v', 0)
            threonine = json_file.get('Threonine', {}).get('v', 0)
            isoleucine = json_file.get('Isoleucine', {}).get('v', 0)
            leucine = json_file.get('Leucine', {}).get('v', 0)
            lysine = json_file.get('Lysine', {}).get('v', 0)
            methionine = json_file.get('Methionine', {}).get('v', 0)
            cystine = json_file.get('Cystine', {}).get('v', 0)
            phenylalanine = json_file.get('Phenylalanine', {}).get('v', 0)
            tyrosine = json_file.get('Tyrosine', {}).get('v', 0)
            valine = json_file.get('Valine', {}).get('v', 0)
            arginine = json_file.get('Arginine', {}).get('v', 0)
            histidine = json_file.get('Histidine', {}).get('v', 0)
            alanine = json_file.get('Alanine', {}).get('v', 0)
            aspartic_acid = json_file.get('Aspartic_acid', {}).get('v', 0)
            glutamic_acid = json_file.get('Glutamic_acid', {}).get('v', 0)
            glycine = json_file.get('Glycine', {}).get('v', 0)
            proline = json_file.get('Proline', {}).get('v', 0)
            serine = json_file.get('Serine', {}).get('v', 0)
            fat = json_file.get('Fat', {}).get('v', 0)
            ala = json_file.get('ala', {}).get('v', 0)
            epa = json_file.get('epa', {}).get('v', 0)
            dpa = json_file.get('dpa', {}).get('v', 0)
            dha = json_file.get('dha', {}).get('v', 0)
            omega6 = json_file.get('omega6', {}).get('v', 0)
            omega3 = json_file.get('omega3', {}).get('v', 0)
            carb = json_file.get('Carb', {}).get('v', 0)
            fiber = json_file.get('Fiber', {}).get('v', 0)
            sugar = json_file.get('Sugar', {}).get('v', 0)
            sucrose = json_file.get('sucrose', {}).get('v', 0)
            glucose = json_file.get('glucose', {}).get('v', 0)
            fructose = json_file.get('frutose', {}).get('v', 0)
            lactose = json_file.get('lactose', {}).get('v', 0)
            maltose = json_file.get('maltose', {}).get('v', 0)
            galactose = json_file.get('galctose', {}).get('v', 0)
            starch = json_file.get('strach', {}).get('v', 0)

            # Minerals
            ca = json_file.get('Ca', {}).get('v', 0)
            fe = json_file.get('Fe', {}).get('v', 0)
            mg = json_file.get('Mg', {}).get('v', 0)
            p = json_file.get('P', {}).get('v', 0)
            k = json_file.get('K', {}).get('v', 0)
            na = json_file.get('Na', {}).get('v', 0)
            zn = json_file.get('Zn', {}).get('v', 0)
            cu = json_file.get('Cu', {}).get('v', 0)
            mn = json_file.get('Mn', {}).get('v', 0)
            se = json_file.get('Se', {}).get('v', 0)
            v_c = json_file.get('V_c', {}).get('v', 0)
            b1 = json_file.get('B1', {}).get('v', 0)
            b2 = json_file.get('B2', {}).get('v', 0)
            b3 = json_file.get('B3', {}).get('v', 0)
            b6 = json_file.get('B6', {}).get('v', 0)
            b9 = json_file.get('B9', {}).get('v', 0)
            b12 = json_file.get('B12', {}).get('v', 0)
            v_a = json_file.get('V_a', {}).get('v', 0)
            v_e = json_file.get('V_e', {}).get('v', 0)
            v_k = json_file.get('V_k', {}).get('v', 0)
            laz = json_file.get('laz', {}).get('v', 0)
            v_d = json_file.get('v_d', {}).get('v', 0)

            # Additional compounds
            tsFat = json_file.get('tsFat', {}).get('v', 0)
            tmsFat = json_file.get('tmsFat', {}).get('v', 0)
            tpusFat = json_file.get('tpusFat', {}).get('v', 0)
            transFat = json_file.get('transFat', {}).get('v', 0)
            cholest = json_file.get('cholest', {}).get('v', 0)

            # Amino acids
            tryptophan = json_file.get('Tryptophan', {}).get('v', 0)
            threonine = json_file.get('Threonine', {}).get('v', 0)
            isoleucine = json_file.get('Isoleucine', {}).get('v', 0)
            leucine = json_file.get('Leucine', {}).get('v', 0)
            lysine = json_file.get('Lysine', {}).get('v', 0)
            methionine = json_file.get('Methionine', {}).get('v', 0)
            cystine = json_file.get('Cystine', {}).get('v', 0)
            phenylalanine = json_file.get('Phenylalanine', {}).get('v', 0)
            tyrosine = json_file.get('Tyrosine', {}).get('v', 0)
            valine = json_file.get('Valine', {}).get('v', 0)
            arginine = json_file.get('Arginine', {}).get('v', 0)
            histidine = json_file.get('Histidine', {}).get('v', 0)
            alanine = json_file.get('Alanine', {}).get('v', 0)
            aspartic_acid = json_file.get('Aspartic_acid', {}).get('v', 0)
            glutamic_acid = json_file.get('Glutamic_acid', {}).get('v', 0)
            glycine = json_file.get('Glycine', {}).get('v', 0)
            proline = json_file.get('Proline', {}).get('v', 0)
            serine = json_file.get('Serine', {}).get('v', 0)
            hydroxyproline = json_file.get('hydroxyproline', {}).get('v', 0)

            # Alcohol and Caffeine
            alcohol = json_file.get('alcho', {}).get('v', 0)
            caffeine = json_file.get('caffine', {}).get('v', 0)



            sql_get = f"""SELECT * FROM `food` WHERE `usda_id` = {usda_id}""";
            # print(name)
            mycursor.execute(sql_get);
            myresult = mycursor.fetchall();
            if(len(myresult) > 0):
                print(f'{food_name} {usda_id} data exist')
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
                    
                    VALUES ('{usda_id}', '{food_name}', '{food_category}', 
                    '{water}', '{kcal}', '{protein}', '{tryptophan}', '{threonine}', '{isoleucine}', 
                    '{leucine}', '{lysine}', '{methionine}', '{cystine}', '{phenylalanine}', '{tyrosine}', 
                    '{valine}', '{arginine}', '{histidine}', '{alanine}', '{aspartic_acid}', 
                    '{glutamic_acid}', '{glycine}', '{proline}', '{serine}', '{fat}', '{ala}', 
                    '{epa}', '{dpa}', '{dha}', '{omega6}', '{omega3}', '{carb}', '{fiber}', '{sugar}', 
                    '{ca}', '{fe}', '{mg}', '{p}', '{k}', '{na}', '{zn}', '{cu}', '{mn}', '{se}', 
                    '{v_c}', '{b1}', '{b2}', '{b3}', '{b6}', '{b9}', '{b12}', '{v_a}', '{v_e}', 
                    '{v_k}', '{tsFat}', '{tmsFat}', '{tpusFat}', '{transFat}', '{cholest}', 
                    '{caffeine}', '{alcohol}', '{hydroxyproline}', '{laz}', '{v_d}', 
                    '{sucrose}', '{glucose}', '{fructose}', '{lactose}', '{maltose}', '{galactose}', 
                    '{starch}'); """;  

                mycursor.execute(sql_insert);               
                mydb.commit();
                print(f"Done inserting {usda_id} , {food_name}") 
                
