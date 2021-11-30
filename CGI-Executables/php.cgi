#!/usr/bin/php

<?php

    $link = mysqli_connect("127.0.0.1","root","myroot","test") or die("Connet Error: " . mysqli_connect_error());
    $link->query("SET NAMES utf8"); 
    $sql    = "SELECT * FROM `books` ";
    $result = mysqli_query($link, $sql);

    echo "mysqli_connect  database: test table: books\n\n";

    while( $row = $result->fetch_array(MYSQLI_ASSOC) )
    {
        $id = $row['id'];
        $name = $row['name'];
        echo "($id) : $name \n";
    } 

    mysqli_free_result($result);
    mysqli_close($link);

    die();
?>