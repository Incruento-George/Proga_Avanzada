import parametros as p
import rw_files as rw

from canales import Canal
from barcos import BarcoPasajeros, BarcoCarguero, BarcoBuque
from tripulacion import DCCapitan, DCCarguero, DCCocinero
from mercancia import Mercancia

"""
To make the code easier to read and modularize the program
"""

# Función para crear un objeto de la clase Canal y retornar el objeto
def instanciar_canal(canal_data):
    # Nombre (str), Tamaño (int), Dificultad (str)
    canal = Canal(canal_data[0], int(canal_data[1]), canal_data[2])

    return canal


# Función para crear un objeto de una de las clases que hereda de Barco y retornar el objeto
# Nombre (str), Costo mantención (float), Vel. base (int), Pasajeros (int),
# Carga máxima (int), Moneda (str), Tripulación (list), Carga (list)
def instanciar_barco(barco_data):
    # Se instancian los tripulantes asociados al barco
    tripulantes_obj = []
    for tripulante_nombre in barco_data[7]:
        tripulante = instanciar_tripulante(tripulante_nombre)
        tripulantes_obj.append(tripulante)
    # Se instancian los lotes de mercancía asociados al barco
    mercancias_obj = []
    for mercancia_id in barco_data[8]:
        mercancia = instanciar_mercancia(mercancia_id)
        mercancias_obj.append(mercancia)

    if barco_data[1] == "Pasajero":
        barco = BarcoPasajeros(barco_data[0], float(barco_data[2]), int(barco_data[3]), \
                               int(barco_data[4]), int(barco_data[5]), barco_data[6], \
                                tripulantes_obj, mercancias_obj)
    elif barco_data[1] == "Carguero":
        barco = BarcoCarguero(barco_data[0], float(barco_data[2]), int(barco_data[3]), \
                               int(barco_data[4]), int(barco_data[5]), barco_data[6], \
                                tripulantes_obj, mercancias_obj)
    elif barco_data[1] == "Buque":
        barco = BarcoBuque(barco_data[0], float(barco_data[2]), int(barco_data[3]), \
                               int(barco_data[4]), int(barco_data[5]), barco_data[6], \
                                tripulantes_obj, mercancias_obj)

    return barco


# Función para crear un objeto de una de las clases que hereda de Tripulacion y retornar el objeto
def instanciar_tripulante(nombre):
    tripulantes = rw.cargar_tripulantes()
    trip_data = tripulantes[nombre]

    # Nombre (str), Años de experiencia (int)
    if trip_data[1] == "DCCapitán":
        tripulante = DCCapitan(trip_data[0], int(trip_data[2]))
    elif trip_data[1] == "DCCarguero":
        tripulante = DCCarguero(trip_data[0], int(trip_data[2]))
    elif trip_data[1] == "DCCocinero":
        tripulante = DCCocinero(trip_data[0], int(trip_data[2]))

    return tripulante


# Función para crear un objeto de una de las clases que hereda de Tripulacion y retornar el objeto
def instanciar_mercancia(num_lote):
    mercancias = rw.cargar_mercancia()
    merc_data = mercancias[num_lote]

    # Número de lote (int), Tipo (str), Tiempo de expiración (int), Peso (int)
    mercancia = Mercancia(int(merc_data[0]), merc_data[1], int(merc_data[2]), int(merc_data[3]))

    return mercancia


if __name__ == "__main__":
    #Test 1
    canal_data1 = rw.cargar_canales()["Canal de Panamá"]
    canal1 = instanciar_canal(canal_data1)
    print(canal1.nombre, canal1.largo, canal1.dificultad)
    canal_data2 = rw.cargar_canales()["Canal de Suez"]
    canal2 = instanciar_canal(canal_data2)
    print(canal2.nombre, canal2.largo, canal2.dificultad)
    print()

    # Test 2
    barco_data1 = rw.cargar_barcos()["El Sirenita"]
    barco1 = instanciar_barco(barco_data1)
    print(barco1.nombre, barco1.tipo, barco1.moneda_origen, barco1.tripulacion, barco1.mercancia)
    print(str(barco1.tripulacion[0]) + "-> " + str(barco1.tripulacion[0].experiencia))
    
    barco_data2 = rw.cargar_barcos()["Inferno"]
    barco2 = instanciar_barco(barco_data2)
    print(barco2.nombre, barco2.tipo, barco2.moneda_origen, barco2.tripulacion, barco2.mercancia)
    print(str(barco2.tripulacion[1]) + "-> " + str(barco2.tripulacion[1].experiencia))
    print()