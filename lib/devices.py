import curses
import os
import configparser
def set_selected_device(selected_device):
    config = configparser.ConfigParser()
    config.read('./lib/camsimulate.conf')
    config.set('CamSimulate','device',selected_device)
    with open('./lib/camsimulate.conf','w') as configfile:
        config.write(configfile)
def list_video_devices():
    devices = []
    for file in os.listdir('/dev'):
        if file.startswith('video'):
            devices.append(os.path.join('/dev', file))
    return devices

def select_device(stdscr):
    stdscr.clear()
    devices = list_video_devices()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    selected_option = 0
    while True:
        for idx, file in enumerate(devices):
            if idx == selected_option:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")

            stdscr.refresh()

            key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(devices)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(devices)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_device = devices[selected_option]
            set_selected_device(selected_device)
            break
    stdscr.clear()
    stdscr.refresh()