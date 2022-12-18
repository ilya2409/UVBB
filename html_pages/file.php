<?php
$name = $_POST['name'];
$surname = $_POST['surname'];
$file = fopen("file.txt","a+");
fwrite($file,"\n $name:$surname \n");
fclose($file);
?