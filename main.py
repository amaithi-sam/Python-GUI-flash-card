from tkinter import*
import pandas as pd
from random import randint, choice
#DataFrame ------------------
try:
    word_csv = pd.read_csv("data/words_to_learn.csv")
except:
    word_csv = pd.read_csv("data/french_words.csv")


data = word_csv.to_dict(orient="records")
current_card = {}

#-------function button------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    canvas.itemconfig(back_image, image=card_back)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(back_image, image=card_front)

def is_known():
    data.remove(current_card)
    next_card()
    to_learn = pd.DataFrame(data)
    print(len(to_learn))
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#-----------------UI----------Design
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card")
window.config(height=50, width=50, padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right_ = PhotoImage(file="images/right.png")
wrong_ = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = canvas.create_image(400, 270, image=card_back)
canvas.grid(column=0, columnspan=2, row=0, rowspan=1)

language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

known_button = Button(image=right_, command=is_known, highlightthickness=0).grid(column=1, row=1)
unknown_button = Button(image=wrong_, command=next_card, highlightthickness=0).grid(column=0, row=1)

next_card()


window.mainloop()