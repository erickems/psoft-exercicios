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

listaConexoes = []

def servidor_no_ar(cliente_socket, dados):
    listaConexoes.append((cliente_socket, dados))
    while True:
        mensagem_cliente = cliente_socket.recv(1024)
        mensagem_cliente = mensagem_cliente.decode('utf-8').rstrip() 
        mensagem_editada = '[' + str(dados[0]) + '/' + str(dados[1]) + ']> ' + mensagem_cliente + '\n'       

        if mensagem_cliente == 'BYE':
            cliente_saiu(cliente_socket, dados)
            break

        print('[%s/%s]: %s' % (dados[0], dados[1], mensagem_cliente))

        reprodutor_mensagens(mensagem_editada, cliente_socket)
    threads()

def threads():
    while True:
        cliente, dados = servidor.accept()
        t = threading.Thread(target=servidor_no_ar, args=(cliente, dados))
        t.start()

def reprodutor_mensagens(mensagem, cliente_socket):
    for i in listaConexoes:
        if(i[0] != cliente_socket):
            s = i[0]
            s.send(mensagem.encode())
        else:
            nova_mensagem = mensagem[16:]
            cliente_socket.send(nova_mensagem.encode())

def cliente_saiu(cliente_socket, dados):
    for i in listaConexoes:
        if(i[0] != cliente_socket):
            mensagem_despedida = '[' + str(dados[0]) + '/' + str(dados[1]) + '] SAIU DO SERVIDOR!\n'
            s = i[0]
            s.send(mensagem_despedida.encode())
    listaConexoes.remove(((cliente_socket), dados))
    cliente_socket.close()
        
threads()