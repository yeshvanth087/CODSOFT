import random

# Possible choices
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Instructions:")
print("Type rock, paper, or scissors to play")
print("--------------------------------------")

while True:
    # User input
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"👤 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win!")
        user_score += 1
    else:
        print("😢 You lose!")
        computer_score += 1

    # Display scores
    print(f"📊 Score → You: {user_score} | Computer: {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break
