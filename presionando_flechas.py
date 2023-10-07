import readchar

def interpreta_tecla(tecla):
    if tecla == readchar.key.UP:
        return "Flecha Arriba"
    elif tecla == readchar.key.DOWN:
        return "Flecha Abajo"
    elif tecla == readchar.key.LEFT:
        return "Flecha izquierda"
    elif tecla == readchar.key.RIGHT:
        return "Flecha Derecha"
    else:
        return tecla

print("Presiona una tecla:")
caracter = readchar.readkey()
print(f"Has presionado: {interpreta_tecla(caracter)}")


"""
"""
while True:

    print("presiona una tecla:")
    caracter = readchar.readkey()
    print(f"Has presionado: {caracter}")
    if caracter == readchar.key.UP:
        break