names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #List of name

search = input("Enter the name you want to search for: ")#Ask the user for the name to be searched

if search in names: #Searches for the name
    print(f"{search} found in the list.") #This will print if name is found
else:
    print(f"{search} not found in the list.") #This will print if name is not found