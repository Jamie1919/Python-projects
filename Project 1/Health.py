import random

health = 10 

difficulty = 1

potion_health = int(random.randint(10,90)/difficulty)

health = health + potion_health
print(health)

