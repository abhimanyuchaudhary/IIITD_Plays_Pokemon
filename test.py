from subprocess import Popen, PIPE
import time
import os

emulator = {
'A': b'key J\n',
'B': b'key K\n',
'UP': b'key W\n',
'DOWN': b'key D\n',
'LEFT': b'key A\n',
'RIGHT': b'key S\n'
}

emulator_down = {
'A': b'keydown J\n',
'B': b'keydown K\n',
'UP': b'keydown W\n',
'DOWN': b'keydown S\n',
'LEFT': b'keydown A\n',
'RIGHT': b'keydown D\n'
}

emulator_up = {
'A': b'keyup J\n',
'B': b'keyup K\n',
'UP': b'keyup W\n',
'DOWN': b'keyup S\n',
'LEFT': b'keyup A\n',
'RIGHT': b'keyup D\n'
}

file_name = "/home/hanit/VBA-M/Code/IIITD_Plays_Pokemon/file.txt"

def keypress(sequence):
        p = Popen(['xte'], stdin=PIPE)
        # pyautogui.press(sequence)
        p.communicate(input=sequence)

with open(file_name, "r") as f:
    while(True):
        for line in f:
            try:
                    print(line)
                    keypress(emulator_down[line])
                    time.sleep(0.1)
                    keypress(emulator_up[line])
            except:
                    pass