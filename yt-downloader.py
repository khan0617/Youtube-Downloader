import tkinter as tk
from tkinter import filedialog
import os
import pytube



root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{int(width / 4)}x{int(height / 2)}')
root.resizable(True, True)
root.title('YouTube Downloader')

# Clear the display for the YouTube URL box by setting ints StringVar to ''
def clearURL():
    yt_link.set('')


# Set the destination StringVar's data to a new filepath selected by a user
def browse():
    dir = tk.filedialog.askdirectory(initialdir=os.getcwd(), title='Select a destination folder')

    if dir != '' and dir != ():
        destination.set(dir)

def createWidgets():

    # Main title of the window, appears on the top row
    label_title = tk.Label(
            text='YouTube Download using Tkinter and PyTube',
            font=('Arial', 18, 'underline'),
            padx=20,
            pady=30
        )
    label_title.grid(row=0, column=1, columnspan=2)

    # Label for the YouTube URL Entry field
    label_yt_link = tk.Label(
        text='YouTube URL',
        font=('Arial', 12),
        padx=20
    )
    label_yt_link.grid(row=1, column=0, pady=30)

    # Text Entry box for the YouTube URL
    entry_yt_link = tk.Entry(
        width=70,
        font=('Arial', 12),
        textvariable=yt_link,
        highlightcolor='#7af5ed',
        highlightthickness=4,
        relief=tk.FLAT
    )
    entry_yt_link.grid(row=1, column=1, pady=30, padx=50)

    btn_clear_yt_link = tk.Button(
        text='Clear',
        font=('Arial', 12),
        width=10,
        bg='#fa5a5a',
        activebackground='#bf4545',
        fg='white',
        command=lambda: clearURL()
    )
    btn_clear_yt_link.grid(row=1, column=3)

    # Label for the YouTube URL Entry field
    label_destination = tk.Label(
        text='File Destination',
        font=('Arial', 12),
    )
    label_destination.grid(row=2, column=0, pady=30)

    # Text Entry box for the YouTube URL
    entry_destination = tk.Entry(
        width=70,
        font=('Arial', 12),
        textvariable=destination,
        highlightcolor='#7af5ed',
        highlightthickness=4,
        relief=tk.FLAT
    )
    entry_destination.grid(row=2, column=1, pady=30, padx=50)
    entry_destination.insert(0, os.getcwd())

    # Button to open up a file dialog to allow user to select a directory
    btn_browse = tk.Button(
        text='Browse',
        font=('Arial', 12),
        width=10,
        bg='#e6e8e6',
        activebackground='#b8bab9',
        fg='black',
        command=browse
    )
    btn_browse.grid(row=2, column=3)


yt_link = tk.StringVar()
destination = tk.StringVar()

createWidgets()
root.mainloop()