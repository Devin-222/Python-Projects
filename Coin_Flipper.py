import tkinter as tk
import random

def animate_flip(count=10):
    if count > 0:
        temp_result = random.choice(["Heads", "Tails"])
        result_label.config(text=temp_result)
        window.after(100, animate_flip, count - 1)
    else:
        final_result = random.choice(["Heads", "Tails"])
        result_label.config(text=final_result)

# GUI setup
window = tk.Tk()
window.title("Coin Flip")
window.geometry("300x200")

title_label = tk.Label(window, text="Flip the Coin!", font=("Arial", 18))
title_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 24), fg="blue")
result_label.pack(pady=20)

flip_button = tk.Button(window, text="Flip", font=("Arial", 14), command=animate_flip)
flip_button.pack()

window.mainloop()
