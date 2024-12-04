import tkinter
import os
from subprocess import call
import threading

window = tkinter.Tk()
window.title("GUI")

def clicked():
    #os.system('python inference.py')
    #os.system('python extract_frames.py')

    # I used the threading approach

    threading.Thread(target=call, args=("python approve_all_roles.py" ,), ).start()



bt = tkinter.Button(window,text="approve all roles",command=clicked).pack()

window.geometry('400x400')
window.mainloop()