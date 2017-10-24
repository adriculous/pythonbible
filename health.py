# health potion (video game) random number generator script thing using the RANDOM module
# check Python docs for the lists of modules to use

import random

health = 50

# easy - 1, normal - 2, difficult - 3

difficulty = 3

# convert result into an integer (int) since division statements will appear with a 'float' data type

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)
