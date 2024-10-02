## Positive, Negative, or Zero
#Write a program that asks the user for a number. Check whether the number is positive, negative, or zero, and print an appropriate message.

num=float(input("Enter a number: "))#Gets the number

if(num<0):#Checks the number and prints a message based on the answer 
    print("Your number is negative")
elif(num>0):
    print("Your number is postive")
else:
    print("Your number is 0")