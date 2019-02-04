import socket,select,sys,time
print("Welcome to Ezzat's Chat Client Side\n")
print("Enter Host ip and your name in separated lines\n")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter Server Host ip :")
name = input("Enter your name : ")

server.connect((host,4444))
def send():
    server.send(("<%s> %s"%(name,message)).encode())
while True: 

	sockets_list = [sys.stdin, server] 

	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print(message.decode())
		else: 
			message = sys.stdin.readline() 
			send()

			sys.stdout.write(message)
			sys.stdout.flush() 
server.close() 
