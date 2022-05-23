import os
import ffmpeg
import tkinter as tk
from tkinter import LEFT, filedialog
from tkinter.ttk import *
from pytube import YouTube



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

# if link is invalid, show an error message and make the border of the entry box red.
# otherwise, download whatever is specified "a" for audio, "v" for video
def download(type):
    try:
        yt = YouTube(yt_link.get(),
            on_progress_callback=progress_func,
            on_complete_callback=complete_func
        )

        ## we want to download the best quality video stream: download audio and video separate, then merge.
        if type == 'v':
            best_audio = yt.streams.get_audio_only()
            best_video = yt.streams.filter(only_video=True).first()

        else:
            pass

        label_invalid_link.grid_remove()
        entry_yt_link.config(highlightbackground="#b8b7b6")

    except Exception as e:
        print(f'Error: {e}')
        label_invalid_link.grid()
        entry_yt_link.config(highlightbackground="red")

# called when the download has completed, will display "Done! File location:"
def complete_func(stream, file_path):
    pass

# Updates a progress label showing percentage that's been downloaded.
def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize() # size in bytes of the whole stream
    percent_completed = (total_size - bytes_remaining) / total_size
    print(f'Percent Completed: {percent_completed}')

def createWidgets():

    # Main title of the window, appears on the top row
    label_title = tk.Label(
            text='YouTube Download using Tkinter and PyTube',
            font=('Arial', 18, 'underline'),
            padx=20,
            pady=30
        )
    label_title.grid(row=0, column=1, columnspan=2)

    # Error message for when an invalid link is entered. Hidden initially.
    global label_invalid_link
    label_invalid_link = tk.Label(
        text='Invalid link! Please enter a valid YouTube URL.',
        font=('Arial', 12),
        fg="red",
        padx=20,
    )
    label_invalid_link.grid(row=1, column=1)
    label_invalid_link.grid_remove()

    # Label for the YouTube URL Entry field
    label_yt_link = tk.Label(
        text='YouTube URL',
        font=('Arial', 12),
        padx=20
    )
    label_yt_link.grid(row=2, column=0, pady=30)

    # Text Entry box for the YouTube URL
    global entry_yt_link
    entry_yt_link = tk.Entry(
        width=100,
        font=('Arial', 10),
        textvariable=yt_link,
        highlightcolor='#7af5ed',
        highlightbackground='#b8b7b6',
        highlightthickness=4,
        relief=tk.FLAT
    )
    entry_yt_link.grid(row=2, column=1, pady=30, padx=50)
    # entry_yt_link.bind('<FocusOut>', lambda event, a=entry_yt_link, b=label_invalid_link:
    #                     verifyLink(a, b))

    # Button to clear the YouTube URL entry box
    btn_clear_yt_link = tk.Button(
        text='Clear',
        font=('Arial', 12),
        width=10,
        bg='#fa5a5a',
        activebackground='#bf4545',
        fg='white',
        command=lambda: clearURL()
    )
    btn_clear_yt_link.grid(row=2, column=3)

    # Label for the YouTube URL Entry field
    label_destination = tk.Label(
        text='File Destination',
        font=('Arial', 12),
    )
    label_destination.grid(row=3, column=0, pady=30)

    # Text Entry box for the YouTube URL
    entry_destination = tk.Entry(
        width=100,
        font=('Arial', 10),
        textvariable=destination,
        highlightcolor='#7af5ed',
        highlightbackground='#b8b7b6',
        highlightthickness=4,
        relief=tk.FLAT
    )
    entry_destination.grid(row=3, column=1, pady=30, padx=50)
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
    btn_browse.grid(row=3, column=3)

    # frame (container) to hold the three items below pertaining to file download
    frame = tk.Frame(root)
    frame.grid(row=4, column=1)

    # Label for the YouTube URL Entry field
    label_download = tk.Label(
        master=frame,
        text='Download',
        font=('Arial', 12),
        padx=20
    )
    label_download.pack(side=LEFT, padx=50)

    btn_audio = tk.Button(
        master=frame,
        text='Best\nAudio',
        font=('Arial', 12),
        width=10,
        bg='#04b6de',
        activebackground='#038cab',
        fg='black',
        command= lambda: download('a')
    )
    btn_audio.pack(side=LEFT, padx=50)

    # Btn to initiate video file download
    btn_video = tk.Button(
        master=frame,
        text='Best\nVideo',
        font=('Arial', 12),
        width=10,
        bg='#3eedc7',
        activebackground='#2dad92',
        fg='black',
        command= lambda: download('v')
    )
    btn_video.pack(side=LEFT, padx=50)

    global label_progress
    label_progress = tk.Label(
        text='Download progress: 50%',
        font=('Arial', 24),
        fg='#349134',
        padx=20,
        pady=100,
    )
    label_progress.grid(row=5, column=1)


yt_link = tk.StringVar()
destination = tk.StringVar()

createWidgets()

root.mainloop()