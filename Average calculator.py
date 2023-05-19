# This program calculates the average of numbers entered by the user.
# User enters numbers until enter -1 to indicate completion. 
# Program calculates and displays the average.

# Descripe the program and give instructions.
print("Welcome to the average calculator.")
print("You can enter several numbers to calculate their average.")
print("When finished, please enter -1.")
print("Please enter only numeric values, otherwise the program will produce an error.")

# Ask the user to enter the first number.
num=(input("\tEnter the first number, please: (-1 to exit): "))
# Assign variables for calculating the average.
sum=0
count=1

# Loop through until the user enters -1 to exit (with input validation).
while num!=-1:
    try:
        num=float(num)      # Convert the input to a float
        sum+=num            # Add the number to the sum
        average=sum/count   # Calculate the average   
        count+=1            # Increase the count
        # Ask the user to enter the next number.
        num=int(input("\tEnter the next number, please: (-1 to exit): ")) 

    except ValueError:      # Handle non-numeric input by the user
        print("Please enter a valid number")
        num=(input("\tEnter a number, please: (-1 to exit): "))
        continue
      
# Display the calculated average to the user with two decimal places.
print("\nThe average of numbers is: {:.2f}".format(average))
print("Thank you for using our program.")