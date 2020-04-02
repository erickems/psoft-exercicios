#coding: utf-8
#UFCG - Ciência da Computação
#Erick Morais de Sena - github.com/erickems

import threading
import socket

ip = 'localhost'
porta = 9090

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, porta))
servidor.listen()

def servidor_no_ar(cliente_socket, dados):
    while True:
        mensagem_cliente = cliente_socket.recv(1024)
        mensagem_cliente = mensagem_cliente.decode('utf-8').rstrip()

        if mensagem_cliente == 'FIM':
            cliente_socket.close()
            break
        print('[%s/%s]: %s' % (dados[0], dados[1], mensagem_cliente))
        mensagem_editada = '> ' + mensagem_cliente + '\n'
        cliente_socket.send(mensagem_editada.encode())
    threads()

def threads():
    while True:
        cliente, dados = servidor.accept()
        t = threading.Thread(target=servidor_no_ar, args=(cliente, dados))
        t.start()

threads()