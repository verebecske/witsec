# 1. Mit csinál a következő program?
```
rand=`echo $((1 + $RANDOM % 100))`

echo "Írj egy számot"
read answer 

until [ $answer -eq $rand ]
do
    if [ $answer -lt $rand ]
    then
        echo "Nem nyert, ennél nagyobb"
        read answer
    else
        echo "Nem nyert, ennél kisebb"
        read answer
    fi
done
```

# 2. Mi a hiba a következő program esetén?
```
<!DOCTYPE html>
<html>

<body>
    <?php
$txt = "PHP";

echo "I $verb $txt!";
?>
</body>

</html>
```