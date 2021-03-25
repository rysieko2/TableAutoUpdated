<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Koronawirus - Polska/Włochy - Tabela</title>
    <link href="corona.css" rel="stylesheet" type="text/css" media="all" />
    <link href='http://fonts.googleapis.com/css?family=Lato|Josefin+Sans&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
</head>
<body>
<section id='all'>
<div>
<?php
    session_start();
    require_once "connect.php";
	$polaczenie = @new mysqli($host, $db_user, $db_password, $db_name);
	
	if ($polaczenie->connect_errno!=0)
	{
		echo "Error: ".$polaczenie->connect_errno;
	}
	else
	{
     $rezultat = @$polaczenie->query(sprintf("SELECT * FROM zarazenia ORDER BY date DESC"));
     $polaczenie->close();
	}
?>

<table id='table' style="width: 50%;">
<tr id='korona'>
    <th id='koronawirus' colspan=9"><center><b>POLSKI COVID</b></center></th>
</tr>
<tr >
    <th id='zakazenia' colspan="9"><center><b>ZAKAŻENIA AUTOMATYCZNIE AKTUALIZOWANE</b></center></th>
</tr>
</table>
<table>
<tr >
	<th>Data</th>
	<th>Zakażenia Razem</th>
	<th>Zakażenia Dniami</th>
	<th>Zgony Razem</th>
	<th>Zgony Dniami </th>
    <th>Ozdrowieńcy Razem</th>
    <th>Ozdrowieńcy Dniami</th>
    <th>Aktywni Razem</th>
    <th>Aktywni Dniami</th>
</tr>

<?php
$licz = 0;
$licznik = 0;
while($wiersz= $rezultat->fetch_assoc())
{
    if ($licznik == 0){
        echo '<tr class="white">';
        $licznik++;
    }
    else{
        echo '<tr class="silver">';
        $licznik = 0;
    }
    echo "<td>".$wiersz['date']."</td>";
    echo "<td>".$wiersz['plZar']."</td>";
    if ($licz == 0){
        echo '<td class="przyr">'.$wiersz['plPrz']."</td>";
    }
    else{
        echo "<td>".$wiersz['plPrz']."</td>";
    }




    echo "<td>".$wiersz['plZgo']."</td>";
    if ($licz == 0){
        echo '<td class="przyr">'.$wiersz['plZP']."</td>";
    }
    else{
        echo "<td>".$wiersz['plZP']."</td>";
    }



    echo "<td>".$wiersz['wlZar']."</td>";

    if ($licz == 0){
        echo '<td class="przyr">'.$wiersz['wlPrz']."</td>";
    }
    else{
        echo "<td>".$wiersz['wlPrz']."</td>";
    }




    echo "<td>".$wiersz['wlZgo']."</td>";
    if ($licz == 0){
        echo '<td class="przyr">'.$wiersz['wlZP']."</td>";
    }
    else{
        echo "<td>".$wiersz['wlZP']."</td>";
    }
    echo "</tr>";

    $licz++;
    

}

?>
</table>
</div>

<section class="rectangle">2020 &copy; Krzysztof Kordecki - <a href='index.html' class='portfolio'>Portfolio!</a> <i class="icon-mail-alt"></i></section>

</section>
</body>
</html>


