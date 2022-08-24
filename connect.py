import sys
import socket
from time import sleep

ip = '10.10.10.34'
port = 7411
username = "admin"
password = "1974jailbreak!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

def authenticate():

    print(sock.recv(1024).decode('utf-8'))
    sock.send(bytes(f"USER {username}", 'utf-8'))
    print(sock.recv(1024).decode('utf-8'))
    sock.send(bytes(f"PASS {password}", 'utf-8'))
    print(sock.recv(1024).decode('utf-8'))

def exec_cmds():
    while True:
        cmd = input('>')
        sock.send(bytes(cmd, 'utf-8'))
        res = sock.recv(1024).decode('utf-8')
        print(res)

        if cmd == 'q' or cmd == 'quit':
            return
        elif "invalid command" in res.lower():
            sock.close()
            connected = False

            while not connected:
                try:
                    sock.connect((ip, port))
                    connected = True
                    print('Successfully reconnected')
                except socket.error:
                    print('reconnecting...')
                    sleep(2)
                
            authenticate()

authenticate()
exec_cmds()
