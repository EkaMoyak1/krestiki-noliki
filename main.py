import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("350x350+500+200")
root["bg"] = '#219EBC'
frame = tk.Frame(root)
frame.pack(padx=10, pady=40)
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return
    buttons[row][col]['fg'] = 'white' if current_player == "X" else '#FB8500'
    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Поздравляем!", f"Игрок {current_player} победил!")
        root.destroy()

    if is_draw():
        messagebox.showinfo("Ничья!", "Игра окончена, ничья!")
        root.destroy()
        return

    current_player = "O" if current_player == "X" else "X"

def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(frame, text="", font=("Arial", 20), bg='#023047', width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

current_player = "X"

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False



root.mainloop()
