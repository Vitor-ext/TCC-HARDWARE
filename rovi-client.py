### Autor: Vitor de Jesus ###
   ### Projeto: ROVI-BR ###
       ### TCC DS ###

import socket

host = "127.0.0.1"  # server address
port = 1235  #server port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


Var = str(0)

s.send(Var.encode())
dados = s.recv(1024)
print('Mensagem do Servidor:', dados.decode())
s.close

#s = imagem.shape   #Caso queira utilizar o tamanho da imagem