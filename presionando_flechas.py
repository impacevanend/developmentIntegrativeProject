import readchar
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print("".join(fila))
    print()

def main_loop(mapa, inicio, final):
    px, py = inicio
    while (px, py) != final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'
        movimiento = readchar.readkey()
        if movimiento == readchar.key.UP:  # Arriba
            if mapa[px-1][py] == '.':
                px -= 1
        elif movimiento == readchar.key.DOWN:  # Abajo
            if mapa[px+1][py] == '.':
                px += 1
        elif movimiento == readchar.key.RIGHT:  # Derecha
            if mapa[px][py+1] == '.':
                py += 1
        elif movimiento == readchar.key.LEFT:  # Izquierda
            if mapa[px][py-1] == '.':
                py -= 1

laberinto = """
###################
..#.........#.......#
#.#.###.#.#.#####.###
#...#...#.#.......#.#
#####.#####.#.###.#.#
#.#...#.....#...#.#.#
#.###.#######.#####.#
#.....#.....#...#...#
#.#######.#.#.#.###.#
#.#.....#.#...#.....#
#.#.#######.#####.###
#.......#.....#.#...#
#.#########.#.#.###.#
#...#.......#.#...#.#
#.#########.#.###.###
#.....#.....#.#.....#
#.#####.#####.#.#####
#.....#.....#.#.#...#
#########.###.#.#.###
#...........#.......#
###################
"""

def convertir_mapa(laberinto):
    return [list(fila) for fila in laberinto.split("\n") if fila]

mapa = convertir_mapa(laberinto)
inicio = (1, 0)
final = (len(mapa) - 2, len(mapa[0]) - 1)

main_loop(mapa, inicio, final)