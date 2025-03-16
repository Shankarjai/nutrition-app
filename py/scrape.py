import requests; 
import lxml.html;
import json;


#https://fdc.nal.usda.gov/portal-data/external/174272

#https://fdc.nal.usda.gov/fdc-app.html#/food-details/174272/nutrients

food_id = 2262074; 

response = requests.get('https://fdc.nal.usda.gov/portal-data/external/'+str(food_id));

# json_res = json.loads(response.text);


json_out = json.loads(response.text);

nutrients = json_out['foodNutrients']; 

attrs = json_out['foodAttributes'];

group = json_out['foodGroup']['id'];

# desc = json_out['description'];
# sci_name = json_out['scientificName'];

our_json = {'id':food_id}; 

if ("description" in json_out):
    our_json['name'] = json_out['description'];

if ("scientificName" in json_out):
    our_json['sname'] = json_out['scientificName'];

# our_json = {'name': json_out['description'],
#             'sname':json_out['scientificName']}; 


if(group == 9):
    our_json['group'] = json_out['foodGroup']['description'];
else:
    pass;


our_keys = {1051:'water', 
            1008:'Kcal',
            1003:'Protein',
            1210:'Tryptophan',
            1211:'Threonine',
            1212:'Isoleucine',
            1213:'Leucine',
            1214:'Lysine',
            1215:'Methionine',
            1216:'Cystine',
            1217:'Phenylalanine',
            1218:'Tyrosine',
            1219:'Valine',
            1220:'Arginine',
            1221:'Histidine',
            1222:'Alanine',
            1223:'Aspartic_acid',
            1224:'Glutamic_acid',
            1225:'Glycine',
            1226:'Proline',
            1227:'Serine',
            1004:'Fat',
            1404:'ala',
            1278:'epa',
            1280:'dpa',
            1272:'dha',
            1269:'omega6',
            1270:'omega3',
            1005:'Carb',
            1079:'Fiber',
            2000:'Sugar',
            1087:'Ca',
            1089:'Fe', 
            1090:'Mg',
            1091:"P",
            1092:'K',
            1093:'Na',
            1095:'Zn',
            1098:'Cu',
            1101:'Mn',
            1103:'Se',
            1162:'V_c',
            1165:'B1',
            1166:'B2',
            1167:'B3',
            1175:'B6',
            1177:'B9',
            1178:'B12',
            1106:'V_a',
            1109:'V_e',
            1185:'V_k',
            1258:'tsFat',
            1292:'tmsFat',
            1293:'tpusFat',
            1257:'transFat',
            1253:'cholest',
            1000:'cname',
            1057:'caffine',
            1018:'alcho',
            1228:'hydroxyproline',
            1123:'laz',
            1114:'V_d',
            1010:'sucrose',
            1011:'glucose',
            1012:'frutose',
            1013:'lactose',
            1014:'maltose',
            1075:'galctose',
            1009:'strach'  

} 

## list of keys

# water = '-'; 
# Kcal = '-';
# Protein = '-';
# Tryptophan = '-';
# Threonine = '-';
# Isoleucine = '-';
# Leucine = '-';
# Lysine = '-';
# Methionine = '-';
# Cystine = '-';
# Phenylalanine = '-';
# Tyrosine = '-';
# Valine = '-';
# Arginine = '-';
# Histidine = '-';
# Alanine = '-';
# Aspartic_acid = '-';
# Glutamic_acid = '-';
# Glycine = '-';
# Proline = '-';
# Serine = '-';
# Fat = '-';
# ala = '-';
# epa = '-';
# dpa = '-';
# dha = '-';
# omega6 = '-';
# omega3 = '-';
# Carb = '-';
# Fiber = '-';
# Sugar = '-';
# Ca = '-';
# Fe = '-'; 
# Mg = '-';
# P = '-';
# K = '-';
# Na = '-';
# Zn = '-';
# Cu = '-';
# Mn = '-';
# Se = '-';
# V_c = '-';
# B1 = '-';
# B2 = '-';
# B3 = '-';
# B6 = '-';
# B9 = '-';
# B12 = '-';
# V_a = '-';
# V_e = '-';
# V_k = '-';
# tsFat = '-';
# tmsFat = '-';
# tpusFat = '-';
# transFat = '-';
# cholest = '-';
# cname = '-';
# caffine = '-';
# alcho = '-';
# hydroxyproline = '-';
# laz = '-';
# V_d = '-';
# sucrose = '-';
# glucose = '-';
# frutose = '-';
# lactose = '-';
# maltose = '-';
# galctose = '-';
# strach = '-';
# id = '-'; 
# name = '-';
# sname = '-';
# group = '-';

for nutrient in nutrients:
    
    try:
        #print(nutrient['nutrient']['name'], ' ', nutrient['value'], nutrient['nutrient']['nutrientUnit']['name'] );
        # print(nutrient['nutrient']['id'])
        id = nutrient['nutrient']['id'] 
        if( id in our_keys):
            # our_json[our_keys[id]] = "{value}{unit}".format(value=nutrient['value'], unit=nutrient['nutrient']['nutrientUnit']['name']);
            our_json[our_keys[id]] = {"v":nutrient['value'], "u":nutrient['nutrient']['nutrientUnit']['name']}
    except:
        pass;


for attr in attrs:

    try:
        id = attr['foodAttributeType']['id'];
        if(id in our_keys):
            our_json[our_keys[id]] = attr['value'];


    except:
        pass;

    
print(our_json); 

file_name = 'foodJson/'+our_json['name'][:6]+'_'+str(food_id)+'.json';


with open(file_name, 'w', encoding='utf8') as f:
    json.dump(our_json, f, ensure_ascii=False, separators=(',', ':'))  

 