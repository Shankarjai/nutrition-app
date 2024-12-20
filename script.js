this.nutri_arr = [];

nutri_keys = ["water", "Kcal", "Protein", "Tryptophan", "Threonine","Isoleucine","Leucine","Lysine","Methionine","Cystine","Phenylalanine","Tyrosine","Valine","Arginine","Histidine","Alanine","Aspartic_acid","Glutamic_acid","Glycine","Proline","Serine","Fat","ala","epa","dpa","dha","omega6","omega3","Carb","Fiber","Sugar","Ca","Fe","Mg","P","K","Na","Zn","Cu","Mn","Se","V_c","B1","B2","B3","B6","B9","B12","V_a","V_e","V_k","tsFat","tmsFat","tpusFat","transFat","cholest","cname","caffine","alcho","hydroxyproline","laz","V_d","sucrose","glucose","frutose","lactose","maltose","galctose","strach","id","name","sname","group"]

/* nutri keys missing keys:  */ 

removeLast = function(){
    console.log("remove last func called");
}    

createTable = function(){
    
    for( index in nutri_arr){
        //console.log(foods[i]['name'])
        for(n in nutri_keys){
            //console.log(foods[index][nutr[n]]);
            if(nutri_arr[index][nutri_keys[n]] != undefined){
                
                if(nutri_keys[n] == "name" || nutri_keys[n] == "id" || nutri_keys[n] == "sname" || nutri_keys[n] == "group" || nutri_keys[n] == "cname"){
                    table[nutri_keys[n]].data.push(nutri_arr[index][nutri_keys[n]]);
                    //table[nutr[n]].unit = foods[index][nutr[n]];     
                }else{
                    table[nutri_keys[n]].data.push(nutri_arr[index][nutri_keys[n]].v);
                    table[nutri_keys[n]].unit = nutri_arr[index][nutri_keys[n]].u;     
                }
                
            }else{
                table[nutri_keys[n]].data.push('-');
                //table[nutr[n]].unit = foods[index][nutr[n]].u; 
            }
        }
        //console.log("---------")
    }
}  

