"""mario bros en ascii art 
hecho por jorge flores ari"""
import random
import string


def cielo(arg):
    print("\x1b[1;37;46m"+arg,end="")
def piel(arg):
    print("\x1b[1;31;43m"+arg,end="")
def ropaR(arg):
    print("\x1b[1;41m"+arg,end="")
def ropaV(arg):
    print("\x1b[1;30;42m"+arg,end="")

pix = [12,10,6,6,6,0,11,10,6,6,0,0,0,1,1,1,11,10,6,0,7,0,0,1,1,1,11,10,6,7,2,2,2,2,1,1,11,10,
        6,3,3,3,1,1,3,1,0,3,3,3,11,10,0,0,0,0,3,1,3,1,1,1,3,1,0,3,3,3,11,10,
        0,0,0,0,3,1,3,3,1,1,1,3,1,1,1,3,11,10,0,0,0,0,3,3,1,1,1,1,4,0,11,10,
        6,0,1,1,1,1,1,1,1,3,0,0,11,10,0,0,4,2,3,3,3,2,3,0,0,0,11,10,
        0,4,3,3,2,3,3,3,2,0,0,3,11,10,1,1,4,3,7,0,0,3,11,10,
        1,1,1,0,2,2,3,2,2,1,2,2,1,2,3,3,11,10,0,1,0,3,7,7,3,3,11,10,
        0,0,3,3,3,7,2,2,2,2,3,3,11,10,0,3,3,3,7,2,2,6,11,10,0,3,0,0,2,2,2,2,6,0,0,0,11,10,
        6,6,6,0,11,12]

for k in pix:
#fondo azul con letras blancas al azar    
    if k == 0:
        for i in range(2):
            a = random.choice(string.ascii_letters)
            cielo(a)
    elif k == 6:
        for i in range(10):
            a = random.choice(string.ascii_letters)
            cielo(a)
#demas colores
    elif k == 1: 
        piel("oo")
    elif k == 7:
        ropaR("          ")
    elif k == 2:
        ropaR("  ")
    elif k == 3:
        ropaV("##")
    elif k == 4:
        ropaV("##########")
#borde izquierdo (5 caracteres)
    elif k == 10:
        print("*",end='')
        for i in range(4):
            a = random.choice(string.ascii_letters)
            cielo(a)
#borde derecho (5 caracteres)
    elif k == 11:
        for i in range(4):
            a = random.choice(string.ascii_letters)
            cielo(a)
        print('\x1b[0;m'+"*")
#asteriscos de arriba y abajo
    elif k == 12:
        for i in range(20):
            print("* ",end='')
        print("*") 
