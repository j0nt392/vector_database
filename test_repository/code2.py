import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please try again.")

play_game()