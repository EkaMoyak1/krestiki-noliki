import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("350x400+500+200")
root["bg"] = '#219EBC'

# Счетчики побед
score_X = 0
score_O = 0

# Создание фрейма для игрового поля
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Функция для обновления счета на экране
def update_score():
    score_label.config(text=f"X: {score_X}  |  O: {score_O}")

# Функция для обработки нажатия на кнопку
def on_click(row, col):
    global current_player, score_X, score_O

    if buttons[row][col]['text'] != "":
        return
    buttons[row][col]['fg'] = 'white' if current_player == "X" else '#FB8500'
    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Поздравляем!", f"Игрок {current_player} победил!")
        if current_player == "X":
            score_X += 1
        else:
            score_O += 1
        update_score()
        clear_btn()  # Очистка поля после победы
        return

    if is_draw():
        messagebox.showinfo("Ничья!", "Игра окончена, ничья!")
        clear_btn()  # Очистка поля после ничьи
        return

    current_player = "O" if current_player == "X" else "X"

# Функция для проверки ничьей
def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# Создание игрового поля
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(frame, text="", font=("Arial", 20), bg='#023047', width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

current_player = "X"

# Функция для проверки победителя
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

# Функция для очистки поля
def clear_btn():
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""



# Создание метки для отображения счета
score_label = tk.Label(root, text=f"X: {score_X}  |  O: {score_O}", font=("Arial", 16), bg='#219EBC', fg='white')
score_label.pack(pady=10)

# Кнопка для сброса игры
btn_sbros = tk.Button(root, text="Начать заново", font=("Arial", 12),
                      bg='#023047', fg='white',
                      width=15, height=2, command=clear_btn)
btn_sbros.pack(side="bottom", pady=10)

root.mainloop()