<!DOCTYPE html>

<?php
    $current_page = 'food';
    include 'template/header.php';
?>

<body>

    <?php
        include 'template/sidebar.php';
        include 'config/dbconfig.php'
    ?>

   

    <div class="page-container">
        

        <?php
        //echo $host,'', $dbname,'', $user,'', $password;
        $pdo = new PDO("mysql:host=$host;dbname=$dbname", "$user", "$password");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        
        ?>

        <div class="food-table-container">
            <table id="foodTable" class="display" style="width:100%">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Office</th>
                        <th>Age</th>
                        <th>Start date</th>
                        <th>Salary</th>
                       
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Tiger Nixon</td>
                        <td>System Architect</td>
                        <td>Edinburgh</td>
                        <td>61</td>
                        <td>2011-04-25</td>
                        <td>$320,800</td>
                       
                    </tr>
                    <tr>
                        <td>Garrett Winters</td>
                        <td>Accountant</td>
                        <td>Tokyo</td>
                        <td>63</td>
                        <td>2011-07-25</td>
                        <td>$170,750</td>
                       
                    </tr>
    

                </tbody>
       
            </table>
        </div>
        

    </div>


</body>

<script>
    <?php include 'js/datatable.js' ?> 
</script>  

</html>
