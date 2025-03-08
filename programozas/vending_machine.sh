#!/bin/bash

declare -A drink_names=(
    [1]="Kávé"
    [2]="Tea"
    [3]="Forró csoki"
    [4]="Víz"
)

declare -A drink_prices=(
    [1]=250
    [2]=200
    [3]=300
    [4]=150
)

print_drinks() {
    echo "Válassz egy italt:"
    for key in 1 2 3 4; do
    # for key in "${!drink_names[@]}"; do
        echo "$key: ${drink_names[$key]} - ${drink_prices[$key]} Ft"
    done
}

choose_drink() {
    local choice
    while true; do
        read -p "Add meg a választott ital számát: " choice
        if [[ 0 < $choice && $choice < 5 ]]; then
            echo "${drink_names[$choice]} választva. Ár: ${drink_prices[$choice]} Ft" >&2
            echo $choice
            return
        else
            echo "Érvénytelen választás." >&2
        fi
    done
}

pay_drink() {
    local choice=$1    
    local inserted_money
    local price=${drink_prices[$choice]}
    local name=${drink_names[$choice]}
    read -p "Dobd be a pénzt: " inserted_money
    
    if (( inserted_money < price )); then
        echo "Nincs elég pénzed az italhoz."
    elif (( inserted_money > price )); then
        echo "Itt a $name, és a visszajáró: $((inserted_money - price)) Ft."
    else
        echo "Itt a $name. Köszönjük a vásárlást!"
    fi
}

vending_machine() {
    while true; do
        echo "Üdvözöl az italautomata!"
        print_drinks
        choice=$(choose_drink)
        pay_drink $choice
    done
}

vending_machine
