import configparser
import curses
import subprocess
def configuration():
	config = configparser.ConfigParser()
	config.read('./lib/camsimulate.conf')
	args = {}
	args["device"] = config.get('CamSimulate', 'device')
	args["source"] = config.get('CamSimulate', 'source')
	return args
def execute(args):
	device = args['device']
	source = args['source']
	ffmpeg_command = f"ffmpeg -re -i { args['source'] } -f v4l2 { args['device'] }"
	ffmpeg_command = ffmpeg_command.split()
	subprocess.call(ffmpeg_command)
def start(stdscr):
	curses.curs_set(0)
	args = configuration()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	stdscr.clear()
	stdscr.refresh()
	stdscr.attron(curses.color_pair(1))
	stdscr.addstr(0, 0, f"device : { args['device'] }")
	stdscr.addstr(1, 0, f"source : { args['source'] }")
	stdscr.addstr(3, 0, f"PRESS ANY KEY TO CONTINUE")
	key = stdscr.getch()
	if key:
		execute(args=args)