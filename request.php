<?php
// $jsonData = '{"key1": "value1", "key2": "value2", "key3": "value3"}';
// header('Content-Type: application/json; charset=utf-8');
// echo json_encode($jsonData);

$jsonData;
header('Content-Type: application/json; charset=utf-8');

$servername = "localhost";
$username = "root"; 
$password = "";
$dbname = "food";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

$query =  $_GET['q'];

/* $sql = "SELECT id, firstname, lastname FROM MyGuests" */

$sql =  "SELECT value FROM json WHERE id={$query} ";
$result = $conn->query($sql);


// print_r($result);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    //   echo "id: " . $row["id"]. "<br/> Text: " . $row["text"]. "<br>";
        $jsonData = $row['value'];
        echo json_encode($jsonData);
    }
  } else {
    echo json_encode('{"result":0}');
  }



?>