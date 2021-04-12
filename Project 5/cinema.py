films= {
"James Bond": [18,5],
"Avengers": [5,5],
"Juistice league": [14,5],
"Pulp fiction": [1,5]	 
}

while True:
	choice = input("What film would you like to watch?").strip().title()
	if choice in films:
		age= int(input("How old are you?:").strip())

		#check user age

		if age >=films[choice][0]:
			#check enough seats

			num_seats = films[choice][1]

			if num_seats > 0:
				print("Enjoy the film")
			films[choice] = films[choice][1] -1
			
		else:
			print("Your are too young too view the film")	
	else:
		print("We dont have that film...")