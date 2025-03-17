# 1. Mit csinál a következő program?
```
use std::io;

fn main() {
    println!("Enter a number: ");
    let mut number = String::new();

    io::stdin()
        .read_line(&mut number)
        .expect("Incorrect input!");

    let number: u32 = number
        .trim()
        .parse()
        .expect("Please enter a number!");

    println!();
    fizzbuzz(number);
}

fn fizzbuzz(n: u32) {
    for x in 1..n+1 {
        if x % 3 != 0 && x % 5 != 0 {
            println!("{}", x);
        } else if x % 3 == 0 && x % 5 == 0 {
            println!("FizzBuzz");
        } else if x % 3 == 0 {
            println!("Fizz");
        } else if x % 5 == 0 {
            println!("Buzz");
        }
    }
}
```
# 2. Mi a hiba a következő program esetén?
```
users = [
    {"name": "Freddy Krueger", "movie": "A Nightmare on Elm Street", "year": 1984},
    {"name": "Jason Voorhees", "movie": "Friday the 13th", "year": 1980},
    {"name": "Michael Myers", "movie": "Halloween", "year": 1978},
    {"name": "Pennywise", "movie": "It", "year": 2017},
    {"name": "John Kramer", "movie": "Saw", "year": 2004},
]

for user in users: 
    name = user["name"]
    favorite_movie = user["favorite_movie"]
    print(f"{name}'s favorite movie {favorite_movie}.")

```