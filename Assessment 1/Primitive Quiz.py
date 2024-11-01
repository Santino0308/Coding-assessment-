#Basic
while True:
    answer = input("What is the capital of France? ")  
    if answer.strip().lower() == "paris":  #will accept if the case is big or small
        print("That is correct!!!! Good job")
        break
    else:
        print("WRONG, Try again:>")
#Advance Requirments 
while True: #Quiz introduction 
    ready_or_not = input("Are you ready for a quiz about the capitals of 10 European countries?\nAre you up for it? 'yes or no': ")
    if ready_or_not.strip().lower() == "yes":
        print("Well then, let's begin:>>")
        break
    elif ready_or_not.strip().lower() == "no":
        print("Okay then, Goodbye!!!!")
        exit() 
    else:
        print("Please answer with 'yes' or 'no'.")
        continue
while True: #Quiz starts here
    answer1 = input("What is the capital of France? ")
    if answer1.strip().lower() == "paris":  #will accept if the case is big or small
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer2 = input("What is the capital of Germany? ")
    if answer2.strip().lower() == "berlin":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer3 = input("What is the capital of Italy? ")
    if answer3.strip().lower() == "rome":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer4 = input("What is the capital of Spain? ")
    if answer4.strip().lower() == "madrid":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer5 = input("What is the capital of Portugal? ")
    if answer5.strip().lower() == "lisbon":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer6 = input("What is the capital of Netherlands? ")
    if answer6.strip().lower() == "amsterdam":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer7 = input("What is the capital of Belgium? ")
    if answer7.strip().lower() == "brussels":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer8 = input("What is the capital of Austria? ")
    if answer8.strip().lower() == "vienna":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer9 = input("What is the capital of Sweden? ")
    if answer9.strip().lower() == "stockholm":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
while True:
    answer10 = input("What is the capital of Norway? ")
    if answer10.strip().lower() == "oslo":  
        print("Correct!!!!")
        break
    else:
        print("Oops, that is wrong!!!! Try again")
#End of the quiz
while True:
    answer11= input("Did you have fun with out quiz?\n'Yes or no'?")
    if answer11.strip().lower() == "yes":
        print("Thank you for participating!! I worked hard on this:>>>>")
        break
    elif answer11.strip().lower() == "no":
        print("Thank you for participating still, im sorry if for wasting your time:<")
        break
    else:
        print("Please give me a yes or no answer!!!!!!")