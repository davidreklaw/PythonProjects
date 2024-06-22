import random as rd

YES = ["Yes", "yes", "YES", "y", "Y"]
NO = ["No", "no", "NO", "n", "N"]

restaurants = {
    "Mexican": ["Taco Bell", "La Hacienda", "Azul Tequila", "El Ranchero", "Senor Taco", "Twisted Taco"],
    "Burgers": ["Five Guys", "Burger King", "Stake n' Shake", "Wendy's", "Culver's", "Freddy's", "Red Robin", "Sonic"],
    "Breakfast": ["IHOP", "Waffle House", "Mimi's"],
    "Chicken": ["Chick-fil-A", "Popeye's", "Zaxby's", "Buffalo Wild Wings"],
    "Pizza": ["Papa Johns", "Dominos", "Your Pie", "Partners", "Pizza Hut"],
    "Burritos": ["Willie's", "Chipotle", "Qdoba", "Moe's"],
    "Sandwiches": ["Subway", "Pub Subs", "Jersey Mike's", "Firehouse"],
    "Steakhouse": ["Long Horns", "Texas Roadhouse"],
    "Misc": ["Cracker Barrel", "Clubhouse", "Asian Cook", "Panda", "Chilli's", "Broadway", "O'Charley's", "Panera", "Arby's"],
    "Italian": ["Olive Garden", "Italian Oven"]
}

ok = NO
pickedCategories = []
pickedResturants = []

while (ok == NO):
    category = rd.choice(list(restaurants.keys()))

    while category in pickedCategories:
        category = rd.choice(list(restaurants.keys()))

    pickedCategories.append(category)

    answer = input("Is {} ok? ".format(category))

    if answer in YES:
        ok = NO
        while (ok == NO):

            dinner = rd.choice(list(restaurants[category]))
            while dinner in pickedResturants:
                dinner = rd.choice(list(restaurants[category]))
            pickedResturants.append(dinner)

            answer = input("Is {} ok? ".format(dinner))

            if answer in YES:
                break
            else:
                if len(pickedResturants) == len(restaurants[category]):
                    print("Then Stay Home!")
        break
    else:
        if len(pickedCategories) == len(list(restaurants.keys())):
            print("Then stay home!")
            break
        
        