import parametros as p
from random import random
from abc import ABC, abstractmethod

"""
This file only contains definitions of classes related with Barcos

Barcos --> Tipos: de pasajeros, carguero, buque
"""

# Clase abstracta de la que herederán todos los tipos de barcos
class Barcos(ABC):

    def __init__(self, nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc):
        # ATRIBUTOS BÁSICOS COMÚN ENTRE TODOS LOS TIPOS DE BARCOS
        self.nombre = nombre                            # str
        self.costo_mantencion = costo_m                 # float
        self.vel_base = vel_b                           # int
        self.pasajeros = pasajeros                      # int
        self.carga_max = carga_max                      # int
        self.moneda = moneda                            # str
        self.tripulacion = trip                         # list [class Tripulacion]
        self.mercancia = merc                           # list [class Mercancia]

        # ATRIBUTOS EXTRAS PARA DESARROLLO DE SIMULACIÓN
        self.posicion = 0               # Desplazamiento total del barco
        self.encallado = False          # Estado actual del barco en el canal
        self.poder_capitan = 0          # Cantidad de efectos especiales tipo DCCapitan acumulados
        self.evento_done = False        # Ocurrencia del evento especial del barco
        self.tiempo_detenido = 0

    # El barco avanza a lo largo del canal a una nueva posición SI ES QUE NO ESTÁ ENCALLADO
    # Si un barco adelante de este está encallado, no puede avanzar más allá del barco encallado 
    def desplazarse(self):
        peso_total_merc = 0                             # Peso total de la mercancía
        for caja in self.mercancia:
            peso_total_merc += caja.peso

        ratio = (self.carga_max - peso_total_merc - 0.3 * self.pasajeros) / self.carga_max
        value_min = min(1, ratio)
        desplazamiento = max(0.1, value_min) * self.vel_base    # En kilómetros
        self.posicion += desplazamiento

        # Verificación de si el barco salió del canal se realiza fuera de esta clase
        return self.posicion

    # Se calcula y retorna el riesgo de que el barco encalle
    def calcular_riesgo(self, dif_canal):
        peso_total_merc = 0                             # Peso total de la mercancía
        for caja in self.mercancia:
            peso_total_merc += caja.peso

        exp_total_tripulacion = 0                       # Experiencia total de la tripulación
        for tripulante in self.tripulacion:
            exp_total_tripulacion += tripulante.experiencia

        ratio = (self.vel_base + peso_total_merc - exp_total_tripulacion) / 120
        if dif_canal == "principiante":
            ponderador = p.PONDERADOR_PRINCIPIANTE
        else:
            ponderador = p.PONDERADOR_AVANZADO
        prob_encallar = min(1, ratio) * self.tend_encallar * ponderador

        return prob_encallar

    # En cada iteración de la simulación, el barco sufre el riesgo de encallar en el canal
    # Al estar encallado, el barco no puede desplazarse ni gatillar su evento especial
    def encallar(self, dif_canal):
        prob_encallar = self.calcular_riesgo(dif_canal)
        print(f"La probabilidad del barco {self.nombre} es de {prob_encallar * 100}%")

        # No ocurre el encallamiento del barco
        if random() > prob_encallar:
            print(f"El barco {self.nombre} no ha encallado y podrá seguir su camino\n")
            return False
        # El barco encalla bloqueando el canal
        else:
            print(f"¡El barco {self.nombre} ha encallado bloqueando el canal!\n")
            if self.poder_capitan > 0:
                print("Gracias al DCCapitán del barco, este fue desencallado automáticamente\n")
                self.poder_capitan -= 1
                return False
            self.encallado = True
            return True

    # Método abstracto -> Depende del tipo de barco
    @abstractmethod
    def evento_especial(self):
        pass

    # Efectos especiales de la tripulación se aplican automáticamente
    def tripulacion_efectos(self):
        print(f"Tripulantes del barco {self.nombre} aplicarán sus efectos especiales!\n")
        for tripulante in self.tripulacion:
            print(f"Tripulante {tripulante.nombre} ({tripulante.tipo}) presente!")
            tripulante.efecto_especial()
            
            if tripulante.tipo == "DCCarguero":
                self.carga_max += p.CARGA_EXTRA_CARGUERO
            elif tripulante.tipo == "DCCocinero":
                for merc in self.mercancia:
                    if merc.tipo == "alimentos":
                        merc.tiempo_exp *= 2
            elif tripulante.tipo == "DCCapitán":
                self.poder_capitan += 1

        print("La tripulación comenzará a trabajar de inmediato!\n")
        return True


