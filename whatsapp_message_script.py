import pywhatkit
import csv
import tkinter as tk
from tkinter import filedialog

# Open a dialog box to select the CSV file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    numbers = [row[0] for row in reader]

# Add the Indian country code to each number if it's not already there
numbers = [number if number.startswith('+91') else '+91' + number for number in numbers]

# Open a dialog box to enter the message
message = tk.simpledialog.askstring("Message", "Enter the message:")

# Open a dialog box to enter the send time
send_time = tk.simpledialog.askstring("Send Time", "Enter the send time (HH:MM):")

# Validate the send time
if len(send_time) != 5 or not send_time[2] == ':':
    print("Invalid send time format! Please enter the time in HH:MM format.")
else:
    # Split the send time into hours and minutes
    send_time = send_time.split(':')
    hour = int(send_time[0])
    minutes = int(send_time[1])

    # Send the message to each number in the list
    for number in numbers:
        pywhatkit.sendwhatmsg(number, message, hour, minutes)

    print("Messages sent successfully!")
