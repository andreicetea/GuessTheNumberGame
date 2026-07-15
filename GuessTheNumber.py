# A simple guess the number game made as my first small Python project 
# Using pyinstaller to convert this into a .exe file
# with the following command in Powershell: 
# python -m PyInstaller --onefile GuessTheNumber.py
# Some of the code was assisted by Gemini 3, but selfwritten to the best of my abilities
# as to improve my own learning

import random

print("\n                  |---------------------------------------|", 
      "\n                  |  Welcome to the Pythonian dimension!  |", 
      "\n                  |---------------------------------------|\n\n")

def play_game():

    while True:
        difficulty = input(" Type your desired difficulty below:\n Easy - Medium - Hard: ").strip().lower()

        if difficulty == "easy": 
            a, b = 1, 15
            print("\nYou have chosen the path of the weak, as you wish!") 
            break    
        elif difficulty == "medium": 
            a, b = 1, 30
            print("\nDon't expect this to be a breeze...") 
            break
        elif difficulty == "hard": 
            a, b = 1, 75
            print("\nYou have chosen to enter into Pythonian Mordor, \nwhere few beings come out whole again!")
            break
        else:
            print("\n❌ Invalid choice! Please type Easy, Medium, or Hard (no case sensitivity).\n")
    
    secret_number = random.randint(a, b)
    wins = 0 
    losses = 0
    attempts = 0
    prompt = f"I'm thinking of a number between {a} and {b}. Can you guesss it? "
    while True:
        try:
            guess = int(input(prompt)) 
        except ValueError: 
            prompt = "That's not a number! Try again: "
            continue
        
        attempts += 1  

        if guess < secret_number and attempts < 5:       
            prompt = f"Too low! You have {5 - attempts} attempts left: "
        elif guess > secret_number and attempts < 5:
            prompt = f"Too high! You have {5 - attempts} attempts left: "
        elif guess != secret_number and attempts == 5:
            print(f"You lose! The number was {secret_number}")
            return "loss"
        else:
            print(f"🎯 You win! You found {secret_number} in \n", 
            f"{attempts} tries!")
            return "win"
                  
def guess_the_number_game(): 
    wins = 0
    losses = 0
    while True: 
        result = play_game()
        if result == "win": 
            wins += 1 
        elif result == "loss": 
            losses += 1
        
        play_again = input("Play again? (y/n): ")
        if play_again != "y":
            exit = input(f"\nYou have given up already! I wouldn't expect any different from a mere earthling...\n" +
                         "Below is your less than impressive score! Press enter to be teleported back\n" +
                         f"\nWins: {wins}\nLosses: {losses} \n\n")
            break
            
guess_the_number_game()