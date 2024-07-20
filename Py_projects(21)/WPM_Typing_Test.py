# Speed Typing Test Program
# This program is a simple speed typing test that uses the curses library to display text and capture user input.
# The user needs to type the displayed text as quickly and accurately as possible.
# The program calculates and displays the user's words per minute (WPM) as they type.

import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    """
    Displays the start screen with a welcome message and instructions to press any key to begin.
    """
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    """
    Displays the target text, current input, and WPM on the screen.

    Args:
    stdscr: The standard screen object from curses.
    target: The target text the user needs to type.
    current: The current text the user has typed.
    wpm: The current words per minute speed.
    """
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Default color is green
        if char != correct_char:
            color = curses.color_pair(2)  # Incorrect characters are displayed in red

        stdscr.addstr(0, i, char, color)


def load_text():
    """
    Loads a random line of text from a file to be used as the target text.

    Returns:
    A random line of text from the file.
    """
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    """
    Runs the main typing test, capturing user input and calculating WPM.

    Args:
    stdscr: The standard screen object from curses.
    """
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Non-blocking input

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key to exit
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):  # Handle backspace
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    """
    Initializes color pairs and runs the main loop for the typing test.

    Args:
    stdscr: The standard screen object from curses.
    """
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct characters
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Incorrect characters
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Other text

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:  # ESC key to exit
            break


# Run the main function within the curses wrapper
wrapper(main)