# Tipo específico de barco - Evento especial: intoxicación de pasajeros -> Pagar al canal
class BarcoPasajeros(Barcos):

    def __init__(self, nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc):
        super().__init__(nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc)
        self.tend_encallar = p.TENDENCIA_ENCALLAR_PASAJEROS
        self.tipo = "Pasajeros"

    # Barco paga al canal DINERO_INTOXICACION por medicinas
    def evento_especial(self):
        # LOS EVENTOS ESPECIALES DE CADA BARCO OCURREN UNA SOLA VEZ POR BARCO
        if self.evento_done:
            return False
        elif not self.encallado:    # Un barco encallado no puede ejecutar su evento especial
            # Evento especial del barco no ocurre en esta iteración
            if random() > p.PROBABILIDAD_EVENTO_ESPECIAL:
                return False
            else:
                self.evento_done = True
                print(f"\n¡Evento especial del barco {self.nombre} ocurriendo!")
                print(f"Los pasajeros del {self.nombre} se han intoxicado y necesitan medicinas")
                print(f"El barco ha pagado {p.DINERO_INTOXICACION} USD al canal por medicamentos")
                return True
        else:
            return False
    

# Tipo específico de barco - Evento especial: ataque de piratas -> No puede pagar tarifa de salida
class BarcoCarguero(Barcos):

    def __init__(self, nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc):
        super().__init__(nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc)
        self.tend_encallar = p.TENDENCIA_ENCALLAR_CARGUERO
        self.tipo = "Carguero"

    # Barco pierde su mercancía por ataque de piratas, sin poder pagar al canal
    def evento_especial(self):
        # LOS EVENTOS ESPECIALES DE CADA BARCO OCURREN UNA SOLA VEZ POR BARCO
        if self.evento_done:
            return False
        elif not self.encallado:    # Un barco encallado no puede ejecutar su evento especial
            if random() > p.PROBABILIDAD_EVENTO_ESPECIAL:
                return False
            else:
                self.evento_done = True
                print(f"\n¡Evento especial del barco {self.nombre} ocurriendo!")
                print(f"El {self.nombre} ha sido atacado por piratas y perdió toda su mercancía")
                print(f"El barco no podrá pagar la tarifa de salida del canal")
                self.mercancia = []
                return True
        else:
            return False
    

# Tipo específico de barco - Evento especial: avería interna -> No se desplaza por X horas
class BarcoBuque(Barcos):

    def __init__(self, nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc):
        super().__init__(nombre, costo_m, vel_b, pasajeros, carga_max, moneda, trip, merc)
        self.tend_encallar = p.TENDENCIA_ENCALLAR_BUQUE
        self.tipo = "Buque"

    # POR IMPLEMENTAR - Barco sufre avería y se detiene por TIEMPO_AVERIA_BUQUE horas
    def evento_especial(self):
        # LOS EVENTOS ESPECIALES DE CADA BARCO OCURREN UNA SOLA VEZ POR BARCO
        if self.evento_done:
            return False
        elif not self.encallado:    # Un barco encallado no puede ejecutar su evento especial
            if random() > p.PROBABILIDAD_EVENTO_ESPECIAL:
                return False
            else:
                self.evento_done = True
                print(f"\n¡Evento especial del barco {self.nombre} ocurriendo!")
                print(f"El barco {self.nombre} sufrió una avería interna y no podrá avanzar")
                print(f"El barco estará detenido por {p.TIEMPO_AVERIA_BUQUE} horas")
                self.tiempo_detenido = p.TIEMPO_AVERIA_BUQUE
                return True