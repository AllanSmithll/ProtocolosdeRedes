#!/usr/bin/env python3
import socket
import sys

TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = '127.0.0.1'     # IP do Servidor
PORT = 40000           # Porta que o Servidor escuta

if len(sys.argv) > 1:
    HOST = sys.argv[1]
print('Servidor:', HOST+':'+str(PORT)) 
serv = (HOST, PORT)
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(serv)
    print('Para sair use CTRL+D\n')
    try:
        nomeArq = input('Arquivo: ')
    except: break
    sock.send(str.encode(nomeArq))
    print('Recebendo:', nomeArq)
    arq = open(nomeArq, "wb")
    while True:
        dados = sock.recv(TAM_MSG)
        if not dados: break
        arq.write(dados)	
    sock.close()
