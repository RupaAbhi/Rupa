#import os
#print (os.system("ipconfig"))
import socket
hostname = socket.gethostname()
ipadd = socket.gethostbyname(hostname)
print (ipadd)

