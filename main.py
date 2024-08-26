from tkinter import *
from playsound import playsound
playsound('/Users/clementducharne/Desktop/The Duck Song.mp3',False)




#List of Questions, Answers, Categories, and Point Values

questions = [{"name": "q11", "category": "Popularity", "question": "What is the most popular duck in the US?",
                  "answer": "what is the mallard", "value": 100},
                 {"name": "q12", "category": "Popularity",
                  "question": "Which country has the largest duck population in the world?", "answer": "what is china",
                  "value": 200},
                 {"name": "q13", "category": "Popularity",
                  "question": "Which dish from Beijing uses duck as its centerpiece?", "answer": "what is peking duck",
                  "value": 300},
                 {"name": "q14", "category": "Popularity",
                  "question": "What duck-centric dish has been banned in multple countries due to questionable ethics?",
                  "answer": "what is foie gras", "value": 400},
                 {"name": "q15", "category": "Popularity", "question": "What is the scientific name for a duck?",
                  "answer": "what is anas platyrhynchos", "value": 500},
                 {"name": "q21", "category": "Size", "question": "What is the smallest type of duck?",
                  "answer": "what are perching ducks", "value": 100},
                 {"name": "q22", "category": "Size", "question": "What is the biggest duck in the world",
                  "answer": "what is the muscovy duck", "value": 200},
                 {"name": "q23", "category": "Size", "question": "Which duck has the biggest beak?", "answer": "what is the crested duck", "value": 300},
                 {"name": "q24", "category": "Size", "question": "Which duck has the biggest wingspan?", "answer": "what is the cayuga", "value": 400},
                 {"name": "q25", "category": "Size", "question": "Which duck has the smallest winspan?", "answer": "what is the bufflehead duck", "value": 500},
                 {"name": "q31", "category": "Wildcard", "question": "What was the duck looking for in the duck song?",
                  "answer": "what are grapes", "value": 100},
                 {"name": "q32", "category": "Wildcard", "question": "What is a female duck called?",
                  "answer": "what is a hen", "value": 200},
                 {"name": "q33", "category": "Wildcard", "question": "What is a duck's favorite color?", "answer": "what is the color green", "value": 300},
                 {"name": "q34", "category": "Wildcard", "question": "What is the most common name for a duck?", "answer": "who is aflac", "value": 400},
                 {"name": "q35", "category": "Wildcard", "question": "What color are duck eggs?", "answer": "what is pale green", "value": 500}]

# Initiating Defaults

score = 0
COLOR = "#063970"
counter = 0

# Open a Window once a button is clicked

def open_new_window(qname):
    global questions
    global score
    global counter
    cat = questions[qname]["category"]
    currentQ = questions[qname]["question"]
    currentA = questions[qname]["answer"]
    points = questions[qname]["value"]

    def is_answer_correct():
        global score
        global score_label
        user_answer = website_entry.get()
        if user_answer.lower() == currentA:
            score += points
            score_label.config(text = f"x {score}")
            print("Correct!")
            print(score)
        else:
            print("Incorrect.")
        question_window.destroy()
        if counter == 15:
            end_window = Tk()
            end_window.config(padx=25, pady=25, bg=COLOR)
            end_window.title("Game Over")
            window.destroy()
            msg = Label(end_window, text=f"You Have Completed the Game!\nYou collected {score} ducks!",
                        font=("Arial", 24, "bold"), pady=3, bg=COLOR)
            msg.grid(column=0, row=0)



    question_window = Toplevel(window)
    question_window['background'] = COLOR
    question_window.title(f"{cat}")
    question_window.config(padx=25, pady=25)

    question_label = Label(question_window, text=f"Question: {currentQ}", font=("Arial", 16, "bold"), pady=25, padx=5, bg=COLOR)
    question_label.grid(column=0, row=0)

    enter_button = Button(question_window, text="Enter", width=13, font=("Arial", 12, "bold"), command=is_answer_correct, fg="gray", pady=10, bd=20,
                       highlightbackground=COLOR)
    enter_button.grid(column=0, row=2)
    website_entry = Entry(question_window, width=21)
    website_entry.focus()
    website_entry.grid(column=0, row=1)

    if qname == 0:
        q1_button["state"] = DISABLED
        counter+=1
    if qname == 1:
        q2_button["state"] = DISABLED
        counter += 1
    if qname == 2:
        q3_button["state"] = DISABLED
        counter += 1
    if qname == 3:
        q4_button["state"] = DISABLED
        counter += 1
    if qname == 4:
        q5_button["state"] = DISABLED
        counter += 1
    if qname == 5:
        q6_button["state"] = DISABLED
        counter += 1
    if qname == 6:
        q7_button["state"] = DISABLED
        counter += 1
    if qname == 7:
        q8_button["state"] = DISABLED
        counter += 1
    if qname == 8:
        q9_button["state"] = DISABLED
        counter += 1
    if qname == 9:
        q10_button["state"] = DISABLED
        counter += 1
    if qname == 10:
        q11_button["state"] = DISABLED
        counter += 1
    if qname == 11:
        q12_button["state"] = DISABLED
        counter += 1
    if qname == 12:
        q13_button["state"] = DISABLED
        counter += 1
    if qname == 13:
        q14_button["state"] = DISABLED
        counter += 1
    if qname == 14:
        q15_button["state"] = DISABLED
        counter += 1



    question_window.mainloop()

