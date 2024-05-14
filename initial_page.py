import tkinter as tk
from tkinter import ttk
import os
import pandas as pd
def open_spor():
    os.system('python ocr.py')
    os.system('python alarm.py')

def open_manual_entry():
    os.system('python manual_entry.py')
    os.system('python alarm.py')

def open_verify():
    os.system('python new.py')



# Create the initial page GUI window
initial_page = tk.Tk()
initial_page.title("HOME PAGE")

initial_page.configure(bg="lightblue")
# Get screen width and height
screen_width = initial_page.winfo_screenwidth()
screen_height = initial_page.winfo_screenheight()

# Desired window width and height (adjust as needed)
window_width = 900
window_height = 500

# Calculate the offset to center the window
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2

# Set window geometry with calculated offsets
initial_page.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Add a heading "MedVision"
heading_label = tk.Label(initial_page, text="MedVision", font=("Arial", 24), bg="lightblue")
heading_label.pack(pady=20)

button_frame = tk.Frame(initial_page, bg="lightblue")
button_frame.pack(fill="both", expand=True)

# Create style for buttons
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 24, "bold"))

# Create buttons with the custom style and pack them in the frame
ocr_button = ttk.Button(button_frame, text="OCR", style="Custom.TButton", command=open_spor)
ocr_button.pack(side="left", padx=20, pady=20, expand=True, fill="both")  # Pack at left with padding and expand

manual_entry_button = ttk.Button(button_frame, text="Manual Entry", style="Custom.TButton", command=open_manual_entry)
manual_entry_button.pack(side="left", padx=20, pady=20, expand=True, fill="both")  # Pack at left with padding and expand

verify_button = ttk.Button(button_frame, text="Verify", style="Custom.TButton", command=open_verify)
verify_button.pack(side="left", padx=20, pady=20, expand=True, fill="both")  # Pack at left with padding and expand

# Run the initial page GUI main loop
initial_page.mainloop()