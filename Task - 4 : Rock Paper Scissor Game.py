import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    global user_score, computer_score
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Choose one: rock 🪨, paper 📃, or scissors ✂️")
        
        user_choice = input("Your choice: ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round! 🥳")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round! 🙃")
            computer_score += 1
        else:
            print("It's a tie! 😐")
        
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print("\nGame Over!")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game! 🥳🥳🥳")
    elif user_score < computer_score:
        print("Computer won the game. Better luck next time! 🙃🙃🙃")
    else:
        print("The game is a tie! 😐😐😐")

if __name__ == "__main__":
    play_game()
