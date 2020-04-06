#coding: utf-8
#UFCG - Ciência da Computação
#Erick Morais de Sena - github.com/erickems

import socket
import threading

	
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((('localhost'), 9090))

def envia_mensagem():
	while True:
		msg = str(input(''))

		if (msg == 'BYE'):
			cliente.send(msg.encode())
			mensagem_server = cliente.recv(1024).decode('utf-8').rstrip()
			print(mensagem_server)
			cliente.close()
			break
		cliente.send(msg.encode())

t1 = threading.Thread(target=envia_mensagem, args=())
t1.daemon = True
t1.start()

while True:
	mensagem_servidor = cliente.recv(1024).decode('utf-8').rstrip()
	if len(mensagem_servidor) < 0:
		break
	else:
		print(mensagem_servidor)	

	