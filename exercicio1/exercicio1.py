#coding: utf-8
#UFCG - Ciência da Computação
#Erick Morais de Sena - github.com/erickems

import socket

ip = 'localhost'
porta = 9090

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, porta))
servidor.listen()

def servidor_no_ar():
    cliente, dados = servidor.accept()

    while True:
        mensagem_cliente = cliente.recv(1024)
        mensagem_cliente = mensagem_cliente.decode('utf-8').rstrip()

        if mensagem_cliente == 'FIM':
            cliente.close()
            servidor_no_ar()
        print('[%s/%s]: %s' % (dados[0], dados[1], mensagem_cliente))
        mensagem_editada = '> ' + mensagem_cliente + '\n'
        cliente.send(mensagem_editada.encode())

servidor_no_ar()