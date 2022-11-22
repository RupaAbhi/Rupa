import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear',shell=True)
remoteServer = input("enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print(" " *60)
print("please wait,scanningremote host",remoteServerIP)
print("_" *60)
t1 = datetime.now()
try:
	for port in range(1,5000):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=sock.connect_ex((remoteServerIP,port))
		if result ==0:
			print("port {}:			open".format(port))
			sock.close()
except KeyboardInterrupt:
	 print("row pressed ctrl+c")
	 sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.Exiting")
	sys.exit()
except socket.error:
	print("couldn't connect to server")
	sys.exit()