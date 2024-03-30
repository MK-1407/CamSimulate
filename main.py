import subprocess
import os
import curses

def list_video_devices():
    devices = []
    for file in os.listdir('/dev'):
        if file.startswith('video'):
            devices.append(os.path.join('/dev', file))
    return devices
def select_device(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    devices = list_video_devices()
    selected_device = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select a video device:")
        for idx, device in enumerate(devices):
            if idx == selected_device:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {device}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {device}")
        
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_device = (selected_device - 1) % len(devices)
        elif key == curses.KEY_DOWN:
            selected_device = (selected_device + 1) % len(devices)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return devices[selected_device]

def select_input_file(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    input_file = []
    input_files = os.listdir('.') + ['FILE FROM URL']
    selected_file = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select an input file:")        
        for idx, file in enumerate(input_files):
            if idx == selected_file:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {file}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_file = (selected_file - 1) % len(input_files)
        elif key == curses.KEY_DOWN:
            selected_file = (selected_file + 1) % len(input_files)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            input_file = input_files[selected_file]
            break
    if input_file == "FILE FROM URL":
        stdscr.clear()
        stdscr.addstr(0,0, "Enter URL Example:- (https://vide_src.com/video.mp4)")
        textbox = stdscr.subwin(5, 20, 1, 0)
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
        return text
    else:
        return input_file

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    stdscr.addstr(0, 0, "Please use as administrator")
    stdscr.refresh()
    stdscr.getch()

    # Load v4l2loopback if not already loaded
    if not any(os.path.exists('/dev/video' + str(i)) for i in range(10)):
        subprocess.call('sudo modprobe v4l2loopback'.split())

    # Select video device
    selected_device = select_device(stdscr)

    # Select input file
    input_file = select_input_file(stdscr)

    # Execute ffmpeg command
    ffmpeg_command = f"ffmpeg -re -i {input_file} -f v4l2 {selected_device}"
    stdscr.clear()
    stdscr.addstr(0, 0, f"Running command: {ffmpeg_command}")
    stdscr.refresh()
    subprocess.call(ffmpeg_command.split())
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
