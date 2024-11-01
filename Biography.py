#Basic
name= "Santino Stanlee Gabriel C. Partosa" #The information that is going to be displayed 
hometown= "Sto. tomas, Davao del Norte" #The information that is going to be displayed 
age= "18" #The information that is going to be displayed 
print(f"{name}\n{hometown}\n{age}") #Print code



#Advance requirements
user_first_name= input("What is your first name? ") #Ask the user for an input so that the information that is going to be displayed 
user_second_name= input("and your second name? ") #Ask the user for an input so that the information that is going to be displayed 
user_hometown_name= input("Where is your hometown? ") #Ask the user for an input so that the information that is going to be displayed 
user_age= input("And how old are you? ") #Ask the user for an input so that the information that is going to be displayed
print(f"Well hello there {user_first_name} {user_second_name}\nI see you live in {user_hometown_name}\nYou are {user_age} years old") #Print Code



#Enhanced and revised 
name = input("Enter your first name: ") #Ask the user for an input 
name2 = input("Enter your second name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")
# Store information in a dictionary
person_info = {
        "name": name,
        "second name": name2,
        "hometown": hometown,
        "age": age}
print(f"Hello {person_info['name']} {person_info['second name']}\nI see your live in {person_info['hometown']}\nAnd you are {person_info['age']}\nNice to meet you") #Print Code 
