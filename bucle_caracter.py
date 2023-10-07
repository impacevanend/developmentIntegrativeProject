import readchar

def defincion_caracter(caracter):
    bandera = True
    while bandera:
        print(f"Has presionado la tecla: {caracter}")
        caracter = readchar.readkey()
        print(f"Has presionado: {caracter}")
        if caracter == readchar.key.UP:
            bandera = False
    return "Has presionado: Flecha Arriba"

entrada = input("Ingrese una tecla: ")
print(defincion_caracter(entrada))
