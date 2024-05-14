import tkinter as tk
from tkinter import ttk
import pandas as pd

def add_entry():
    medicine_name = medicine_name_entry.get()
    time = time_entry.get()
    duration = duration_entry.get()

    # Insert entry into the table
    medicine_table.insert('', 'end', values=(medicine_name, time, duration))

    # Save entry to Excel file
    save_to_excel(medicine_name, time, duration)

    # Clear entry fields
    clear_fields()

def clear_fields():
    medicine_name_entry.delete(0, 'end')
    time_entry.delete(0, 'end')
    duration_entry.delete(0, 'end')


import pandas as pd


def save_to_excel(medicine_name, time, duration, filename="medicine_data.xlsx"):
    try:
        # Check if the file already exists
        existing_df = pd.read_excel(filename)

        # Create a new DataFrame for the new entry
        new_entry = pd.DataFrame({'Medicine Name': [medicine_name],
                                  'Time': [time],
                                  'Duration': [duration]})

        # Concatenate the existing DataFrame with the new entry DataFrame
        updated_df = pd.concat([existing_df, new_entry], ignore_index=True)

        # Write the updated DataFrame to the Excel file
        updated_df.to_excel(filename, index=False)
    except FileNotFoundError:
        # If the file does not exist, create a new Excel file with headers
        data = {'Medicine Name': [medicine_name], 'Time': [time], 'Duration (Days)': [duration]}
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)


# Create the GUI window
window = tk.Tk()
window.title("Manual Entry")
window.geometry("400x350")

# Create a table to display manual entries
columns = ('Medicine Name', 'Time', 'Duration (Days)')
medicine_table = ttk.Treeview(window, columns=columns, show='headings')

# Define column headings
for col in columns:
    medicine_table.heading(col, text=col)

# Add table to window
medicine_table.pack(fill='both', expand=True)

# Add entry fields for manual entry
medicine_name_label = ttk.Label(window, text="Medicine Name:")
medicine_name_label.pack(pady=5)
medicine_name_entry = ttk.Entry(window)
medicine_name_entry.pack(pady=5)

time_label = ttk.Label(window, text="Time (e.g., 11am, 12pm):")
time_label.pack(pady=5)
time_entry = ttk.Entry(window)
time_entry.pack(pady=5)

duration_label = ttk.Label(window, text="Duration (Days):")
duration_label.pack(pady=5)
duration_entry = ttk.Entry(window)
duration_entry.pack(pady=5)

# Add button to add entry
add_button = ttk.Button(window, text="Add Entry", command=add_entry)
add_button.pack(pady=5)

# Run the GUI main loop
window.mainloop()
