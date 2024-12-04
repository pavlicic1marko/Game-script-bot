import subprocess
import tkinter as tk

proclist = []


def clicked():
    proclist.clear()
    script = 'approve_all_roles_using_images.py'
    proc = subprocess.Popen(['python', script])
    proclist.append(proc)


def kill_tasks():
    proc=proclist[0]
    if proc and proc.poll() is None:
        print('Killing process with PID', proc.pid)
        proc.kill()
    proclist.clear()


root = tk.Tk()
root.geometry('400x400')
root.title('Last War Bot')

tk.Button(root, text='Start 1st lady Approve', width=20, command=clicked).pack()
tk.Button(root, text='Stop', width=20, command=kill_tasks).pack()

root.mainloop()
