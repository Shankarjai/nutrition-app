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
        
        echo $host,'', $dbname,'', $user,'', $password;
        $pdo = new PDO("mysql:host=$host;dbname=$dbname", "$user", "$password");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        
        ?>
    </div>

</body>

</html>
