<!DOCTYPE html>

<?php
    $current_page = 'nutrients';
    include 'template/header.php';
?>

<body>

    <?php
        include 'template/sidebar.php';
        include 'config/dbconfig.php'
    ?>

    <div class="page-container">
        <span>nutrients</span>

        <?php

            $pdo = new PDO("mysql:host=$host;dbname=$dbname", "$user", "$password");
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


            $sql = "SELECT * FROM nutrients";

             // Prepare and execute the query
            $stmt = $pdo->prepare($sql);
            $stmt->execute();

            // Fetch all results as an associative array
            $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
            foreach($results as $row){
                echo('<p>'.$row['id'].$row['name'].$row['desc'].'</p>');
            }

            $sql = "SELECT 
                nutrients.name as nutrient_name, 
                nutrient_pros.pro,
                pro_variation.variation_text
                
            FROM nutrients
            LEFT JOIN nutrient_pros on nutrients.id = nutrient_pros.nutrient_id
            LEFT JOIN pro_variation on nutrient_pros.pro_id = pro_variation.pro_id";


            $stmt = $pdo->prepare($sql);
            $stmt->execute();

            $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

            print_r($results) ;

            foreach($results as $row){

                echo ('  <div class="nutrient-card">
            
                            <div class="nutrient-card-header">
                                <button class="button nutrition-toggle">X</button>  
                                <span class="nutrient-card-title">'.$row['nutrient_name'].'</span>
                                <button class="button modify">modify</button>
                                <button class="button delete">delete</button>
                            </div>
                        
                            <div class="nutrient-card-body">
                                <div class="pros-box desc-card">
                                    <p>'.$row['pro'].'</p>

                                </div>
                                <div class="cons-box desc-card">
                                    <p>the nutrient cons will be gone here </p>

                                </div>
                            </div>
                        

                        </div>');
                

            }

        ?>

        <div class="nutrient-card">
            
            <div class="nutrient-card-header">
                <button class="button nutrition-toggle">X</button>  
                <span class="nutrient-card-title">Nutrient Name</span>
                <button class="button modify">modify</button>
                <button class="button delete">delete</button>
            </div>
            
            <div class="nutrient-card-body">
                <div class="pros-box desc-card">
                    <p>the nutrient pros will be gone here </p>
                    <div class="pros-variation-wrapper">
                        <div class="pro-variation desc-card">
                            <p>this is variation 1</p>
                        </div>
                        <div class="pro-variation desc-card">
                            <p>this is variation 2</p>
                        </div>
                    </div>
                </div>
                <div class="cons-box desc-card">
                    <p>the nutrient cons will be gone here </p>

                </div>
            </div>
            

        </div>
    
    
    </div>

</body>
<script>
    <?php include 'js/script.js' ?>
</script>            


</html>
