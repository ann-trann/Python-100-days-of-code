from tkinter import *
# import turtle

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Label

my_label = Label(text="I Am a Label", font=("Consolas", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=50)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button

def button_clicked():
    pass
    # print("I got clicked")
    # my_label.config(text="Button got clicked")
    #
    # new_text = input.get()
    # my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
