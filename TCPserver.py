import socket
import threading
import time
import json
from colorama import Fore
from RSree import RunNs

Server_cred = {
    "name":"Server"
}

server = socket.socket()
server.bind(("localhost",1728))
server.listen(3)
print("Server Started....")
clients = {}


def clientCon():
    while True:
        ob,add = server.accept()
        revdata = json.loads(ob.recv(1024).decode())
        ob.send(json.dumps({
            "Server":Server_cred,
            "Conn":add,
        }).encode())
        clients[revdata['name']] = (add,ob)
        ob.send(f"Welcome to R's Server {revdata['name']}".encode())


t = threading.Thread(target=clientCon)
tk = False


def sendD(cl):
    while True:
        mes  = input(f"{Server_cred['name']}>")
        clients[cl][1].send(mes.encode())
        if mes == "end":
            global tk
            clients[cl][1].shutdown(1)
            clients.pop(cl)
            tk = True
            break
        
        
def reciveD(cl):
    global tk
    if tk:
        while True:
            data = clients[cl][1].recv(1024).decode()
            print(f"\n{cl}:"+data)
        



def Bash():
    while True:
        command = input("/")
        if command == "lc":
            for _ in enumerate(clients.keys()):
                print(f"{_[0]+1}.{_[1]}")
        elif "connect" in command:
            ar = command.split()
            clients[ar[1]][1].send(b"Approved")
            print(f"Connected.....")
            rt = threading.Thread(target=reciveD,args=(ar[1],))
            rt.start()
            sendD(ar[1])
            

            
        else:
            print(Fore.LIGHTRED_EX+"Input command is not recognized",end=Fore.WHITE+"\n")
            
            

                
t2 = threading.Thread(target=Bash)



if __name__ == "__main__":
    t.start()
    t2.start()

