#include <stdio.h>

typedef struct {
    char name[20];
    int price;
} Drink;

Drink drinks[] = {
    {"Kávé", 250},
    {"Tea", 200},
    {"Forró csoki", 300},
    {"Víz", 150}
};

void print_drinks() {
    printf("Válassz egy italt:\n");
    for (int i = 0; i < 4; i++) {
        printf("%d: %s - %d Ft\n", i + 1, drinks[i].name, drinks[i].price);
    }
}   

int choose_drink() {
    int choice;
    printf("Add meg a választott ital számát: ");
    scanf("%d", &choice);

    while (choice < 1 || choice > 4) {
        printf("Érvénytelen választás.\n");
        printf("Add meg a választott ital számát: ");
        scanf("%d", &choice);
    }
    return choice;           
}

void pay_drink(int choice) {
    int price = drinks[choice - 1].price;
    char *drink_name = drinks[choice - 1].name;
    int inserted_money;

    printf("%s választva. Ár: %d Ft\n", drink_name, price);
    printf("Dobd be a pénzt: ");
    scanf("%d", &inserted_money);

    if (inserted_money < price) {
        printf("Nincs elég pénzed az italhoz.\n");
    } else if (inserted_money > price) {
        printf("Itt a %s, és a visszajáró: %d Ft.\n", drink_name, inserted_money - price);
    } else {
        printf("Itt a %s. Köszönjük a vásárlást!\n", drink_name);
    }	
}
    
void vending_machine() {
    while (1) {
        printf("Üdvözöl az italautomata!\n");
        print_drinks();
        int choice;
        choice = choose_drink();
        pay_drink(choice);
    }
}

int main() {
    vending_machine();
    return 0;
}  
                        
