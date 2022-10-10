from jsonschema import validate


# la forma que debe tener el archivo json
JSON_SCHEMA: dict = {
        "type" : "object",
        "properties" : {
            "player1" : {
                "type" : "object",
                "properties": {
                    "movimientos": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "golpes": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            },
            "player2" : {
                "type" : "object",
                "properties": {
                    "movimientos": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "golpes": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            },
        },
    }

def todo_mayucula(pelea: dict) -> dict:  # Retorna la pelea con todos los movimientos y golpes en mayúscula
    for i in range(len(pelea["player1"]["movimientos"])):
        pelea["player1"]["movimientos"][i] = pelea["player1"]["movimientos"][i].upper()
    for i in range(len(pelea["player1"]["golpes"])):
        pelea["player1"]["golpes"][i] = pelea["player1"]["golpes"][i].upper()
    for i in range(len(pelea["player2"]["movimientos"])):
        pelea["player2"]["movimientos"][i] = pelea["player2"]["movimientos"][i].upper()
    for i in range(len(pelea["player2"]["golpes"])):
        pelea["player2"]["golpes"][i] = pelea["player2"]["golpes"][i].upper()
    return pelea