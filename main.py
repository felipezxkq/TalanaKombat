import json
import sys
import auxiliares

# Talana challenge



def main():
    pelea = auxiliares.leer_json()
    quien_parte = auxiliares.quien_parte(pelea)
    player_energies = [6, 6]  # Energías de Tonyn y Arnaldor  
    
    print("La pelea comienza!!!\n")

    if quien_parte == "Tonyn":
        for mov in range(0, len(pelea['player2']['movimientos'])):
            if checkea_estado_de_pelea('player1', mov, pelea, player_energies):
                return
            if checkea_estado_de_pelea('player2', mov, pelea, player_energies):
                return
    else:  # parte Arnaldor
        for mov in range(0, len(pelea['player1']['movimientos'])):
            if checkea_estado_de_pelea('player2', mov, pelea, player_energies):
                return
            if checkea_estado_de_pelea('player1', mov, pelea, player_energies):
                return
    print("Ha ganado Tonyn por ser el hermano mayor! Felicitaciones!")


# Retorna verdadero si la pelea ha terminado
def checkea_estado_de_pelea(jugador: str, num_movimiento: int, pelea: dict, player_energies: list)-> bool:  
    if num_movimiento < len(pelea[jugador]['movimientos']):
        if jugador == "player1":
            lectura, damage = auxiliares.lectura_movimiento_tonyn(pelea[jugador]['movimientos'][num_movimiento], 
            pelea[jugador]['golpes'][num_movimiento])
            print(lectura)
            player_energies[1] -= damage
            if player_energies[1] <= 0:
                print("Tonyn gana y aun le queda "+str(player_energies[0])+" de energia")
                return True
        else:
            lectura, damage = auxiliares.lectura_movimiento_arnaldor(pelea[jugador]['movimientos'][num_movimiento],
            pelea[jugador]['golpes'][num_movimiento])
            print(lectura)
            player_energies[0] -= damage
            if player_energies[0] <= 0:
                print("Arnaldor gana y aun le queda "+str(player_energies[1])+" de energia")
                return True
    return False

if __name__ == "__main__":
    main()





    


    