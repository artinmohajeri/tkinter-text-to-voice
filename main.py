import pyttsx3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Artin Text To Voice")
win.iconbitmap("./logo.ico")
win.minsize(500,450)
win.config(bg="blue")

gender = IntVar()
gender.set("0")
def click():
    if text.get("1.0", "end-1c") and speed_input.get():
        # Take input from the user

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Change the voice speed (rate)
        engine.setProperty('rate', int(speed_input.get()))  # You can adjust the rate (words per minute) as needed

        # Change the voice gender (0 for male, 1 for female)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[gender.get()].id)  # Change the index to 0 for a male voice

        # Convert the text to speech
        engine.say(text.get("1.0", "end-1c"))

        # Play the converted speech
        engine.runAndWait()
    else:
        messagebox.showerror(title="Error", message="fill out the form completely")

label = Label(win, text="Enter your text:", bg="blue", fg="white", font=("None",15,"bold"))
text = Text(win,font=("None",14), width=40, height=5)
label.pack(pady=(20,0))
text.pack()

speed_label = Label(win, text="speed (wpm):", bg="blue", fg="white", font=("None",12,"bold"))
speed_label.pack(pady=(40,0))
speed_input = ttk.Entry(win, width=10, justify='center', font=("None",12))
speed_input.config(validate="key", validatecommand=(win.register(lambda s: s.isdigit() or s == ""), "%P"))
speed_input.insert(0,130)
speed_input.pack()

gender_label = Label(win, text="Male or Female:", bg="blue", fg="white", font=("None",12,"bold") )
gender_label.pack(pady=(20,0))
gender_frm = Frame(win)
gender_frm.pack()
male = Radiobutton(gender_frm, variable=gender, value="0", text="male", bg="blue", fg="white", font=("None", 14), selectcolor="red", indicatoron=0, activeforeground="red")
female = Radiobutton(gender_frm, variable=gender, value="1", text="female", bg="blue", fg="white", font=("None", 14), selectcolor="red", indicatoron=0, activeforeground="red")
male.grid(row=0, column=0)
female.grid(row=0, column=1)

convert_btn = Button(win, text="Convert", command=click, font=("None",14))
convert_btn.pack(pady=(40,0))


win.mainloop()