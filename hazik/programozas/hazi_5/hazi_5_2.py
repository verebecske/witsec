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