import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#BASED ON RULES: Rock beats scissors, scissors beat paper, and paper beats rock
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice]) #Images printed based upon user choice

computer_choice = random.randint(0, 2) #Computer chooses randomly from 0,1 or 2
print("Computer chose:")
print(game_images[computer_choice])#Images printed based upon computer choice

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2: #Rock beats scissors
  print("You win!")
elif computer_choice == 0 and user_choice == 2:#Rock beats scissors
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

print("Do you want to play again?")
#if user input n or N then condition is True
ans = input("Enter Y or N as your input: \n")
if  ans == "N":
    print("Thanks for playing!")# we print thanks for playing
else:
    print("Restart the game!")
