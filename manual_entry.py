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
window.geometry("680x580")
window.config(bg='lightblue')

header_frame = ttk.Frame(window, relief='raised', borderwidth=2)
header_frame.pack(fill='x', pady=10)

# Title label
title_label = ttk.Label(header_frame, text="Manual Entry", font=("Arial", 20))
title_label.pack(pady=5)

# Content area frame
content_frame = ttk.Frame(window)
content_frame.pack(fill='both', expand=True, pady=10)

style = ttk.Style()
style.map('Treeview', background='lightblue')  # Set background for the entire Treeview
style.map('Treeview.Heading', background='lightgray', font=[('!disabled', ('Arial', 12, 'bold'))])  # Style for headings

columns = ('Medicine Name', 'Time', 'Duration (Days)')
medicine_table = ttk.Treeview(content_frame, columns=columns, show='headings', style='Treeview')

# Define column headings
for col in columns:
    medicine_table.heading(col, text=col)
    # Adjust column width here (adjust values as needed)
    medicine_table.column(col, width=100)

# Add table scrollbar
table_scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=medicine_table.yview)
medicine_table.configure(yscrollcommand=table_scrollbar.set)
table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

medicine_table.pack(fill='both', expand=True)



# Medicine Name section
medicine_name_frame = ttk.Frame(content_frame)
medicine_name_frame.pack(pady=5)

medicine_name_label = ttk.Label(medicine_name_frame, text="Medicine Name:", font=("Arial", 12))
medicine_name_label.pack(side=tk.LEFT)

medicine_name_entry = ttk.Entry(medicine_name_frame, background="lightblue")
medicine_name_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Time section (similar structure as medicine name)
time_frame = ttk.Frame(content_frame)
time_frame.pack(pady=5)

time_label = ttk.Label(time_frame, text="Time (e.g., 11:00, 22:15):", font=("Arial", 12))
time_label.pack(side=tk.LEFT)

time_entry = ttk.Entry(time_frame, background="lightblue")
time_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Duration section (similar structure as medicine name)
duration_frame = ttk.Frame(content_frame)
duration_frame.pack(pady=5)

duration_label = ttk.Label(duration_frame, text="Duration (Days):", font=("Arial", 12))
duration_label.pack(side=tk.LEFT)

duration_entry = ttk.Entry(duration_frame, background="lightblue")
duration_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)


# Add button to add entry
add_button = ttk.Button(window, text="Add Entry", command=add_entry)
add_button.pack(pady=5)

# Run the GUI main loop
window.mainloop()
