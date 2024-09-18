# Adding funcion: this function adds two numbers and returns the result
def adding(x, y):
  return x + y

# Subtraction function: this function subtracts one number from another number and returns the result
def subtraction(x, y):
  return x - y

# Multiplication function: This function multiply two numbers and returns the result
def multiplication(x, y):
  return x * y

# Division function: This function divide one numbers by another number and returns the result, with error handling when division by zero
def division(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    return "Can not divide by zero! Please change the value of right operand."

  return result

# Modulus function: This function returns the modulus after doing the division of two numbers, with error handling when division by zero.
def modulus(x, y):
  try:
    reminder = x % y
  except ZeroDivisionError:
    return "Can not divide by zero! Please change the value of right operand."
  
  return reminder

# Function takes input from the users to make choice of one of the oparations and returns choice. With exception handling.
def user_choice():
  while True:
    try:
      choice = int(input("Enter choice (1/2/3/4/5): "))
      if choice in [1, 2, 3, 4, 5]:
        return choice
      else:
        print("Invalid Input: Choose between 1 to 5")

    except ValueError:
      print("Enter a valid and number!")
  
# Function takes user's input and returns the value by converting to float. With valueError exception.
def user_input_number(sms):
  while True:
    try:
      return float(input(sms))
    except ValueError:
      print("Enter a valid and real number.")


""" 
Calculation function:
1. Takes input as user's choice of which function among the five that the usres want to perform.
2. Then takes input of two numbers.
3. Then perform the chosen function.
4. And return the expected result.
"""
def calculation():
  while True:
    print("Select operation: \n1. Adding \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus")

    # Call the choice functtion and store the result in a variable, choice.
    choice = user_choice()

    # Call the user_input_number function to get two numbers from user and store in separate two variables.
    firstNumber =  user_input_number("Enter first number: ")
    secondNumber =  user_input_number("Enter second number: ")

    # The conditional statement depends on the choosen oparations option 1 to 5 and display the results.
    if choice == 1:
      print(f"Adding: {firstNumber} + {secondNumber} = {adding(firstNumber, secondNumber)}")
    
    elif choice == 2:
      print(f"Subtraction: {firstNumber} - {secondNumber} = {subtraction(firstNumber, secondNumber)}")
    
    elif choice == 3:
      print(f"Multiplication: {firstNumber} x {secondNumber} = {multiplication(firstNumber, secondNumber)}")
    
    elif choice == 4:
      print(f"Division: {firstNumber} / {secondNumber} = {division(firstNumber, secondNumber)}")
    
    elif choice == 5:
      print(f"Modulus: {firstNumber} % {secondNumber} = {modulus(firstNumber, secondNumber)}")
    
    # Additional features, to ask the user if the program will continue the calculation process.
    more_calculation = input("Do you want to calculate more? (Yes/No): ").lower()
    if more_calculation != "yes" and more_calculation != 'y':
      break


# Call the calculation function
if __name__ == "__main__":
  calculation()