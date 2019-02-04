#!/usr/bin/python3
import socket 
import select 
import sys,os
from _thread import *
gw = os.popen("ip -4 route show default").read().split()
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.connect((gw[2], 0))
ipaddr = sk.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()

print("Welcome to Ezzat's Chat Server Side\n")






server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

	

IP_address = ipaddr



server.bind((IP_address, 4444)) 

server.listen(100) 
print("Server is up")
print("Server Name : %s\nHost : %s"%(host,ipaddr))

list_of_clients = [] 

def clientthread(conn, addr): 

	conn.send("Welcome to this chatroom!".encode()) 

	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 

					print(message.decode())

					# Calls broadcast function to send message to all 
					message_to_send = "<%s> %s"%("SERVER",message.encode())
					broadcast(message_to_send, conn) 

				else: 
					
					remove(conn) 

			except: 
				continue

def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message.encode()) 
			except: 
				clients.close() 

				remove(clients) 
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 

	conn, addr = server.accept() 
	list_of_clients.append(conn) 

	print(addr[0] + " is on")

	
	start_new_thread(clientthread,(conn,addr))

conn.close() 
server.close() 
