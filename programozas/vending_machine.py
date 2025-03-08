drinks = {
    "1": {"name": "Kávé", "price": 250},
    "2": {"name": "Tea", "price": 200},
    "3": {"name": "Forró csoki", "price": 300},
    "4": {"name": "Víz", "price": 150},
}


def print_drinks():
    print("Válassz egy italt:")
    for code, data in drinks.items():
        print(f"{code}: {data['name']} - {data['price']} Ft")


def choose_drink():
    choice = input("Add meg a választott ital számát: ")
    while choice not in drinks:
        print("Érvénytelen választás.")
        choice = input("Add meg a választott ital számát: ")
    
    drink_name = drinks[choice]["name"]
    price = drinks[choice]["price"]
    print(f"{drink_name} választva. Ár: {price} Ft")
    return choice


def pay_drink(choice):
    drink_name = drinks[choice]["name"]
    price = drinks[choice]["price"]

    inserted_money = int(input("Dobd be a pénzt: "))

    if inserted_money < price:
        print("Nincs elég pénzed az italhoz.")
        return
    elif inserted_money > price:
        change = inserted_money - price
        print(f"Itt a {drink_name}, és a visszajáró: {change} Ft.")
    else:
        print(f"Itt a {drink_name}. Köszönjük a vásárlást!")


def vending_machine():
    while True:
        print("Üdvözöl az italautomata!")
        print_drinks()
        choice = choose_drink()
        pay_drink(choice)



vending_machine()