# window
window = Tk()
window['background'] = COLOR
window.title("Duck Jeopardy")
window.config(padx=25, pady=25)

# Canvas
canvas = Canvas(width=50, height=50, bg=COLOR, highlightbackground=COLOR)
logo = PhotoImage(file="/Users/clementducharne/Desktop/rubber-ducky-clip-art-rubber-duck-115635289485obpxrdkah.png")
canvas.create_image(30, 30, image=logo)
canvas.grid(column=0, row=0)

canvas = Canvas(width=800, height=200, bg=COLOR, highlightbackground=COLOR)
title = PhotoImage(file="/Users/clementducharne/Desktop/cooltext427427556210949 (1).png")
canvas.create_image(400, 100, image=title)
canvas.grid(column=2, row=1, columnspan=3)

# Labels
popularity_label = Label(text="Popularity", font=("Arial", 24, "bold"), pady=3, bg=COLOR)
popularity_label.grid(column=2, row=2)

wild_card_label = Label(text="Wild Card", font=("Arial", 24, "bold"), pady=3, bg=COLOR)
wild_card_label.grid(column=4, row=2)

size_label = Label(text="Size", font=("Arial", 24, "bold"), pady=3, bg=COLOR)
size_label.grid(column=3, row=2)

score_label = Label(text=f"x {score}", font=("Arial", 24, "bold"), pady=3, bg=COLOR)
score_label.grid(column=1, row=0)

# Buttons

q1_button = Button(text="100", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(0), fg="black", pady=10, bd=0, highlightbackground="white")
q1_button.grid(column=2, row=3)

q2_button = Button(text="200", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(1), fg="black", pady=10, bd=0, highlightbackground="white")
q2_button.grid(column=2, row=4)

q3_button = Button(text="300", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(2), fg="black", pady=10, bd=0, highlightbackground="white")
q3_button.grid(column=2, row=5)

q4_button = Button(text="400", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(3), fg="black", pady=10, bd=0, highlightbackground="white")
q4_button.grid(column=2, row=6)

q5_button = Button(text="500", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(4), fg="black", pady=10, bd=0, highlightbackground="white")
q5_button.grid(column=2, row=7)

q6_button = Button(text="100", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(5), fg="black", pady=10, bd=0, highlightbackground="white")
q6_button.grid(column=3, row=3)

q7_button = Button(text="200", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(6), fg="black", pady=10, bd=0, highlightbackground="white")
q7_button.grid(column=3, row=4)

q8_button = Button(text="300", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(7), fg="black", pady=10, bd=0, highlightbackground="white")
q8_button.grid(column=3, row=5)

q9_button = Button(text="400", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(8), fg="black", pady=10, bd=0, highlightbackground="white")
q9_button.grid(column=3, row=6)

q10_button = Button(text="500", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(9), fg="black", pady=10, bd=0, highlightbackground="white")
q10_button.grid(column=3, row=7)

q11_button = Button(text="100", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(10), fg="black", pady=10, bd=0, highlightbackground="white")
q11_button.grid(column=4, row=3)

q12_button = Button(text="200", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(11), fg="black", pady=10, bd=0, highlightbackground="white")
q12_button.grid(column=4, row=4)

q13_button = Button(text="300", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(12), fg="black", pady=10, bd=0, highlightbackground="white")
q13_button.grid(column=4, row=5)

q14_button = Button(text="400", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(13), fg="black", pady=10, bd=0, highlightbackground="white")
q14_button.grid(column=4, row=6)

q15_button = Button(text="500", width=13, font=("Arial", 24, "bold"), command=lambda: open_new_window(14), fg="black", pady=10, bd=0, highlightbackground="white")
q15_button.grid(column=4, row=7)

window.mainloop()
