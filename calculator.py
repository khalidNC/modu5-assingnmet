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
  except ZeroDivisionError as err:
    return "Can not divide by zero! Please change the value of right operand."
  
  return result

# Modulus function: This function returns the modulus after doing the division of two numbers, with error handling when division by zero.
def modulus(x, y):
  try:
    reminder = x % y
  except ZeroDivisionError as err:
    return "Can not divide by zero! Please change the value of right operand."
  
  return reminder

# User's input Function
# def user_input():
#   num1 = input('Enter first number ... ')
#   if num1 
#   # num2 = input('Enter second number ... ')

#   return float(num1)


""" 
Calculation function:
1. Takes input as user's choice of which function among the five that the usres want to perform.
2. Then takes input of two numbers.
3. Then perform the chosen function.
4. And return the expected result.
"""
def calculation():
  print("Select operation: \n1. Adding \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus")

  # Take input from the users to make choice of one of the oparations. And the exception handling.
  try:
    choice = int(input("Choose one of the above options(1/2/3/4/5) ... "))
  except ValueError as err:
    print("Enter a valid number")
    return err

  list_of_choice = [1, 2, 3, 4, 5]

  if choice in list_of_choice:
    firstNumber =  float(input("Enter first number ... "))
    secondNumber =  float(input("Enter sceond number ... "))

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

  else:
    print("Invalid Input: Choose between 1 to 5")


# While loop to have option to run the program till users want.
if __name__ == "__main__":
  while True:
    calculation()
    more_calculation = input("Do you want to calculate more? (yes/no) ... ")
    if more_calculation != "yes" and more_calculation != "y":
      break