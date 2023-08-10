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
        self.dinero = p.DINERO_INICIAL                  # float (USD)
        self.barcos_nombres = []                        # list [str: nombres de los barcos]

        # Atributos que dependen de la dificultad del canal
        if self.dificultad == "Principiante":
            # El costo de salida que paga un barco al canal al salir | int (USD)
            self.costo_uso = p.COBRO_USO_PRINCIPIANTE
            # La probabilidad de éxito de desencallar un barco posee un ponderador
            self.pond_desencallar = p.PONDERADOR_PRINCIPIANTE
        else:
            # El costo de salida del canal depende de su dificultad | int (USD)
            self.costo_uso = p.COBRO_USO_AVANZADO
            # La probabilidad de éxito de desencallar un barco posee un ponderador
            self.pond_desencallar = p.PONDERADOR_AVANZADO

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

        barco_elegido = input("Escribe el nombre del barco que elegirás -> ")
        if barco_elegido in self.barcos_nombres:
            print("El barco indicado ya se encuentra dentro del canal!")
            return False
        else:
            print(f"Bien, el barco {barco_elegido} ingresará al canal!")
            self.barcos_nombres.append(barco_elegido)
            barco = inst.instanciar_barco(barcos[barco_elegido])
            self.barcos.append(barco)
            return True

    # Se simula una hora en el canal, efectuando las acciones correspondientes a la iteración
    def avanzar_barcos(self):
        pass

    # El canal intenta desencallar un barco con cierta probabilidad, antes pagando el costo
    def desencallar_barcos(self, barco_nombre):
        # Se evalúa primero si el barco posee el dinero suficiente
        if self.dinero < p.COSTO_DESENCALLAR:
            print(f"El canal no tiene dinero suficiente para desencallar el barco elegido!")
        else:
            # El resultado depende de la probabilidad de éxito
            prob_exito = p.PROB_BASE_DESENCALLAR * self.pond_desencallar
            
            if prob_exito < random():   # Resultado sin éxito
                print(f"Fue un fracaso el intento de desencallar el barco {barco_nombre}!")
                return False
            else:                       # Resultado con éxito
                print(f"El barco {barco_nombre} desencalló con éxito!")
                return True