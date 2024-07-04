import socket
import threading as td
import json
import sys

cred = {
    "name":"rahul",
    "type":None,
    "host":"localhost",
    "port":1728 
}



def reciveD(cl):
    global tk
    if tk:
        while 1:
            data:str = cl.recv(1024).decode() 
            print(f"\n{con_cred['Server']['name']}:"+str(data))
 

tk = False
def sendD(cl):
    while True:
        mes  = input(f"{cred['name']}>")
        if mes == "end":
            global tk
            tk = True
            cl.shutdown(1)
            break
        cl.send(mes.encode())


def main():
    global client
    client = socket.socket()
    client.connect((cred["host"],cred["port"]))
    client.send(json.dumps(cred).encode())
    global con_cred
    con_cred = json.loads(client.recv(1024))
    print(f"Client as connected waiting for Approval from {con_cred['Server']['name']}......")
    while True:
        app = client.recv(1024).decode()
        if app == "Approved":
            print("Connection Approved")
            t2 = td.Thread(target = sendD,args=(client,))
            t = td.Thread(target = reciveD,args=(client,))
            t.start()
            t2.start()
            break


if __name__ == "__main__":
    main()