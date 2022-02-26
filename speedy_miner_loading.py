from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(3)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        progress_window.update_idletasks()

    warning = Label(progress_window, text="Did you really wait for this to download? You fool!", font=("Arial", 9))
    warning.pack()

#loading screen
progress_window = Tk()
progress_window.title("!")
progress_window.iconbitmap()

#download warning label
warning = Label(progress_window, text="Do NOT leave window until download is complete!", font=("Arial", 9))
warning.pack()

percent = StringVar()
text = StringVar()

bar = Progressbar(progress_window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(progress_window, textvariable = percent).pack()
taskLabel = Label(progress_window, textvariable = text).pack()

button = Button(progress_window, text="Download", command = start,).pack()

progress_window.mainloop()