flushTableJSON = function(){
    table = {
        "water": {"data":[], "high": 0, "unit": 0} , "Kcal": {"data":[], "high": 0, "unit": 0} , "Protein": {"data":[], "high": 0, "unit": 0} , "Tryptophan": {"data":[], "high": 0, "unit": 0} , "Threonine": {"data":[], "high": 0, "unit": 0} ,"Isoleucine": {"data":[], "high": 0, "unit": 0} ,"Leucine": {"data":[], "high": 0, "unit": 0} ,"Lysine": {"data":[], "high": 0, "unit": 0} ,"Methionine": {"data":[], "high": 0, "unit": 0} ,"Cystine": {"data":[], "high": 0, "unit": 0} ,"Phenylalanine": {"data":[], "high": 0, "unit": 0} ,"Tyrosine": {"data":[], "high": 0, "unit": 0} ,"Valine": {"data":[], "high": 0, "unit": 0} ,"Arginine": {"data":[], "high": 0, "unit": 0} ,"Histidine": {"data":[], "high": 0, "unit": 0} ,"Alanine": {"data":[], "high": 0, "unit": 0} ,"Aspartic_acid": {"data":[], "high": 0, "unit": 0} ,"Glutamic_acid": {"data":[], "high": 0, "unit": 0} ,"Glycine": {"data":[], "high": 0, "unit": 0} ,"Proline": {"data":[], "high": 0, "unit": 0} ,"Serine": {"data":[], "high": 0, "unit": 0} ,"Fat": {"data":[], "high": 0, "unit": 0} ,"ala": {"data":[], "high": 0, "unit": 0} ,"epa": {"data":[], "high": 0, "unit": 0} ,"dpa": {"data":[], "high": 0, "unit": 0} ,"dha": {"data":[], "high": 0, "unit": 0} ,"omega6": {"data":[], "high": 0, "unit": 0} ,"omega3": {"data":[], "high": 0, "unit": 0} ,"Carb": {"data":[], "high": 0, "unit": 0} ,"Fiber": {"data":[], "high": 0, "unit": 0} ,"Sugar": {"data":[], "high": 0, "unit": 0} ,"Ca": {"data":[], "high": 0, "unit": 0} ,"Fe": {"data":[], "high": 0, "unit": 0} ,"Mg": {"data":[], "high": 0, "unit": 0} ,"P": {"data":[], "high": 0, "unit": 0} ,"K": {"data":[], "high": 0, "unit": 0} ,"Na": {"data":[], "high": 0, "unit": 0} ,"Zn": {"data":[], "high": 0, "unit": 0} ,"Cu": {"data":[], "high": 0, "unit": 0} ,"Mn": {"data":[], "high": 0, "unit": 0} ,"Se": {"data":[], "high": 0, "unit": 0} ,"V_c": {"data":[], "high": 0, "unit": 0} ,"B1": {"data":[], "high": 0, "unit": 0} ,"B2": {"data":[], "high": 0, "unit": 0} ,"B3": {"data":[], "high": 0, "unit": 0} ,"B6": {"data":[], "high": 0, "unit": 0} ,"B9": {"data":[], "high": 0, "unit": 0} ,"B12": {"data":[], "high": 0, "unit": 0} ,"V_a": {"data":[], "high": 0, "unit": 0} ,"V_e": {"data":[], "high": 0, "unit": 0} ,"V_k": {"data":[], "high": 0, "unit": 0} ,"tsFat": {"data":[], "high": 0, "unit": 0} ,"tmsFat": {"data":[], "high": 0, "unit": 0} ,"tpusFat": {"data":[], "high": 0, "unit": 0} ,"transFat": {"data":[], "high": 0, "unit": 0} ,"cholest": {"data":[], "high": 0, "unit": 0} ,"cname": {"data":[], "high": 0, "unit": 0} ,"caffine": {"data":[], "high": 0, "unit": 0} ,"alcho": {"data":[], "high": 0, "unit": 0} ,"hydroxyproline": {"data":[], "high": 0, "unit": 0} ,"laz": {"data":[], "high": 0, "unit": 0} ,"V_d": {"data":[], "high": 0, "unit": 0} ,"sucrose": {"data":[], "high": 0, "unit": 0} ,"glucose": {"data":[], "high": 0, "unit": 0} ,"frutose": {"data":[], "high": 0, "unit": 0} ,"lactose": {"data":[], "high": 0, "unit": 0} ,"maltose": {"data":[], "high": 0, "unit": 0} ,"galctose": {"data":[], "high": 0, "unit": 0} ,"strach": {"data":[], "high": 0, "unit": 0} ,"id": {"data":[], "high": 0} ,"name": {"data":[], "high": 0} ,"sname": {"data":[], "high": 0} ,"group": {"data":[], "high": 0}, "pop" : removeLast
                          
        } 
}

flushTableHeader = function(){
   
    let header_length = $('#table-header-row').children().length;
    for(let x=header_length-1; x>0; x--){
        $('#table-header-row').children()[x].remove();
    }
    
}

removeTableIndexData = function(index){

    for(i in nutri_keys){
        // table[nutri_keys[i]].data = table[nutri_keys[i]].data.slice(index,1);
        table[nutri_keys[i]].data.splice(index,1);
    }

}


removeNutrIndexData = function(index){
    nutri_arr.splice(index,1);
}

removeFood = function(e){
    //console.log(e.target.attributes.click_i.value);
    removeTableIndexData(e.target.attributes.click_i.value);
    removeNutrIndexData(e.target.attributes.click_i.value);
    renderTableHeader();
    renderTableBody();
    showHigh();
}

renderTableHeader = function(){
    flushTableHeader();
    // for(index in nutri_arr){
    //     $("#table-header-row").append(`<th>${nutri_arr[index].name}</th>`)
    //     //console.log(nutri_arr[index].name);
    // } 
    
    for(index in table.name.data){
        $("#table-header-row").append(`<th id="header-${index}" fi="${index}">${table.name.data[index]}<span onClick="removeFood(event)" click_i="${index}"> &#9421;</span></th>`) 
    }
}


