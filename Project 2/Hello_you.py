# Ask user for name 
name = input("What is your name ?:")
print(name)

#Ask user for age
age = input("How old are you?:")
print(age)

#Ask user for city
city = input("What is your city?:")
print(city)

#Ask user what they enjoy
enjoy = input("What do you enjoy?:")
print(enjoy)

#Create output text

string = "Your name is {} and you are {} years old.	You live in {} and you enjoy {}"
output = string.format(name, age, city, enjoy)

#Print output to screen
print(output)