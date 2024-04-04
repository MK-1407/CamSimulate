import os
import curses
import subprocess
from lib.devices import select_device
from lib.sources import select_source
from lib.cam import start
if not any(os.path.exists('/dev/video' + str(i)) for i in range(10)):
    subprocess.call('sudo modprobe v4l2loopback devices=1 card_label="CS_Cam_pro" exclusive_caps=1'.split())

def select_menu_options(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    menu_options = ["START","CHANGE DEVICE","CHANGE SOURCE","EXIT"]
    selected_option = 0
    while True:
        stdscr.clear()
        stdscr.refresh()
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(0, 0, "Select an input file:")        
        for idx, file in enumerate(menu_options):
            if idx == selected_option:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu_options[selected_option] == "START":
                stdscr.clear()
                start(stdscr)
            elif menu_options[selected_option] == "CHANGE SOURCE":
                stdscr.clear()
                select_source(stdscr)
            elif menu_options[selected_option] == "CHANGE DEVICE":
                select_device(stdscr)
            elif menu_options[selected_option] == "EXIT":
                break
            else:
                menu_options = menu_options[selected_option]
                break
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Select input file
    menu_options= select_menu_options(stdscr)
    stdscr.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
        curses.endwin()
    except KeyboardInterrupt:
        pass