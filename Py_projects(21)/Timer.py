# Alarm Timer with Sound Notification
# This script sets an alarm for a specified duration (in minutes and seconds) and plays a sound when the time is up.

from playsound import playsound
import time

# ANSI escape codes for clearing the screen and returning the cursor to the home position
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    """
    Function to set an alarm for the specified duration.
    Args:
    seconds (int): Total time in seconds for the alarm countdown.
    """
    time_elapsed = 0

    # Clear the screen
    print(CLEAR)

    # Countdown loop
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Display the time remaining
        print(f"{CLEAR_AND_RETURN} Alarm will ring in: {minutes_left:02d}:{seconds_left:02d}")

    # Play the alarm sound
    playsound('alarm.mp3')

# Input the duration for the timer
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

# Set the alarm
alarm(total_seconds)
