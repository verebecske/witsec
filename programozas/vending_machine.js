const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const drinks = {
    1: { name: "Kávé", price: 250 },
    2: { name: "Tea", price: 200 },
    3: { name: "Forró csoki", price: 300 },
    4: { name: "Víz", price: 150 }
};

function printDrinks() {
    console.log("Válassz egy italt:");
    for (const [key, drink] of Object.entries(drinks)) {
        console.log(`${key}: ${drink.name} - ${drink.price} Ft`);
    }
}

function askQuestion(question) {
    return new Promise((resolve) => {
        rl.question(question, (answer) => resolve(answer));
    });
}

async function chooseDrink() {
    while (true) {
        const choice = await askQuestion("Add meg a választott ital számát: ");
        if (drinks[choice]) {
            return choice;
        } else {
            console.log("Érvénytelen választás.");
        }
    }
}

async function payDrink(choice) {
    const { name, price } = drinks[choice];
    console.log(`${name} választva. Ár: ${price} Ft`);
    
    const insertedMoney = parseInt(await askQuestion("Dobd be a pénzt: "), 10);
    
    if (insertedMoney < price) {
        console.log("Nincs elég pénzed az italhoz.");
    } else if (insertedMoney > price) {
        console.log(`Itt a ${name}, és a visszajáró: ${insertedMoney - price} Ft.`);
    } else {
        console.log(`Itt a ${name}. Köszönjük a vásárlást!`);
    }
}

async function vendingMachine() {
    while (true) {
        console.log("Üdvözöl az italautomata!");
        printDrinks();
        const choice = await chooseDrink();
        await payDrink(choice);
    }
}

vendingMachine();
