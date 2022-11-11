#!/usr/bin/env python3
import socket

TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = '0.0.0.0'       # IP de alguma interface do Servidor
PORT = 40000           # Porta que o Servidor escuta

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
while True:
    try:
        con, cliente = sock.accept()
    except: break
    print('Cliente conectado', cliente)
    msg = con.recv(TAM_MSG)
    if msg:
        nomeArq = msg.decode()
        print('Arquivo solicitado:', nomeArq)
        arq = open(nomeArq, "rb")
        while True:
            dados = arq.read(TAM_MSG)
            if not dados: break
            con.send(dados)
    con.close()
sock.close()
