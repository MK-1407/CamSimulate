import curses
import os
import configparser
def set_selected_source(selected_file):
    config = configparser.ConfigParser()
    config.read('./lib/camsimulate.conf')
    config.set('CamSimulate','source',selected_file)
    with open('./lib/camsimulate.conf','w') as configfile:
        config.write(configfile)
def select_source(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    selected_file = 0
    current_dir = os.getcwd()
    input_file = []
    while True:
        input_files = ['../'] + os.listdir(current_dir) + ['FILE FROM URL']
        max_length = max(len(s) for s in input_files)
        height, width = stdscr.getmaxyx()
        stdscr.clear()
        stdscr.addstr(0, 0, "Select an input file:")
        start_idx = max(0, selected_file - height + 4)  # Adjust start index based on selected item
        end_idx = min(len(input_files), start_idx + height - 2)
        for idx in range(start_idx, end_idx):
            file = input_files[idx]
            try:
                if idx == selected_file:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(idx - start_idx + 2, 0, f"{idx + 1}. {file[:width-3]}")
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(idx - start_idx + 2, 0, f"{idx + 1}. {file[:width-3]}")
            except:
                pass
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_file = (selected_file - 1) % len(input_files)
        elif key == curses.KEY_DOWN:
            selected_file = (selected_file + 1) % len(input_files)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if selected_file == 0:
                current_dir = os.path.dirname(current_dir)
            else:
                selected_item = input_files[selected_file]
                selected_path = os.path.join(current_dir, selected_item)
                if os.path.isdir(selected_path):
                    current_dir = selected_path
                else:
                    input_file = selected_path
                    break

    if input_file == "FILE FROM URL":
        curses.curs_set(0)
        stdscr.clear()
        stdscr.addstr(0,0, "ENTER URL: ")
        stdscr.refresh()
        textbox = stdscr.subwin(0, 0, 1, 1)
        textbox.border(0)
        textbox.refresh()

        # Move cursor inside the textbox
        curses.curs_set(1)
        # Allow user input
        curses.echo()
        # Get user input until they press Enter
        text = textbox.getstr(1, 1).decode(encoding="utf-8")
        # Turn off cursor
        curses.curs_set(0)
        # Stop echoing
        curses.noecho()
        set_selected_source(text)
    else:
        set_selected_source(input_file)