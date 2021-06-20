#!/usr/bin/python3

import os,socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsap_serveur = ('127.0.0.1',8080)
#tsap_serveur = ('smtp.unilim.fr',25)
#tsap_serveur = ('agate.unilim.fr',22)

s.connect(tsap_serveur)

pid = os.fork()

if not pid:
    #enfant
	while 1:
		entree_clavier = input()
		if not entree_clavier:
			break
		s.sendall(bytes(entree_clavier,'utf-8'))
else:
	while 1:
		ligne = s.recv(1024)
		if not ligne:
			break
		print(str(ligne, 'utf-8'))
s.close()
