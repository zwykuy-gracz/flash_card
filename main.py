from tkinter import *
import random, pandas

BACKGROUND_COLOR = '#B1DDC6'
WHITE = '#FFFFFF'
FONT_NAME = 'Ariel'
FONT_STYLE = 'italic'
TIMER = None
random_french_word = {}
to_learn = {}


def next_card():
    global random_french_word, flip_timer
    window.after_cancel(flip_timer)
    random_french_word = random.choice(dict_words)
    canvas.itemconfig(current_word, text=random_french_word['French'], fill='white')
    canvas.itemconfig(current_language, text='French', fill='white')
    canvas.itemconfig(bg_color, image=card_back)
    flip_timer = window.after(3000, flip_card)
    # try:
    #     dict_words.remove(random_french_word)
    # except IndexError:
    #     print('im out')


def right_button_func():
    dict_words.remove(random_french_word)
    df = pandas.DataFrame(dict_words)
    df.to_csv('data/words_to_learn.csv', index=False)
    next_card()

def create_dict_of_words():
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")
        dict_words = original_data.to_dict(orient='records')
    else:
        dict_words = data.to_dict(orient='records')
    # dict_words = {row.French: row.English for index, row in data.iterrows()}
    return dict_words

def flip_card():
    canvas.itemconfig(current_language, text='English', fill=BACKGROUND_COLOR)
    canvas.itemconfig(current_word, text=random_french_word['English'], fill=BACKGROUND_COLOR)
    canvas.itemconfig(bg_color, image=card_front)
    

dict_words = create_dict_of_words()



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
bg_color = canvas.create_image(400, 260, image=card_back)
current_language = canvas.create_text(400, 150, text='', fill='white', font=(FONT_NAME, 40, FONT_STYLE))
current_word = canvas.create_text(400, 263, text='', fill='white', font=(FONT_NAME, 60, 'bold'))
# current_word = Label(text=random_french_word, fg=WHITE, font=(FONT_NAME, 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
# wrong_button = Button(image=wrong_image, command=wrong_button_func)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=right_button_func)
# right_button = Button(image=right_image, command=right_button_func)
right_button.grid(column=1, row=1)


next_card()

window.mainloop()



# def create_french_list():
#     french_data = pandas.read_csv("data/test.csv")
#     french_list = [row.French for index, row in french_data.iterrows()]
#     return french_list

# def wrong_button_func():
#     random_french_word = random.choice(french_list)
#     canvas.itemconfig(current_word, text=random_french_word)

# def right_button_func():
#     random_french_word = random.choice(french_list)
#     canvas.itemconfig(current_word, text=random_french_word)