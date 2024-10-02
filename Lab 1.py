## Temperature Check
#Write a Python program that asks the user to input the current temperature in Celsius. If the temperature is above 30 degrees, print "It's a hot day." Otherwise, print "The weather is cool."
temp=float(input("Enter temperature outside in Celsius: "))#Gets input from the user
if(temp>30): ## Compares the input to 30
    print("It's a hot day") #If the temp is greater than 30 it prints It's a hot day
else:
    print("The weather is cool.") # If hte temp is below 30 it prints The weather is cool 