import subprocess
import math
import curses
from curses import wrapper

def reset_tablet_area():
    subprocess.run("xsetwacom set \"Wacom Bamboo One S Pen stylus\" ResetArea", shell=True)

def change_tablet_width(tablet_width : int):
    subprocess.run("xsetwacom set \"Wacom Bamboo One S Pen stylus\" Area 0 0 {0} {1}"
    .format(tablet_width, math.floor(int(tablet_width) * 1080/1920)), shell=True)

def user_interface():

    screen = curses.initscr()
    screen.addstr("1: Change tablet area to Width.\n2: Reset tablet area.\n")
    screen.refresh()

    user_input = screen.getkey()
    
    if user_input == "1":
        screen.clear()
        screen.addstr("Please enter a width:\nWidth: ")
        curses.echo()
        width = screen.getstr()
        change_tablet_width(int(width))

    elif user_input == "2":
        reset_tablet_area()

    curses.endwin()
    print("Window ended.")

def main(main_screen):
    user_interface()

wrapper(main)