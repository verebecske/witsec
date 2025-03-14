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
