password = "12345" #The password variable
max_attempts = 5 #How many attempts is allowed
attempts = 0 #The number of attempt that will slowly rise to 5 and will stop the code

while attempts < max_attempts: #A loop that will keep asking for the user to input the right password
    user_input = input("Please enter the password: ") #Asks the user for an input
    
    if user_input == password: #The input will match the user then it will grant access
        print("Access granted! Welcome!")
        break #And this will stop the loop
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Too many incorrect attempts. The authorities have been notified.")