flushTableBody = function(){

    // for(i in nutri_keys){
    //     let row_length = table[nutri_keys[i]].data.length;
    //     for(let x = row_length-1; x > 0; x--){
    //         $(`#${nutri_keys[i]}-row`).children()[x].remove();    
    //     }
    // }

    /* working on this */ 
    for( i in nutri_keys){
        let tbody_length = $(`#${nutri_keys[i]}-row`).children().length;
        for(let x=tbody_length-1; x>0; x--){
            $(`#${nutri_keys[i]}-row`).children()[x].remove();
        }
    }

    

    

}

idExist = function(_id){
    for(let i=0; i<nutri_arr.length; i++){
        if(nutri_arr[i].id == _id){
            return true;
        }
    }
}

showHigh = function(){

    if(nutri_arr.length > 1){

        for(let i in nutri_keys){
        
            let arr = table[nutri_keys[i]].data;
            let h_index = arr.reduce((iMax, x, i, arr) => x > arr[iMax] ? i : iMax, 0);
            table[nutri_keys[i]].high = h_index;
            $(`#${nutri_keys[i]}-value-${h_index}`).css({'font-weight':'600'});
            $(`#${nutri_keys[i]}-value-${h_index}`).css({'color':'#970d2e'}); 
        }

    }

    
}

renderTableBody = function(){
    //debugger;
    flushTableBody();
    for(i in nutri_keys){
        //console.log(nutri_keys[i]);
        let row_length = table[nutri_keys[i]].data.length;
        let unit;

        if(table[nutri_keys[i]].unit == 0){
            unit = '';     
        }else{
            unit = table[nutri_keys[i]].unit;
        }
        

        for(let x=0; x <= row_length-1; x++){

            if(table[nutri_keys[i]].data[x] == '-'){
                unit = '';
            }else{
                unit = table[nutri_keys[i]].unit;
            } 

            $(`#${nutri_keys[i]}-row`).append(`<td id="${nutri_keys[i]}-value-${x}" fi="${x}"class="nutrient-value">${table[nutri_keys[i]].data[x]} ${unit ? unit : ''}</td>`);
            //console.log(`#${nutri_keys[i]}-row`, ':', table[nutri_keys[i]].data[x] )
        }

    }
}


