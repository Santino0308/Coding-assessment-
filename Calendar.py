months_days = {1: 31, 2: 29, 3: 31, 4: 30,
               5: 31, 6: 30, 7: 31, 8: 31,
               9: 30, 10: 31, 11: 30, 12: 31} #The calendar Dictionary as the month on the left and the days on the right 

month = int(input("Enter the month number (1-12): ")) #This ensures the user will input a valid month
if month < 1 or month > 12:
    print("Invalid input! Please enter a number between 1 and 12.")

else: #This checks if the user inputed 2 (Which is febraury) to see if its a leap year or not
    if month == 2:
        leap_year = input("Is it a leap year? (Y/N): ").strip().lower()
        days_in_month = 29 if leap_year == "y" else 28
    else:
        days_in_month = months_days[month]

    print(f"The numbered month {month} has {days_in_month} days.") #This code will print out the results
