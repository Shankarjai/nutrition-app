<?php

echo($_POST['query']);
echo "<br/>"; 
echo($_POST['query_two']); 

$servername = "localhost";
$username = "root"; 
$password = "";
$dbname = "test";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

/* $sql = "SELECT id, firstname, lastname FROM MyGuests" */

$sql =  "SELECT id, text FROM food_data"  ;
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      echo "id: " . $row["id"]. "<br/> Text: " . $row["text"]. "<br>";
    }
  } else {
    echo "0 results";
  }


?>