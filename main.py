import re
import struct

import notification
from themes.testare import testare as theme

FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
qwerty_map = {
    2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9", 11: "0", 12: "-", 14: "[BACKSPACE]",
    16: "q", 17: "W", 18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 28: "\n",
    30: "a", 31: "s", 32: "d", 33: "f", 34: "g", 35: "h", 36: "j", 37: "k", 38: "l",
    44: "z", 45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: "m", 55: "*", 57: " "
}
last_term = ""
last_term_index = 0


def get_infile_path():
    with open("/proc/bus/input/devices") as f:
        lines = f.readlines()

        pattern = re.compile("Handlers|EV=")
        handlers = list(filter(pattern.search, lines))

        pattern = re.compile("EV=120013")

        for idx, elt in enumerate(handlers):
            if pattern.search(elt):
                line = handlers[idx - 1]

        pattern = re.compile("event[0-9]")
        infile_path = "/dev/input/" + pattern.search(line).group(0)

        return infile_path


def find_answer(term):
    global last_term
    global last_term_index

    if term == "r":
        if type(theme.get(last_term)) is list:
            return last_term, theme.get(last_term)[last_term_index]
        else:
            return last_term, theme.get(last_term)

    elif term == "s":
        stop()

    elif term == "n" and type(theme.get(last_term)) is list:
        if len(theme.get(last_term)) - 1 > last_term_index:
            last_term_index += 1
        else:
            last_term_index = 0

        return last_term, theme.get(last_term)[last_term_index]

    elif term == "p" and type(theme.get(last_term)) is list:
        if last_term_index > 0:
            last_term_index -= 1
        else:
            last_term_index = len(theme.get(last_term)) - 1

        return last_term, theme.get(last_term)[last_term_index]

    elif term in theme:
        if type(theme.get(term)) is list:
            last_term = term
            current_term = theme.get(term)[last_term_index]

            return last_term, current_term
        else:
            last_term = term
            return last_term, theme.get(term)

    return "WARNING", "Low memory. Please clean your hard-disk"


def start():
    notification.notify("WARNING", "Process started")

    in_file = open(get_infile_path(), "rb")
    event = in_file.read(EVENT_SIZE)

    typed = ""

    while event:
        (_, _, type, code, value) = struct.unpack(FORMAT, event)
        event = in_file.read(EVENT_SIZE)

        if code != 0 and type == 1 and value == 1:
            if code in qwerty_map:
                if qwerty_map[code] == "[BACKSPACE]":
                    typed = typed[:-1]
                elif qwerty_map[code] == "\n":
                    title, body = find_answer(typed)
                    notification.notify(title, body)
                    typed = ""
                else:
                    typed += qwerty_map[code]


def stop():
    exit()


try:
    start()
except:
    notification.notify("Error", "Critical error")
