<!DOCTYPE html>

    <title>
        PHP
    </title>

    <head>
        <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"> 
        <link rel="stylesheet" href="styles.css">
    </head>

    <body>
        <form action="result.php" method="post">
            <label>Food 1</label>    
            <input type="text" name="query">
            <label>Food 2</label>
            <input type="text" name="query_two">
            <button type="submit" > submit </button>
        </form>

        <button id="json">Json</button>
        <br/>
        <input id="search" />
        <button id="search_submit">submit</button>
        <p id="result_status"></p>
        <table id="table">
            <tbody >
                <tr id="table-header-row">
                    <th>Foods</th>
                    
                    
                </tr>

                <tr id="water-row">
                        <td id="water" class="nutrient-name">water</td>
                        
                </tr>
                <tr id="Kcal-row">
                        <td id="Kcal" class="nutrient-name">Kcal</td>
                        
                </tr>
                <tr id="Protein-row">
                        <td id="Protein" class="nutrient-name">Protein</td>
                        
                </tr>
                <tr id="Tryptophan-row">
                        <td id="Tryptophan" class="nutrient-name">Tryptophan</td>
                        
                </tr>
                <tr id="Threonine-row">
                        <td id="Threonine" class="nutrient-name">Threonine</td>
                       
                </tr>
                <tr id="Isoleucine-row">
                        <td id="Isoleucine" class="nutrient-name">Isoleucine</td>
                        
                </tr>
                <tr id="Leucine-row">
                        <td id="Leucine" class="nutrient-name">Leucine</td>
                       
                </tr>
                <tr id="Lysine-row">
                        <td id="Lysine" class="nutrient-name">Lysine</td>
                        
                </tr>
                <tr id="Methionine-row">
                        <td id="Methionine" class="nutrient-name">Methionine</td>
                        
                </tr>
                <tr id="Cystine-row">
                        <td id="Cystine" class="nutrient-name">Cystine</td>
                       
                </tr>
                <tr id="Phenylalanine-row">
                        <td id="Phenylalanine" class="nutrient-name">Phenylalanine</td>
                        
                </tr>
                <tr id="Tyrosine-row">
                        <td id="Tyrosine" class="nutrient-name">Tyrosine</td>
                        
                </tr>
                <tr id="Valine-row">
                        <td id="Valine" class="nutrient-name">Valine</td>
                        
                </tr>
                <tr id="Arginine-row">
                        <td id="Arginine" class="nutrient-name">Arginine</td>
                        
                </tr>
                <tr id="Histidine-row">
                        <td id="Histidine" class="nutrient-name">Histidine</td>
                        
                </tr>
                <tr id="Alanine-row">
                        <td id="Alanine" class="nutrient-name">Alanine</td>
                        
                </tr>
                <tr id="Aspartic_acid-row">
                        <td id="Aspartic_acid" class="nutrient-name">Aspartic_acid</td>
                        
                </tr>
                <tr id="Glutamic_acid-row">
                        <td id="Glutamic_acid" class="nutrient-name">Glutamic_acid</td>
                       
                </tr>
                <tr id="Glycine-row">
                        <td id="Glycine" class="nutrient-name">Glycine</td>
                        
                </tr>
                <tr id="Proline-row">
                        <td id="Proline" class="nutrient-name">Proline</td>
                        
                </tr>
                <tr id="Serine-row">
                        <td id="Serine" class="nutrient-name">Serine</td>
                        
                </tr>
                <tr id="Fat-row">
                        <td id="Fat" class="nutrient-name">Fat</td>
                       
                </tr>
                <tr id="ala-row">
                        <td id="ala" class="nutrient-name">ala</td>
                        
                </tr>
                <tr id="epa-row">
                        <td id="epa" class="nutrient-name">epa</td>
                        
                </tr>
                <tr id="dpa-row">
                        <td id="dpa" class="nutrient-name">dpa</td>
                        
                </tr>
                <tr id="dha-row">
                        <td id="dha" class="nutrient-name">dha</td>
                        
                </tr>
                <tr id="omega6-row">
                        <td id="omega6" class="nutrient-name">omega6</td>
                        
                </tr>
                <tr id="omega3-row">
                        <td id="omega3" class="nutrient-name">omega3</td>
                        
                </tr>
                <tr id="Carb-row">
                        <td id="Carb" class="nutrient-name">Carb</td>
                        
                </tr>
                <tr id="Fiber-row">
                        <td id="Fiber" class="nutrient-name">Fiber</td>
                        
                </tr>
                <tr id="Sugar-row">
                        <td id="Sugar" class="nutrient-name">Sugar</td>
                        
                </tr>
                <tr id="Ca-row">
                        <td id="Ca" class="nutrient-name">Ca</td>
                        
                </tr>
                <tr id="Fe-row">
                        <td id="Fe" class="nutrient-name">Fe</td>
                        
                </tr>
                <tr id="Mg-row">
                        <td id="Mg" class="nutrient-name">Mg</td>
                        
                </tr>
                <tr id="P-row">
                        <td id="P" class="nutrient-name">P</td>
                        
                </tr>
                <tr id="K-row">
                        <td id="K" class="nutrient-name">K</td>
                        
                </tr>
                <tr id="Na-row">
                        <td id="Na" class="nutrient-name">Na</td>
                        
                </tr>
                <tr id="Zn-row">
                        <td id="Zn" class="nutrient-name">Zn</td>
                        
                </tr>
                <tr id="Cu-row">
                        <td id="Cu" class="nutrient-name">Cu</td>
                        
                </tr>
                <tr id="Mn-row">
                        <td id="Mn" class="nutrient-name">Mn</td>
                        
                </tr>
                <tr id="Se-row">
                        <td id="Se" class="nutrient-name">Se</td>
                        
                </tr>
                <tr id="V_c-row">
                        <td id="V_c" class="nutrient-name">V_c</td>
                        
                </tr>
                <tr id="B1-row">
                        <td id="B1" class="nutrient-name">B1</td>
                        
                </tr>
                <tr id="B2-row">
                        <td id="B2" class="nutrient-name">B2</td>
                        
                </tr>
                <tr id="B3-row">
                        <td id="B3" class="nutrient-name">B3</td>
                        
                </tr>
                <tr id="B6-row">
                        <td id="B6" class="nutrient-name">B6</td>
                        
                </tr>
                <tr id="B9-row">
                        <td id="B9" class="nutrient-name">B9</td>
                        
                </tr>
                <tr id="B12-row">
                        <td id="B12" class="nutrient-name">B12</td>
                        
                </tr>
                <tr id="V_a-row">
                        <td id="V_a" class="nutrient-name">V_a</td>
                        
                </tr>
                <tr id="V_e-row">
                        <td id="V_e" class="nutrient-name">V_e</td>
                        
                </tr>
                <tr id="V_k-row">
                        <td id="V_k" class="nutrient-name">V_k</td>
                        
                </tr>
                <tr id="tsFat-row">
                        <td id="tsFat" class="nutrient-name">tsFat</td>
                        
                </tr>
                <tr id="tmsFat-row">
                        <td id="tmsFat" class="nutrient-name">tmsFat</td>
                        
                </tr>
                <tr id="tpusFat-row">
                        <td id="tpusFat" class="nutrient-name">tpusFat</td>
                        
                </tr>
                <tr id="transFat-row">
                        <td id="transFat" class="nutrient-name">transFat</td>
                        
                </tr>
                <tr id="cholest-row">
                        <td id="cholest" class="nutrient-name">cholest</td>
                        
                </tr>
                <tr id="cname-row">
                        <td id="cname" class="nutrient-name">cname</td>
                       
                </tr>
                <tr id="caffine-row">
                        <td id="caffine" class="nutrient-name">caffine</td>
                        
                </tr>
                <tr id="alcho-row">
                        <td id="alcho" class="nutrient-name">alcho</td>
                        
                </tr>
                <tr id="hydroxyproline-row">
                        <td id="hydroxyproline" class="nutrient-name">hydroxyproline</td>
                        
                </tr>
                <tr id="laz-row">
                        <td id="laz" class="nutrient-name">laz</td>
                        
                </tr>
                <tr id="V_d-row">
                        <td id="V_d" class="nutrient-name">V_d</td>
                        
                </tr>
                <tr id="sucrose-row">
                        <td id="sucrose" class="nutrient-name">sucrose</td>
                        
                </tr>
                <tr id="glucose-row">
                        <td id="glucose" class="nutrient-name">glucose</td>
                        
                </tr>
                <tr id="frutose-row">
                        <td id="frutose" class="nutrient-name">frutose</td>
                        
                </tr>
                <tr id="lactose-row">
                        <td id="lactose" class="nutrient-name">lactose</td>
                        
                </tr>
                <tr id="maltose-row">
                        <td id="maltose" class="nutrient-name">maltose</td>
                        
                </tr>
                <tr id="galctose-row">
                        <td id="galctose" class="nutrient-name">galctose</td>
                        
                </tr>
                <tr id="strach-row">
                        <td id="strach" class="nutrient-name">strach</td>
                        
                </tr>
                <!-- <tr id="id-row">
                        <td id="id" class="nutrient-name">id</td>
                        
                </tr>
                <tr id="name-row">
                        <td id="name" class="nutrient-name">name</td>
                        
                </tr>
                <tr id="sname-row">
                        <td id="sname" class="nutrient-name">sname</td>
                        
                </tr>
                <tr id="group-row">
                        <td id="group" class="nutrient-name">group</td>
                        
                </tr> -->

                
                


            </tbody>
        </table> 

    </body>

    <script src="script.js"></script> 

    <script>

        // this.nutri_arr = [];

        // var nutri_arr2 = [];

        // var url = 'http://localhost/php/request.php'
        // var button = document.getElementById("json");
        // button.onclick = function(){
        //         fetch(url)
        //         .then(response => {
        //             if (!response.ok) {
        //             throw new Error('Network response was not ok');
        //             }
        //             return response.json(); // Parse the response as JSON
        //         })
        //         .then(data => {
                    
        //             nutri_arr.push(JSON.parse(data));
        //             // Now you can work with the JSON data in the "data" variable
        //             console.log(data);
        //         })
        //         .catch(error => {
        //             console.error('Error:', error);
        //         });
        //     }

       
        // var sbutton = document.getElementById("search_submit");
        // sbutton.onclick = function(){
        //         var sqlurl = `http://localhost/php/request.php?q=${document.getElementById('search').value}`;

        //         fetch(sqlurl)
        //         .then(response => {
        //             if (!response.ok) {
        //             throw new Error('Network response was not ok');
        //             }
        //             return response.json(); // Parse the response as JSON
        //         })
        //         .then(data => {
                    
        //             let final_json = JSON.parse(data); 

        //             if(final_json.result == 0){

                        
        //                 document.getElementById('result_status').innerText = `No result for ${document.getElementById('search').value}`;

        //             }else{

        //                 nutri_arr.push(final_json);
        //                 // Now you can work with the JSON data in the "data" variable
        //                 console.log(data);
        //                 // let table = document.getElementById('table').getElementsByTagName('tbody')[0];
        //                 // for (n in nutri_arr[0]){
        //                 //     let row = table.insertRow();
                            
        //                 //     let cell = row.insertCell()
        //                 //     let name = document.createTextNode(n);
        //                 //     cell.appendChild(name);

        //                 //     let cell2 = row.insertCell(); 
        //                 //     let value = document.createTextNode(nutri_arr[0][n]);
        //                 //     cell2.appendChild(value);

        //                 // }
        //                 document.getElementById('result_status').innerText = `Result for ${document.getElementById('search').value} added on array`;

        //             }

                    
        //         })
        //         .catch(error => {
        //             console.error('Error:', error);
        //         });
        //     }  
            
            

    </script>

</html>



