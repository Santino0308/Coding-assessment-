#Basic
name= "Santino Stanlee Gabriel C. Partosa"
hometown= "Sto. tomas, Davao del Norte"
age= "18"
print(f"{name}\n{hometown}\n{age}")



#Advance requirements
user_first_name= input("What is your first name? ")
user_second_name= input("and your second name? ")
user_hometown_name= input("Where is your hometown? ")
user_age= input("And how old are you? ")
print(f"Well hello there {user_first_name} {user_second_name}\nI see you live in {user_hometown_name}\nYou are {user_age} years old")



#Enhanced and revised 
name = input("Enter your first name: ")
name2 = input("Enter your second name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")
# Store information in a dictionary
person_info = {
        "name": name,
        "second name": name2,
        "hometown": hometown,
        "age": age}
print(f"Hello {person_info['name']} {person_info['second name']}\nI see your live in {person_info['hometown']}\nAnd you are {person_info['age']}\nNice to meet you")
