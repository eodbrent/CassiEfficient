import tkinter as tk
from tkinter import filedialog
import pdfplumber
import os
import re

from names import physician_names

# TODO: Duplicates - remove
# TODO: Begin Range date is 30 calendar days before Recert Date, IDG Date at the end
# TODO: Parse out
#           FC
#           LOC
#           DX
#           DX Description
#           Attending physician
#           INS PLAN CODE
#           RECERT RANGE
#           * DAYS REMAINING


# Initialize Tkinter
root = tk.Tk()

options = {
    "r": "(r)ecerts",
    "c": "(c)ompare documents"
}

def input_ask(prompt, option_map):
    optional_vals = "\n".join(f"{key}: {value}" for key, value in option_map.items())
    while True:
        user_input = input(f"{prompt} - select one of the following options:\n{optional_vals}\n")
        if user_input in option_map.keys():
            return user_input  # Return the key
        else:
            print("Invalid selection. Please try again.")

def get_recert_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt"), ("Excel files", "*.xlsx")], initialdir=script_dir)
    root.update()

    if fpath:
        print(fpath)
        extracted_text = extract_text_from_pdf(fpath)
        # Print the extracted text
        print(extracted_text)
    root.withdraw()


def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""

        # Now extract text and process it from all pages
        for page in pdf.pages:
            raw_text = page.extract_text()

            # Skip known physician names
            cleaned_text = skip_known_names(raw_text, physician_names)

            text += cleaned_text
        return text


def skip_known_names(text, known_names):
    # Skip over known names (first and last names) with case-insensitive matching
    for first_name, last_name in known_names.items():
        # Regex to remove the full name (first and last name) from the text
        text = re.sub(rf'\b{first_name} {last_name}\b', '', text, flags=re.IGNORECASE)
    return text

def main():
    # Ask the user for their choice
    init_prompt = "What would you like to do?"
    # choice = input_ask(init_prompt, options) # not used during recert coding
    choice = "r"
    if choice:
        print(f"User's choice: {choice}")

    if choice == "r":
        get_recert_pdf()

    root.mainloop()

if __name__ == "__main__":
    main()