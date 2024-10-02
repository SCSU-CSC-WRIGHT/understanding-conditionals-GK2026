## Simple Calculator
#Write a program that asks the user for two numbers and an arithmetic operator (+, -, *, /). Use if statements to perform the corresponding arithmetic operation and print the result.
num=float(input("Enter a number: ")) #Gets the numbers and operation from the user
num2=float(input("Enter another number "))
operation=input("Enter a arithmetic operator (+, -, *, /)")

if(operation=='+'): #Checks the operation aginst what the user entered and prints the answer 
    print(num+num2)
elif(operation=='-'):
    print(num-num2)
elif(operation=='*'):
    print(num*num2)
elif(operation=='/'):
    print(num/num2)