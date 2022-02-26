from multiprocessing.spawn import import_main_path
from tkinter import *
import time

window = Tk()

window.title("Installation")
window.geometry("250x150")
window.config(bg="blue")

window.attributes('-fullscreen', True)

welcome = Label(window, text="To continue with the miner installation, press 'Download' ", bg="blue", fg="white", font=("Arial", 25))
welcome.pack()

def nextPage():
    import speedy_miner_loading    
    

download = Button(window, text ="Download", command = nextPage, padx="10", pady="10")
download.pack()


window.mainloop()
