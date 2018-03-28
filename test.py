from subprocess import Popen, PIPE
import time
import os

emulator = {
'A': b'keydown J\nkeyup J\n',
'B': b'key K\n',
'UP': b'key W\n',
'DOWN': b'key D\n',
'LEFT': b'key A\n',
'RIGHT': b'key S\n'
}

file_name = "/home/hanit/VBA-M/Code/IIITD_Plays_Pokemon/file.txt"

# a = 'key A\n'

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

# keypress(emulator['A'])

# with open("/home/hanit/VBA-M/Code/IIITD_Plays_Pokemon/file.txt", "r") as f:
# 	while(True):
# 		for line in f:
# 			try:
# 				keypress(emulator[line])
# 				print('x')
# 				print(line)
# 				print(emulator[line])
# 				print('y')
# 			except:
# 				pass

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
        # 	keypress(emulator[line])
        # 	print(emulator[line])
        # except:
        # 	pass


def follow(name):
    current = open(name, "r")
    curino = os.fstat(current.fileno()).st_ino
    while True:
        while True:
            line = current.readline()
            if not line:
                break
            yield line

        try:
            if os.stat(name).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
        time.sleep(1)


if __name__ == '__main__':
    fname = file_name
    for l in follow(fname):
    	try:
    		keypress(emulator[l])
    		print(emulator[l])
    	except:
    		pass