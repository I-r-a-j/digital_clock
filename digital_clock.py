from tkinter import *
import time

window = Tk()
window.title("Digital Clock")
window.geometry("600x400")


def mytime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    secound = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    zone = time.strftime("%Z")

    mytext = hour + ":" + minute + ":" + secound + " " + am_pm
    mytext2 = day + " ," + zone

    myLabel.config(text=mytext)
    myLabel.after(1000, mytime)
    myLabel2.config(text=mytext2)


myLabel = Label(window, text="", font=(
    "Arial", 72), fg="white", bg="blue")
myLabel.pack()

myLabel2 = Label(window, text="hello", font=("Arial", 26))
myLabel2.pack()
mytime()

window.mainloop()
