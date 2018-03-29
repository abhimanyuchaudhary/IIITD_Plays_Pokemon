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

# a = 'key A\n'

def keypress(sequence):
        p = Popen(['xte'], stdin=PIPE)
        # pyautogui.press(sequence)
        p.communicate(input=sequence)

# keypress(emulator['A'])

with open(file_name, "r") as f:
    while(True):
        # while (not os.path.isfile(file_name)):
        #     continue

        for line in f:
            try:
                    print(line)
                    keypress(emulator_down[line])
                    time.sleep(0.1)
                    keypress(emulator_up[line])
                    # keypress(emulator_up[line])
                    # keypress(emulator_up[line])
            except:
                    pass

# def follow(thefile):
#     thefile.seek(0,2)
#     while True:
#         line = thefile.readline()
#         if not line:
#             time.sleep(0.01)
#             continue
#         yield line

# if __name__ == '__main__':
#     logfile = open("/home/hanit/VBA-M/Code/IIITD_Plays_Pokemon/file.txt", "r")
#     loglines = follow(logfile)
#     for line in loglines:
                # try:
                #   keypress(emulator[line])
                #   print(emulator[line])
                # except:
                #   pass


# def follow(name):
#     while (not os.path.isfile(name)):
#         continue
                
#     current = open(name, "r")
#     curino = os.fstat(current.fileno()).st_ino
#     while True:
#         while True:
#             line = current.readline()
#             if not line:
#                 break
#             yield line

#         try:
#             if os.stat(name).st_ino != curino:
#                 new = open(name, "r")
#                 current.close()
#                 current = new
#                 curino = os.fstat(current.fileno()).st_ino
#                 continue
#         except IOError:
#             pass
#         time.sleep(1)


# if __name__ == '__main__':
#     fname = file_name
        
#     for l in follow(fname):
#         # try:
#         print(l)
#         keypress(l)
#         if os.path.isfile(file_name):
#             os.remove(file_name)
#             # keypress(emulator[l])
#         # except:
#             # pass