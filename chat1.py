import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = input("\n\t\tEnter Your IP : ")
port = 5678

s.bind( (ip,port) )

server_ip = input("\n\t\tEnter Server IP : ")
server_port = 1234

print()

def send():

    while True:
        os.system('tput setaf 5')
        msg = input('\n').encode()
        s.sendto(msg,(server_ip,server_port))
        if msg.decode() == "exit":
            os._exit(1)
        
def recv():
    while True:
        os.system('tput setaf 2')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
            os._exit(1)
        
        print('\n\t\t\t\t\t\t\t'+ server_ip +':'+msg[0].decode())
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()
