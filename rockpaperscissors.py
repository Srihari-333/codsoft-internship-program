import random

def get_user_choice():
    """Prompt user to enter their choice (rock, paper, or scissors)."""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter either rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").strip().lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")

    user_score = 0
    computer_score = 0

    while True:
        print("\n")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
