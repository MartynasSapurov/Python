import json

my_dictionary = {123454: ("John", 25), 123455: ("Peter", 35),
                 123456: ("Joan", 19), 123457: ("Elizabeth", 28),
                 123458: ("Albert", 22), 123459: ("Glen", 45)}

with open('Homework_16.txt', 'w') as f:
    json.dump(my_dictionary, f)

