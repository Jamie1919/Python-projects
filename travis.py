known_users = ["Bob", "Greg", "Steve", "Rick" , "Morty", "Price", "Soap"]

while True:
	print("Hi! My name is Rick")
	name = input("What is your name?:").strip().capitalize()

	if name in known_users:
		print("Hello {}!".format(name))
		remove = input("Would you like to be removed from the system(y/n)?:").strp().lower()

		if remove =="y":
			 known_users.remove(name)
		elif remove == "n":
			print("No problem you can stay")
			

	else:
		print("Sorry I dont think I have met you yet {} ".format(name))
		add_me = input("Would you like to be added (y/n)?:").strip().lower()
		if add_me =="y":
			known_users.append(name)
		elif add_me == "n":
			print("No problem see you later")
		

