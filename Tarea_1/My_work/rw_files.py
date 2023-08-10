import parametros as p

"""
File dedicated to loading data from the database in CSV files

The data is only loaded. Class objects are not instantiated
"""

# Carga de datos del archivo barcos.csv para almacenar en un dict:
# Nombre, Tipo, Costo mantención, Vel. base, Pasajeros, Carga máxima, Moneda, Tripulación, Carga
def cargar_barcos():
    barcos = dict()
    with open(p.PATH_BARCOS, "r", encoding="UTF-8") as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            data[7] = data[7].split(";")        # Tripulantes
            data[8] = data[8].split(";")        # Mercancía
            barcos[data[0]] = data

    return barcos


# Carga de datos del archivo canales.csv para almacenar en un dict:
# Nombre, Tamaño, Dificultad
def cargar_canales():
    canales = dict()
    with open(p.PATH_CANALES, "r", encoding="UTF-8") as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            canales[data[0]] = data
    
    return canales


# Carga de datos del archivo tripulantes.csv para almacenar en un dict:
# Nombre, Tipo, Años de experiencia
def cargar_tripulantes():
    tripulantes = dict()
    with open(p.PATH_TRIPULANTES, "r", encoding="UTF-8") as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            tripulantes[data[0]] = data

    return tripulantes


# Carga de datos del archivo mercancia.csv para almacenar en un dict:
# Lote, Tipo, Tiempo de expiración, Peso
def cargar_mercancia():
    mercancia = dict()
    with open(p.PATH_MERCANCIAS, "r", encoding="UTF-8") as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            mercancia[data[0]] = data

    return mercancia


if __name__ == "__main__":
    # Test 1
    barcos = cargar_barcos()
    print(barcos["El Sirenita"])
    print(barcos["Inferno"])
    print(barcos["Aguamarina"])
    print()

    # Test 2
    canales = cargar_canales()
    print(canales)
    print()

    # Test 3
    tripulantes = cargar_tripulantes()
    print(tripulantes["Megan Sanders"])
    print(tripulantes["Samantha Hernandez"])
    print(tripulantes["Mr. Eduardo Johnson"])
    print()

    # Test 4
    mercancia = cargar_mercancia()
    print(mercancia["13"])
    print(mercancia["72"])
    print(mercancia["150"])
    print()