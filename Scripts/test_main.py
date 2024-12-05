import tkinter as tk
from tkinter import messagebox
import multiprocessing
import os
from click_on_help_allies_image import help_allies


class ProcessControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Controller")
        self.process = None

        # Create buttons
        self.start_button = tk.Button(root, text="Start Process", command=self.start_process)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Process", command=self.stop_process)
        self.stop_button.pack(pady=10)

    def start_process(self):
        """Starts a new process running example_function."""
        if self.process and self.process.is_alive():
            messagebox.showinfo("Info", f"Process is already running with PID {self.process.pid}.")
            return

        self.process = multiprocessing.Process(target=help_allies)
        self.process.start()
        messagebox.showinfo("Info", f"Started process with PID {self.process.pid}.")

    def stop_process(self):
        """Terminates the process using its PID."""
        if not self.process or not self.process.is_alive():
            messagebox.showinfo("Info", "No process is currently running.")
            return

        # Terminate the process
        self.process.terminate()
        self.process.join()  # Wait for the process to finish cleanup
        messagebox.showinfo("Info", f"Terminated process with PID {self.process.pid}.")
        self.process = None  # Reset the process


if __name__ == "__main__":
    multiprocessing.freeze_support()
    root = tk.Tk()
    app = ProcessControllerApp(root)
    root.mainloop()
