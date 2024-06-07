# Import
from tkinter import*

# Drawing the canvas
root = Tk(className="da bank")
wndw = Canvas(root, width=600, height=150, bg="silver")
wndw.create_rectangle(200, 10, 400, 100, fill="lightgray", outline="black")
money = wndw.create_text(300, 50, text="Lorem Ipsum", font="Arial 32")

# Adding


def add(num):
    file = open("cash.txt", "r")
    mon = file.read()
    file = open("cash.txt", "w")
    w = round(float(mon)+num, 2)
    file.write(str(w))
    file.close()
    update()


# Updating value


def update():
    global money
    wndw.delete(money)
    file = open("cash.txt", "r")
    v = "{:.2f}€".format(float(file.read()))
    money = wndw.create_text(300, 50, text=v, font="Arial 32")
    file.close()


# Buttons
b1 = Button(root, text="1¢", command=lambda: add(0.01), width=5, height=2, font="Arial 20", bg="dimgray")
b2 = Button(root, text="2¢", command=lambda: add(0.02), width=5, height=2, font="Arial 20", bg="dimgray")
b5 = Button(root, text="5¢", command=lambda: add(0.05), width=5, height=2, font="Arial 20", bg="dimgray")
b10 = Button(root, text="10¢", command=lambda: add(0.1), width=5, height=2, font="Arial 20", bg="dimgray")
b20 = Button(root, text="20¢", command=lambda: add(0.2), width=5, height=2, font="Arial 20", bg="dimgray")
bmin = Button(root, text="-10¢", command=lambda: add(-0.1), width=5, height=2, font="Arial 20", bg="dimgray")

# Packing
wndw.pack()
update()
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b5.pack(side=LEFT)
b10.pack(side=LEFT)
b20.pack(side=LEFT)
bmin.pack(side=RIGHT)
root.mainloop()
