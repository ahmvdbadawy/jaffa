
# wrote by badawy

import tkinter
from tkinter import *
from tkinter import ttk

# Function placeholders for button actions
def submit_to_city():
    to_city = to_city_input.get()
    print('city is : '+to_city)
    # Update this function based on your needs

def submit_from_city():
    from_city = from_city_input.get()
    print('from city is : '+ from_city)
    # Update this function based on your needs

def clear():
    to_city_input.delete(0, 'end')
    from_city_input.delete(0, 'end')
    Text_frame.config(state=NORMAL)
    Text_frame.delete(1.0, END)
    Text_frame.insert(END, "About the City\n\n")
    Text_frame.config(state=DISABLED)

# Make a program window
window = Tk()
window.title("City Navigation")
window.geometry("383x1000")  # Updated geometry
window.configure(bg="#3498DB")  # Set background color

# Text frame
Text_frame = Text(window, bg="#2E4053", state=DISABLED, font=("Verdana", 12), foreground="white", insertbackground="white", bd=3, relief=SOLID, height=600, width=383)
Text_frame.place(x=0, y=0)

# Input frame
input_frame = LabelFrame(window, text="Direction", font=("bold", 14), labelanchor="n", bg="#3498DB", padx=10, pady=10, height=400, width=383)
input_frame.place(x=0, y=600)

# Label and Entry for "To" city
city_label = Label(input_frame, text="To", bg="#3498DB", font=("bold", 12), foreground="white")
city_label.place(x=10, y=10)

to_city_input = Entry(input_frame, bg="#B3C9F4", justify='left', font=("Verdana", 12))
to_city_input.place(x=80, y=10)

To_submit_button = Button(input_frame, text="Submit", bg="#4E6D8C", fg="white", font=("Verdana", 12), command=submit_to_city, relief=GROOVE)
To_submit_button.place(x=280, y=10)

# Label and Entry for "From" city
from_city_label = Label(input_frame, text="From", bg="#3498DB", font=("bold", 12), foreground="white")
from_city_label.place(x=10, y=50)

from_city_input = Entry(input_frame, bg="#B3C9F4", justify='left', font=("Verdana", 12))
from_city_input.place(x=80, y=50)

from_submit_button = Button(input_frame, text="Submit", bg="#4E6D8C", fg="white", font=("Verdana", 12), command=submit_from_city, relief=GROOVE)
from_submit_button.place(x=280, y=50)

# Horizontal line between two frames
h_line = ttk.Separator(window, orient='horizontal')
h_line.place(x=0, y=600, width=383)

# Clear fields
cls_button = Button(input_frame, text='Clear', bg='#E74C3C', fg='white', font=('Verdana', 12), command=clear, relief=GROOVE)    
cls_button.place(x=250, y=100, width=100, height=30)

# Set default title in Text_frame
clear()

window.mainloop()
