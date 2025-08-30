import tkinter as tk
import random

# Game logic
def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    label_result.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}")

# GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Heading
label_title = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Make your move!", font=("Arial", 12), bg="#f0f0f0")
label_result.pack(pady=20)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_buttons, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_buttons, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.grid(row=0, column=2, padx=5)

# Exit button
btn_exit = tk.Button(root, text="Exit", width=10, command=root.quit, bg="red", fg="white")
btn_exit.pack(pady=15)

root.mainloop()