this.table = {
    "water": {"data":[], "high": 0, "unit": 0} , "Kcal": {"data":[], "high": 0, "unit": 0} , "Protein": {"data":[], "high": 0, "unit": 0} , "Tryptophan": {"data":[], "high": 0, "unit": 0} , "Threonine": {"data":[], "high": 0, "unit": 0} ,"Isoleucine": {"data":[], "high": 0, "unit": 0} ,"Leucine": {"data":[], "high": 0, "unit": 0} ,"Lysine": {"data":[], "high": 0, "unit": 0} ,"Methionine": {"data":[], "high": 0, "unit": 0} ,"Cystine": {"data":[], "high": 0, "unit": 0} ,"Phenylalanine": {"data":[], "high": 0, "unit": 0} ,"Tyrosine": {"data":[], "high": 0, "unit": 0} ,"Valine": {"data":[], "high": 0, "unit": 0} ,"Arginine": {"data":[], "high": 0, "unit": 0} ,"Histidine": {"data":[], "high": 0, "unit": 0} ,"Alanine": {"data":[], "high": 0, "unit": 0} ,"Aspartic_acid": {"data":[], "high": 0, "unit": 0} ,"Glutamic_acid": {"data":[], "high": 0, "unit": 0} ,"Glycine": {"data":[], "high": 0, "unit": 0} ,"Proline": {"data":[], "high": 0, "unit": 0} ,"Serine": {"data":[], "high": 0, "unit": 0} ,"Fat": {"data":[], "high": 0, "unit": 0} ,"ala": {"data":[], "high": 0, "unit": 0} ,"epa": {"data":[], "high": 0, "unit": 0} ,"dpa": {"data":[], "high": 0, "unit": 0} ,"dha": {"data":[], "high": 0, "unit": 0} ,"omega6": {"data":[], "high": 0, "unit": 0} ,"omega3": {"data":[], "high": 0, "unit": 0} ,"Carb": {"data":[], "high": 0, "unit": 0} ,"Fiber": {"data":[], "high": 0, "unit": 0} ,"Sugar": {"data":[], "high": 0, "unit": 0} ,"Ca": {"data":[], "high": 0, "unit": 0} ,"Fe": {"data":[], "high": 0, "unit": 0} ,"Mg": {"data":[], "high": 0, "unit": 0} ,"P": {"data":[], "high": 0, "unit": 0} ,"K": {"data":[], "high": 0, "unit": 0} ,"Na": {"data":[], "high": 0, "unit": 0} ,"Zn": {"data":[], "high": 0, "unit": 0} ,"Cu": {"data":[], "high": 0, "unit": 0} ,"Mn": {"data":[], "high": 0, "unit": 0} ,"Se": {"data":[], "high": 0, "unit": 0} ,"V_c": {"data":[], "high": 0, "unit": 0} ,"B1": {"data":[], "high": 0, "unit": 0} ,"B2": {"data":[], "high": 0, "unit": 0} ,"B3": {"data":[], "high": 0, "unit": 0} ,"B6": {"data":[], "high": 0, "unit": 0} ,"B9": {"data":[], "high": 0, "unit": 0} ,"B12": {"data":[], "high": 0, "unit": 0} ,"V_a": {"data":[], "high": 0, "unit": 0} ,"V_e": {"data":[], "high": 0, "unit": 0} ,"V_k": {"data":[], "high": 0, "unit": 0} ,"tsFat": {"data":[], "high": 0, "unit": 0} ,"tmsFat": {"data":[], "high": 0, "unit": 0} ,"tpusFat": {"data":[], "high": 0, "unit": 0} ,"transFat": {"data":[], "high": 0, "unit": 0} ,"cholest": {"data":[], "high": 0, "unit": 0} ,"cname": {"data":[], "high": 0, "unit": 0} ,"caffine": {"data":[], "high": 0, "unit": 0} ,"alcho": {"data":[], "high": 0, "unit": 0} ,"hydroxyproline": {"data":[], "high": 0, "unit": 0} ,"laz": {"data":[], "high": 0, "unit": 0} ,"V_d": {"data":[], "high": 0, "unit": 0} ,"sucrose": {"data":[], "high": 0, "unit": 0} ,"glucose": {"data":[], "high": 0, "unit": 0} ,"frutose": {"data":[], "high": 0, "unit": 0} ,"lactose": {"data":[], "high": 0, "unit": 0} ,"maltose": {"data":[], "high": 0, "unit": 0} ,"galctose": {"data":[], "high": 0, "unit": 0} ,"strach": {"data":[], "high": 0, "unit": 0} ,"id": {"data":[], "high": 0} ,"name": {"data":[], "high": 0} ,"sname": {"data":[], "high": 0} ,"group": {"data":[], "high": 0}, "pop" : removeLast
                      
    } 

let base_url = 'http://localhost/nutri/';    

var url = `${base_url}request.php`
var button = document.getElementById("json");
button.onclick = function(){
        fetch(url)
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            return response.json(); // Parse the response as JSON
        })
        .then(data => {
            
            nutri_arr.push(JSON.parse(data));
            
            // Now you can work with the JSON data in the "data" variable
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }


var sbutton = document.getElementById("search_submit");
sbutton.onclick = function(){
        var sqlurl = `${base_url}request.php?q=${document.getElementById('search').value}`;

        if( idExist(parseInt(document.getElementById('search').value)) ){
            console.log("id already exist");
        }else{

            fetch(sqlurl)
            .then(response => {
                if (!response.ok) {
                throw new Error('Network response was not ok');
                }
                return response.json(); // Parse the response as JSON
            })
            .then(data => {
                
                let final_json = JSON.parse(data); 

                if(final_json.result == 0){

                    
                    document.getElementById('result_status').innerText = `No result for ${document.getElementById('search').value}`;

                }else{

                    nutri_arr.push(final_json);
                    // Now you can work with the JSON data in the "data" variable
                    //console.log(data);
                    
                    flushTableJSON();
                    createTable();
                    renderTableHeader();
                    renderTableBody(); 
                    showHigh();
                    
                    
                    document.getElementById('result_status').innerText = `Result for ${document.getElementById('search').value} added on array`;

                }

                
            })
            .catch(error => {
                console.error('Error:', error);
            });    

        }

        
    }  
     