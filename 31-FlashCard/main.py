import random
from tkinter import *
from os import path
from pandas import *

#------------------------------------------------------Data-------------------------------------------------------------
dirname = path.dirname(__file__)
try:
    data = read_csv(path.join(dirname,"data/words_to_learn.csv"))
except FileNotFoundError:
    original_data = read_csv(path.join(dirname,"data/french_words.csv"))
    words_dict = original_data.to_dict("records")
else:
    words_dict = data.to_dict("records")



#-----------------------------------------------------FUNCTIONS--------------------------------------------------------

selected_word ={}

def switch_words():

    global selected_word,flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(words_dict)

    canvas.itemconfig(card_header, text="French", fill="black")
    canvas.itemconfig(card_word,text=selected_word["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000, turn_card)


def turn_card():
    canvas.itemconfig(card_header, text="English", fill="white")
    canvas.itemconfig(card_word, text=selected_word["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back)

def save_progress():
    words_to_learn = DataFrame(words_dict)
    words_to_learn.to_csv(path.join(dirname,"data/words_to_learn.csv"),index=False)

def remove_words():
    words_dict.remove(selected_word)
    save_progress()
    switch_words()



#---------------------------------------------------------UI-----------------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, turn_card)



card_front = PhotoImage(file=path.join(dirname,"images/card_front.png"))
card_back = PhotoImage(file=path.join(dirname,"images/card_back.png"))
right_img = PhotoImage(file=path.join(dirname,"images/right.png"))
wrong_img = PhotoImage(file=path.join(dirname,"images/wrong.png"))
canvas = Canvas(width=800, height=525, highlightthickness=0,background=BACKGROUND_COLOR)
card_background = canvas.create_image(0, 0, image=card_front, anchor=NW )
card_header = canvas.create_text(400,150, font=("Arial", 40,"italic"), fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), fill="black")


canvas.grid(row=0, column=0, columnspan=2)

wrong = Button(image=wrong_img, relief="flat", activebackground=BACKGROUND_COLOR, overrelief="flat", cursor="pirate",
               borderwidth=0, highlightthickness=0, command=switch_words)
wrong.grid(row=1, column=0)

right = Button(image=right_img, relief="flat", cursor="cross", borderwidth=0, highlightthickness=0,
               activebackground=BACKGROUND_COLOR,command=remove_words)
right.grid(row=1, column=1)

switch_words()





window.mainloop()