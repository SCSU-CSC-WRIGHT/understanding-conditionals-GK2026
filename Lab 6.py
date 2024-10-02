## Day of the Week
#Create a program that asks the user to input a number between 1 and 7. Use an if statement to print the day of the week (e.g., 1 = Monday, 2 = Tuesday, etc.).

day_week=int(input("Enter a number between 1 and 7: "))#Gets the input from the user

if(day_week==1): #Checks the user number and prints the coresponding day of the week
    print("It is Monday")
elif(day_week==2):
    print("It is Tuesday")
elif(day_week==3):
    print("It is Wesnday")
elif(day_week==4):
    print("It is Thursday")
elif(day_week==5):
    print("It is Friday")
elif(day_week==6):
    print("It is Saturday")
elif(day_week==7):
    print("It is Sunday")
else:
    print("Error")#Prints an error if the number the user entered is too big or small 






