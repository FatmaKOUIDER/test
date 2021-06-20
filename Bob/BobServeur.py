#!/usr/bin/python3

import os,socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',8070)) #num port
s.listen(1)
connexion, tsap_client = s.accept() #connexion avec le client
print(tsap_client)

pid = os.fork()

if not pid: 
	while 1:
		ligne = connexion.recv(1024) #lecture du client 
		print(str(ligne,'utf-8'))
else: 
	while 1:
		saisie = input('>')
		connexion.sendall(bytes(saisie,'utf-8'))
s.close()
