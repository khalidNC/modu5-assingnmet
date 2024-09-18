import random


low_bound = 1
high_bound = 100

# Generate a random number and store in a variable which is our secret number
secret_number = random.randint(low_bound, high_bound)

"""
Function takes input from a player and convert it to integer then check if the number is within the range 
then returns the number else display a alert to enter number with in the range. Also exception error is 
going to be handled for value error. So that if player enter a non-numaric value then the program still run 
and display alert to enter a valid number.
"""
def player_guese():
  while True:
    try:
      guese = int(input("\nEnter your guess: "))
      if high_bound >= guese >= low_bound:
        return guese
      else:
        print("Enter a valid number within the range 1 to 100.")
    except ValueError:
      print("Please enter a valid number.")

"""
Function checks the player's guese and secret number are same or not, according to the conditions
it returns text as 'correct'/'Too high'/'Too low'.
"""
def check_guese(guese, secret_number):
  if guese == secret_number:
    return "Correct"
  elif guese >= secret_number:
    return "Too high!"
  else:
    return "Too low!"

"""
Function tracks the count of attemps and runs a loop to continue to gets the player's input while
the guese in high or low and when the guese is same as the secret number the end the game with a
game ending message.
"""
def play_game():
  print("Welcome to the Number Guessing Game!\nTry to guess the number between 1 and 100.")

  count_attempts = 0

  while True:
    count_attempts += 1
    # Call the player_guese function and store the value in a variable
    guese = player_guese()
    # Call the check_guese function and store the results in a variable
    result = check_guese(guese, secret_number)

    if result == "Correct":
      print(f"Congratulations! You've guessed the number in {count_attempts} attempts.\n")
      break
    else:
      print(f"{result}")

if __name__ == "__main__":
  play_game()