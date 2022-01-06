import tkinter as tk
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

#load word list with panda as CSV file
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
column_1 = data.columns[0]
column_2 = data.columns[1]
list_words = data.to_dict(orient="records")
random_word = random.choice(list_words)
def correct():
    list_words.remove(random_word)
    new_data = pandas.DataFrame.from_dict(list_words)
    new_data.to_csv("data/to_learn.csv", index=False)
    if len(list_words) == 0:
        canvas.itemconfig(word, text="You Finished!!")
        window.after_cancel(flip)
    else:
        get_new()


def get_new():
    global flip
    global random_word
    random_word = random.choice(list_words)
    canvas.itemconfig(word, text=random_word[column_1])
    canvas.itemconfig(front, image=card_front)
    canvas.itemconfig(column_first, text=column_1)
    flip = window.after(3000, flip_card)

def flip_card():
    # back of card
    card_back = tk.PhotoImage(file="images/card_back.png")
    canvas.itemconfig(front ,image=card_back)
    canvas.itemconfig(column_first, text= column_2)
    canvas.itemconfig(word, text=random_word[column_2] )



window = tk.Tk()
window.title("Flash Card Quiz")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flip = window.after(3000, flip_card)

#front of card
card_front = tk.PhotoImage(file="images/card_front.png")
front = canvas.create_image(400, 263, image=card_front)
column_first = canvas.create_text(400, 150, text= column_1, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text = random_word[column_1] , font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(column=1,row=1)
wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=get_new)
wrong_button.grid(column=0, row=1)
window.mainloop()
