movie = {
    "Batman": [18, 5],
    "Sonic": [10, 5],
    "Fantastic Beast": [18, 5],
    "Morbius": [20, 5]

}
while True:
    # enter movie name
    choice = input("Which movie would you like to watch?:").strip().title()
    if choice in movie:
        age = int(input("How old are you?:").strip())
        # check user age
        if age >= movie[choice][0]:
            # check enough seats
            num_seats = movie[choice][1]
            if num_seats > 0:
                print("Enjoy the movie")
                movie[choice][1] = movie[choice][1] - 1
            else:
                print("Sorry, we are sold out")
        else:
            print("You are too young to watch the movie!")
        pass
    else:
        print("We dont have this movie...")