#!/usr/bin/python3

import random
import subprocess
import re

random.seed()
def GeneratePrimeNumber():
    while True:
        #choose a number random from  a list
        num = random.choice('1379')
        #check if the number choosen is prime or not with openssl
        commande = "openssl prime "
        r  = subprocess.run(commande+str(num),shell=True,stdout=subprocess.PIPE) 
        resultat_openssl = r.stdout

        #use regular expression ("is prime")
        regexp = re.compile(r'is prime')
        #look for "is prime" into the string resultat_openssl
        #if True break the while boucle
        if regexp.search(str(resultat_openssl)):
            break
    return num

p = GeneratePrimeNumber()
q = GeneratePrimeNumber()

print(str(p)," - ",str(q))
