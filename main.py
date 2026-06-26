import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Rock Paper Scissors Game")
app.geometry("900x800")
app.resizable(False, False)

# game score
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.configure(text=f"You Chose: {user_choice}")
    computer_choice_label.configure(text=f"Computer Chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win"
        user_score += 1

    else:
        result = "Computer Wins"
        computer_score += 1

    result_label.configure(text=result)

    user_score_label.configure(text=f"Your Score: {user_score}")
    computer_score_label.configure(text=f"Computer Score: {computer_score}")


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_score_label.configure(text="Your Score: 0")
    computer_score_label.configure(text="Computer Score: 0")

    user_choice_label.configure(text="You Chose: -")
    computer_choice_label.configure(text="Computer Chose: -")
    result_label.configure(text="Choose Rock Paper Scissors")


# title of app
title = ctk.CTkLabel(
    app,
    text="Rock Paper Scissors",
    font=("Arial", 32, "bold")
)
title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Play against computer",
    font=("Arial", 16)
)
subtitle.pack()

# score section
score_frame = ctk.CTkFrame(app)
score_frame.pack(pady=25)

user_score_label = ctk.CTkLabel(
    score_frame,
    text="Your Score: 0",
    font=("Arial", 20, "bold")
)
user_score_label.grid(row=0, column=0, padx=40, pady=20)

computer_score_label = ctk.CTkLabel(
    score_frame,
    text="Computer Score: 0",
    font=("Arial", 20, "bold")
)
computer_score_label.grid(row=0, column=1, padx=40, pady=20)

# buttons for game
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=30)

ctk.CTkButton(
    button_frame,
    text="Rock",
    width=180,
    height=50,
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=15, pady=10)

ctk.CTkButton(
    button_frame,
    text="Paper",
    width=180,
    height=50,
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=15, pady=10)

ctk.CTkButton(
    button_frame,
    text="Scissors",
    width=180,
    height=50,
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=15, pady=10)

# result display
user_choice_label = ctk.CTkLabel(
    app,
    text="You Chose: -",
    font=("Arial", 18)
)
user_choice_label.pack(pady=10)

computer_choice_label = ctk.CTkLabel(
    app,
    text="Computer Chose: -",
    font=("Arial", 18)
)
computer_choice_label.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="Start Playing",
    font=("Arial", 24, "bold")
)
result_label.pack(pady=20)

# reset button
ctk.CTkButton(
    app,
    text="Reset Game",
    width=200,
    height=45,
    command=reset_game
).pack(pady=20)

# rules box
rules_frame = ctk.CTkFrame(app)
rules_frame.pack(pady=20)

rules_label = ctk.CTkLabel(
    rules_frame,
    text="Rules\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock",
    font=("Arial", 14)
)
rules_label.pack(padx=20, pady=15)

# footer
footer = ctk.CTkLabel(
    app,
    text="© 2026 Jashanpreet | Rock Paper Scissors Game",
    font=("Arial", 12)
)
footer.pack(side="bottom", pady=15)

app.mainloop()
