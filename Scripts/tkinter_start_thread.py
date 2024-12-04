import tkinter as tk
from tkinter import messagebox
import threading
import time
from click_on_help_allies_image import help_allies

class ThreadControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thread Controller")
        self.stop_event = threading.Event()
        self.thread = None

        # Create buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_thread)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_thread)
        self.stop_button.pack(pady=10)

    def example_function(self, stop_event):
        """Function that runs in a thread."""
        print("Thread started.")
        while not stop_event.is_set():
            help_allies()
        print("Thread stopping.")

    def start_thread(self):
        """Starts the worker thread."""
        if self.thread and self.thread.is_alive():
            messagebox.showinfo("Info", "Thread is already running.")
            return

        self.stop_event.clear()  # Reset the stop flag
        self.thread = threading.Thread(target=self.example_function, args=(self.stop_event,))
        self.thread.start()
        print("Thread has been started.")

    def stop_thread(self):
        """Signals the thread to stop."""
        if not self.thread or not self.thread.is_alive():
            messagebox.showinfo("Info", "No thread is running.")
            return

        self.stop_event.set()  # Signal the thread to stop
        self.thread.join()  # Wait for the thread to stop
        print("Thread has been stopped.")

# Create the Tkinter app
root = tk.Tk()
app = ThreadControllerApp(root)
root.mainloop()