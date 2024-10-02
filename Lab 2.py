#Write a program that asks the user to input two numbers. Use an if condition to print which number is larger or if they are equal.
num1=float(input("Enter a number: ")) #Gets the first number from the user
num2=float(input("Enter a second number: ")) #Gets the second number from the user
if(num1<num2):
    print(num2, "is larger than", num1) #Compares the two number and if num2 is larger prints that num2 is larger than num1
elif(num1>num2):
    print(num1, "is greater than", num2)#Compares the two numbers and if num1 is larger prints that num1 is greater than num2
else:
    print("The numbers are equal")#If non of the above are true than it prints they are equal