import os
import shutil
import datetime
import schedule
import time

# Source and Destination Directories
source_dir = "D:/Python_script/Gamca"
destination_dir = "D:/Backups"

def copy_folder_to_directory(source, dest):
    """
    Copies the entire folder from the source directory to the destination directory.
    Creates a subfolder with the current date in the destination directory to avoid overwriting.
    """
    # Get the current date
    today = datetime.date.today()
    # Create the destination directory with today's date
    dest_dir = os.path.join(dest, str(today))

    try:
        # Copy the folder from source to destination
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        # If the folder already exists, print a message
        print(f"Folder already exists in: {dest}")

# Schedule the folder copy task to run daily at 09:23
schedule.every().day.at("09:23").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Run the scheduled tasks
while True:
    # Check and run any pending tasks
    schedule.run_pending()
    # Sleep for 10 seconds before checking again
    time.sleep(10)
