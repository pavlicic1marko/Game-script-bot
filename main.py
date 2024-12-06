import tkinter as tk
from tkinter import messagebox
import multiprocessing
from Scripts.approve_all_roles_using_images import  approve_5_role_and_handel_exceptions
from  Scripts.first_lady_remove_and_approve import first_lady_approve_and_remove_roles

window_title = "First Lady Approve Bot"


class ProcessControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(window_title)
        self.process = None

        # app description
        self.app_label = tk.Label(root, text="Bot approves users in list for all 5 roles", fg='blue', font=('Arial', 11))
        self.app_label.pack()

        # Create buttons
        self.start_button = tk.Button(root, text="Start FL Bot", command=self.start_process)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop FL Bot", command=self.stop_process)
        self.stop_button.pack(pady=10)

        # app warning
        self.app_label = tk.Label(root, text="To stop the bot move mouse to the corner of your screen", fg='red', font=('Arial', 12))
        self.app_label.pack(pady=20)



    def start_process(self):
        """Starts a new process running target function."""
        if self.process and self.process.is_alive():
            messagebox.showinfo("Info", f"FL Bot is already running, PID: {self.process.pid}.")
            return

        self.process = multiprocessing.Process(target=first_lady_approve_and_remove_roles)
        self.process.start()

    def stop_process(self):
        """Terminates the process using its PID."""
        if not self.process or not self.process.is_alive():
            messagebox.showinfo("Info", "FL Boot is currently not running.")
            return

        # Terminate the process
        self.process.terminate()
        self.process.join()  # Wait for the process to finish cleanup
        messagebox.showinfo("Info", "Stopped FL Bot ")
        self.process = None  # Reset the process


if __name__ == "__main__":
    multiprocessing.freeze_support()
    root = tk.Tk()
    app = ProcessControllerApp(root)
    canvas = tk.Canvas(root, width=600, height=100)
    canvas.pack()
    root.mainloop()
