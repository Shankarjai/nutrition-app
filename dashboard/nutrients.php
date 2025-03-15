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
        

        <?php

            $pdo = new PDO("mysql:host=$host;dbname=$dbname", "$user", "$password");
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $sql = "SELECT nutrients.id AS nutrient_id, nutrients.name AS nutrient_name, nutrient_pros.pro, nutrient_pros.pro_id
                    FROM nutrients
                    LEFT JOIN nutrient_pros ON nutrients.id = nutrient_pros.nutrient_id";


            $stmt = $pdo->prepare($sql);
            $stmt->execute();

            $nutrients = $stmt->fetchAll(PDO::FETCH_ASSOC);

            $results = [];

            //print_r($nutrients) ;


            foreach($nutrients as $row){

                $nutrient_id = $row['nutrient_id'];
                $pro_id = $row['pro_id'];

                 // Second query: Get variations for this pro_id
                $variationStmt = $pdo->prepare("SELECT variation_text FROM pro_variation WHERE pro_id = ?");
                $variationStmt->execute([$pro_id]);
                $variations = $variationStmt->fetchAll(PDO::FETCH_COLUMN);

                // Store data in an array
                $results[$nutrient_id]['name'] = $row['nutrient_name'];
                $results[$nutrient_id]['pros'][] = [
                    'pro' => $row['pro'],
                    'variations' => $variations
                ];

            }

            foreach($results as $_row){


                echo('
                
                    <div class="nutrient-card">
                        <div class="nutrient-card-header">
                            <button class="button nutrition-toggle">X</button>  
                                <span class="nutrient-card-title">'.$_row['name'].'</span>
                            <button class="button modify">modify</button>
                            <button class="button delete">delete</button>
                        </div>

                        <div class="nutrient-card-body">

                        
                            
                ');


                foreach($_row['pros'] as $_pros){

                    echo('
                            
                            <div class="pros-box desc-card">
                            <p>'.$_pros['pro'].'</p>
                            <div class="pros-variation-wrapper">
                                
                    ');

                    foreach($_pros['variations'] as $_variation ){

                        echo('

                            <div class="pro-variation desc-card">
                                <p>'.$_variation.'</p>
                            </div>
                        
                        ');
                    }

                    echo('</div>'); // closed pro-variation-wrapper
                    echo('</div>'); // closed pros-box desc-card

                }

                
                echo('</div>'); // closed nutrient-card-body
                echo('</div>'); // closed nutrient-card

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