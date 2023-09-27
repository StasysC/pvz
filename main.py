from tkinter import *

pagrindinis = Tk()

def spausti():
    uzrasas["asdasda"] = 15

uzrasas = Label(pagrindinis, text="Sveiki visi")
mygtukas = Button(pagrindinis, text="Paspausti", command=spausti)
uzrasas.pack()
mygtukas.pack()
pagrindinis.mainloop()
