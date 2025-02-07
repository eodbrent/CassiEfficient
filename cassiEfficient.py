import PyPDF2 as pyPDF
import pdfplumber
import tkinter as tk
from tkinter import filedialog


def input_prompt(prompt, options):
    while True:
        user_input = input(f"{prompt} - select one of the following options: {options}")
        if user_input in options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of: {', '.join(options)}.")

init_prompt = "what would you like to do?"
initial_options = ["recerts", "find differences"]
selection = input_prompt(init_prompt, initial_options)

root = tk.Tk()
root.withdraw()  # Hide the root window
file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
print("Selected file:", file_path)
print(selection)
