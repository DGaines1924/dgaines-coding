# daily_practice.py
import datetime  # importing the time-based library
import textwrap  # for wrapping long text lines
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
root = tk.Tk()
root.withdraw()

# Get today's date
today = datetime.date.today()

# Get current date and time
now = datetime.datetime.now()  # returns date + time
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Ask user what they learned or did today
entry = simpledialog.askstring(
                        title="Daily Work Sesh",
                        prompt=f"What new knowledge has been gained today?\n ({timestamp})"
                            )

if entry is None or entry.strip() == "":
    messagebox.showinfo("No Entry", "No entry was saved today.")
    root.destroy()
    exit()

# Wrap the text at 50 characters per line
wrapped_entry = textwrap.fill(entry, width=60)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "daily_log.txt")

# Save it to a file
with open(file_path, "a") as file:
    file.write(f"{timestamp}:\n{wrapped_entry}\n\n")  # extra newline between entries

messagebox.showinfo("Saved", "Good shi, consistency is key.")
root.destroy()