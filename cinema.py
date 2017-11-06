# logic, user input, data structures, dictionaries, etc.

films = {
    "Finding Dory": [3,5],
    "Jason Bourne": [18,5],
    "Tarzan": [15,5],
    "Wonder Woman": [12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age
        
        if age >= films[choice][0]:
            #check enough seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to watch this!")
    else:
        print("We don't have that film...")
