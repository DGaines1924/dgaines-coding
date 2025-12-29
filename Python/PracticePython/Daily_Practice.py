# daily_practice.py
import datetime  # importing the time-based library
import textwrap  # for wrapping long text lines

# Get today's date
today = datetime.date.today()

# Get current date and time
now = datetime.datetime.now()  # returns date + time
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Ask user what they learned or did today
entry = input(f"What new knowledge has been gained today ({timestamp})? ")

# Wrap the text at 50 characters per line
wrapped_entry = textwrap.fill(entry, width=60)

# Save it to a file
with open("daily_log.txt", "a") as file:
    file.write(f"{timestamp}:\n{wrapped_entry}\n\n")  # extra newline between entries

print("Good shi, consistency is key.")
