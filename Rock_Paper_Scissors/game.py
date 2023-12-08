import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    choices = ['rock', 'paper', 'scissors']
    user_score, computer_score = 0, 0

    while True:
        print("\nChoose: rock, paper, or scissors (type 'quit' to exit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"User's choice: {user_choice}")
        print(f"Result: {result}")

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - User: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()