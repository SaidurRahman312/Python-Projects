import tkinter as tk
from tkinter import filedialog
import yt_dlp


def download_video(url, save_path):
    """
    Downloads the video from the provided YouTube URL to the specified save path.

    Parameters:
    - url (str): The URL of the YouTube video to be downloaded.
    - save_path (str): The directory where the video will be saved.
    """
    try:
        # Options for yt-dlp
        ydl_opts = {
            'format': 'best',  # Download the best quality format available
            'outtmpl': f'{save_path}/%(title)s.%(ext)s'  # Output template for the downloaded video
        }
        # Initialize yt-dlp with the specified options and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        # Print any exceptions that occur during the download
        print(e)


def open_file_dialog():
    """
    Opens a file dialog for the user to select a directory.

    Returns:
    - folder (str): The selected directory path.
    """
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == "__main__":
    # Initialize and hide the Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter a YouTube URL
    video_url = input("Please enter a YouTube URL: ")
    # Open the file dialog to select the save directory
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Downloading...")
        # Download the video to the selected directory
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
