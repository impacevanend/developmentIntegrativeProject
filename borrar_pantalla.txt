import os
import readchar

def borrarYImprimir(numero):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(numero)

def funcionPrincipal():
    numero = 0
    while numero <= 50:
        tecla = readchar.readchar()  
        if tecla == 'n':
            numero += 1
            borrarYImprimir(numero)

funcionPrincipal()