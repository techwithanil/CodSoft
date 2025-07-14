import tkinter as tk
from tkinter import messagebox
import random

# Initialize score counters
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Update the result and scores
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0  Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#e6f7ff")

tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 18, "bold"), bg="#e6f7ff").pack(pady=10)
tk.Label(root, text="Choose one:", font=("Arial", 12), bg="#e6f7ff").pack()

# Buttons for user input
btn_frame = tk.Frame(root, bg="#e6f7ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play('rock')).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play('paper')).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play('scissors')).grid(row=0, column=2, padx=10)

# Result and score display
result_label = tk.Label(root, text="Make your move!", font=("Arial", 12), bg="#e6f7ff")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12), bg="#e6f7ff")
score_label.pack(pady=10)

# Reset Button
tk.Button(root, text="Play Again", command=reset_game, bg="#3399ff", fg="white").pack(pady=10)

# Run the application
root.mainloop()
