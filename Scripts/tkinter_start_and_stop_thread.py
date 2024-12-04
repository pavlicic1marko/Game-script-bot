import multiprocessing
import os
from click_on_help_allies_image import help_allies


def example_function():
    help_allies()


if __name__ == "__main__":
    # Create a new process
    process = multiprocessing.Process(target=example_function)

    # Start the process
    process.start()

    # Print the PID of the process
    print(f"Started process with PID: {process.pid}")

    # Wait for the process to finish
    process.join()
    print("Process completed.")