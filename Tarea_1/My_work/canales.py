import sys
import parametros as p
import rw_files as rw
import instanciador as inst
from random import random

"""
This file only contains definitions of classes related with Canal

Canal --> Entidad principal del programa y que interactúa con el resto de los objetos
"""

class Canal():

    def __init__(self, nombre, largo, dificultad):
        # ATRIBUTOS BÁSICOS COMÚN PARA TODAS LOS CANALES
        self.nombre = nombre                            # str
        self.largo = largo                              # int
        self.dificultad = dificultad                    # str
        self.barcos = []                                # list [class Barco]
        self.__dinero = p.DINERO_INICIAL                # float (USD)

        # ATRIBUTOS AGREGADOS PARA EL DESARROLLO DE LA SIMULACIÓN
        self.barcos_nombres = []                        # list [str: nombres de los barcos]
        self.fin_sim = False                            # bool -> Marca el fin de la simulación
        self.horas_sim = 0                              # int -> Horas simuladas
        self.dinero_recibido = 0                        # int -> Dinero ganado
        self.dinero_gastado = 0                         # int -> Dinero gastado
        self.num_barcos_idos = 0                        # int -> Número de barcos que han pasado
        self.num_barcos_encallados = 0                  # int -> Número de barcos que han encallado
        self.num_eventos_ocurridos = 0                  # int -> Número de eventos especiales

        # Atributos que dependen de la dificultad del canal
        if self.dificultad == "principiante":
            # El costo de salida que paga un barco al canal al salir | int (USD)
            self.costo_uso = p.COBRO_USO_PRINCIPIANTE
            # La probabilidad de éxito de desencallar un barco posee un ponderador
            self.pond_desencallar = p.PONDERADOR_PRINCIPIANTE
        else:
            # El costo de salida del canal depende de su dificultad | int (USD)
            self.costo_uso = p.COBRO_USO_AVANZADO
            # La probabilidad de éxito de desencallar un barco posee un ponderador
            self.pond_desencallar = p.PONDERADOR_AVANZADO

    # El dinero del canal no puede ser menor a cero
    @property
    def dinero(self):
        return self.__dinero

    # Si no tiene suficiente dinero, termina la simulación
    @dinero.setter
    def dinero(self, value):
        if self.__dinero + value < 0:
            print("\nEl canal ya no cuenta con dinero suficiente! Finalizando simulación ...\n")
            self.fin_sim = True
            sys.exit()
        else:
            self.__dinero = value

    # Se selecciona un barco no presente en el canal | Máx. 1 por hora
    def ingresar_barco(self):
        barcos = rw.cargar_barcos()
        print("Aquí tienes una lista de los barcos que pueden ingresar al canal:\n")

        i = 0
        for barco_nombre in barcos.keys():
            if barco_nombre in self.barcos_nombres:
                continue
            else:
                i += 1
                print(f"({i}) {barco_nombre}")

        barco_elegido = input("\nEscribe el nombre del barco que elegirás -> ")
        if barco_elegido in self.barcos_nombres:
            print("El barco indicado ya se encuentra dentro del canal!\n")
            return False
        else:
            print(f"Bien, el barco {barco_elegido} ingresará al canal!\n")
            self.barcos_nombres.append(barco_elegido)
            barco = inst.instanciar_barco(barcos[barco_elegido])
            self.barcos.append(barco)
            return True

    # Se simula una hora en el canal, efectuando las acciones correspondientes a la iteración
    def avanzar_barcos(self):
        pass

    # El canal intenta desencallar un barco con cierta probabilidad, antes pagando el costo
    def desencallar_barco(self, barco_nombre):
        # Se paga la tarifa por intentar desencallar un barco
        self.dinero -= p.COSTO_DESENCALLAR
        print(f"Luego de pagar por intentar desencallar el barco, el canal tiene ${self.dinero}")
        # El resultado depende de la probabilidad de éxito
        prob_exito = p.PROB_BASE_DESENCALLAR * self.pond_desencallar
        
        if prob_exito < random():   # Resultado sin éxito
            print(f"¡Fue un fracaso el intento de desencallar el barco {barco_nombre}!\n")
            return False
        else:                       # Resultado con éxito
            print(f"¡El barco {barco_nombre} desencalló con éxito!\n")
            for barco in self.barcos:
                if barco.nombre == barco_nombre:
                    barco.encallado = False
                    break
            return True
            


if __name__ == "__main__":
    #Test 1
    canal = Canal("Mapocho", 50, "principiante")
    print(f"Dinero del canal = {canal.dinero}")
    canal.dinero -= 50000
    print(f"Dinero del canal = {canal.dinero}")
    print(f"Termina la simulación? -> {canal.fin_sim}")