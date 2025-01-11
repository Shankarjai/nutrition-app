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
