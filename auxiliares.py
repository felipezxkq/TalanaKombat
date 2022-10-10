import json
import sys
from jsonschema import validate
import validaciones


def leer_json():    
    valido = False
    while not valido:
        print("Por favor ingrese la pelea en formato json")
        pelea = input()
        pelea = pelea.replace('“', '"').replace('”', '"')
        try:
            json_data = json.loads(pelea)
            #validate(instance=json_data, schema=validaciones.JSON_SCHEMA)
            valido = True
        # show the exception error
        except Exception as e:
            print("Formato de json incorrecto! vuelva a intentarlo")
            print(pelea)
            print(e)
    json_data = validaciones.todo_mayucula(json_data)
    return json_data

def validacion_pelea(pelea: dict) -> bool:  # Retorna True si la pelea es válida, False si no lo es
    
    golpes_posibles = ['P', 'K']

def read_json_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

def quien_parte(pelea: dict) -> str:  # Retorna "Tonyn" o "Arnaldor" dependiendo de quién parte
    movimientos_p1 = 0
    movimientos_p2 = 0
    golpes_p1 = 0
    golpes_p2 = 0

    for i in pelea['player1']['movimientos']:
        movimientos_p1 += len(i)
    
    for i in pelea['player2']['movimientos']:
        movimientos_p2 += len(i)

    for i in pelea['player1']['golpes']:
        golpes_p1 += len(i)

    for i in pelea['player2']['golpes']:
        golpes_p2 += len(i)
    
    total_p1, total_p2 = movimientos_p1 + golpes_p1, movimientos_p2 + golpes_p2

    if movimientos_p1 + golpes_p1 > movimientos_p2 + golpes_p2:
        return "Arnaldor"
    elif total_p1 == total_p2 and movimientos_p1 > movimientos_p2:
        return "Arnaldor"
    elif total_p1 == total_p2 and movimientos_p1 == movimientos_p2 and golpes_p1 > golpes_p2:
        return "Arnaldor"
    else:
        return "Tonyn"

def lectura_movimiento_tonyn(movimiento: str, golpe: str):  # Retorna una tupla con la narración y el daño del movimiento
    direcciones = ['W', 'S', 'A', 'D']

    if movimiento == "DSD" and golpe == "P":
        return "Tonyn conecta un Taladoken", 3
    elif movimiento == "SD" and golpe == "K":
        return "Tonyn conecta un Remuyuken", 2
    elif movimiento in direcciones and (golpe == "K" or golpe == "P"):
        if movimiento == "W":
            mov = "Tonyn salta"
        elif movimiento == "S":
            mov = "Tonyn se agacha"
        elif movimiento == "A":
            mov = "Tonyn retrocede"
        elif movimiento == "D":
            mov = "Tonyn avanza"
        if golpe == "K":
            return mov+" y pega una patada", 1
        else:
            return mov+" y pega un puñetazo", 1

    elif movimiento == "":
        if golpe == "P":
            return "Tonyn conecta un puñetazo", 1
        elif golpe=="K":
            return "Tonyn conecta una patada", 1    
    elif movimiento != "":
        if golpe == "":
            return "Tonyn se mueve", 0
        elif golpe == "K":
            return "Tonyn se mueve y conecta una patada", 1
        elif golpe == "P":
            return "Tonyn se mueve y conecta un puñetazo", 1
    else:  # Se asume que si el golpe es vacío o no es K ni P ni combo, entonces el personaje no se mueve
        return "Tonyn se queda quieto", 0

def lectura_movimiento_arnaldor(movimiento: str, golpe: str):
    direcciones = ['W', 'S', 'A', 'D']

    if movimiento == "ASA" and golpe == "P":
        return "Arnaldor conecta un Taladoken", 2
    elif movimiento == "SA" and golpe == "K":
        return "Arnaldor conecta un Remuyuken", 3    
    elif movimiento in direcciones and (golpe == "K" or golpe == "P"):
        if movimiento == "W":
            mov = "Arnaldor salta"
        elif movimiento == "S":
            mov = "Arnaldor se agacha"
        elif movimiento == "A":
            mov = "Arnaldor avanza"
        elif movimiento == "D":
            mov = "Arnaldor retrocede"

        if golpe == "K":
            return mov+" y pega una patada", 1
        else:
            return mov+" y pega un puñetazo", 1

    elif movimiento == "":
        if golpe == "P":
            return "Arnaldor conecta un puñetazo", 1
        elif golpe == "K":
            return "Arnaldor conecta una patada", 1
    elif movimiento != "":
        if golpe == "":
            return "Arnaldor se mueve", 0
        elif golpe == "K":
            return "Arnaldor se mueve y conecta una patada", 1
        elif golpe == "P":
            return "Arnaldor se mueve y conecta un puñetazo", 1
    else:  # Se asume que si el golpe es vacío o no es K ni P ni combo, entonces el personaje no se mueve
        return "Arnaldor se queda quieto", 0


    