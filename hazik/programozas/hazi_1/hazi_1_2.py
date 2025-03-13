def count_hills(place_names: list):
    hill_count = 0
    for name in place_names:
        if "hill" in name.lower():
            hill_count += 1


def main():
    place_names = [
        "Ditchling Beacon",
        "Crowborough Hill",
        "Black Hill",
        "Firle Beacon",
        "Wilmington Hill",
        "Hindleap Hill",
        "Saxonbury Hill",
        "Willingdon Hill",
        "Newmarket Hill",
        "North's Seat",
        "Cliffe Hill",
    ]
    hill_count = count_hills(place_names)
    if hill_count >= 5:
        print("There are at least 5 hills.")
    else:
        print("There are fewer than 5 hills.")


main()
