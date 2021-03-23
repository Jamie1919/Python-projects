# get user email address 

email = input("What is your email address?:").strip()

#slice user name 

user = email[:email.index("@")]

#slice domain name 

domain = email[email.index("a") + 1 :]

#format message 

output = "Your username is {} and your domain name is {}".format(user,domain)

#display output message 

print(output)