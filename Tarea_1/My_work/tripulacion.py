from abc import ABC, abstractmethod

"""
This file only contains definitions of classes related with Tripulacion

Tripulacion --> Tipos: DCCapitán, DCCocinero, DCCarguero
"""

# Clase abstracta de la que herederán todos los tipos de tripulantes
class Tripulacion(ABC):
    
    def __init__(self, nombre, experiencia):
        # ATRIBUTOS BÁSICOS COMÚN ENTRE TODOS LOS TIPOS DE TRIPULACIÓN
        self.nombre = nombre
        self.experiencia = experiencia
        self.efecto_usado = False
        self.tipo = ""

    def __repr__(self):
        return f"{self.tipo}: {self.nombre}"

    # El efecto especial depende del tipo de tripulante
    @abstractmethod
    def efecto_especial(self):
        pass


# Tipo de tripulante -> Efecto especial: desencalla automáticamente el barco la primera vez
class DCCapitan(Tripulacion):

    def __init__(self, nombre, experiencia):
        super().__init__(nombre, experiencia)
        self.tipo = "DCCapitán"

    # Desencalla el barco automáticamente la primera vez que encalle en el canal
    def efecto_especial(self):
        # El efecto especial solo puede ser usado una vez
        if self.efecto_usado:
            return False
        else:
            print(f"El DCCapitán {self.nombre} usará su efecto especial y desencallará el barco!")
            # print(f"El DCCapitán {self.nombre} no podrá usar más su efecto especial\n")
            self.efecto_usado = True
            return True
        

# Tipo de tripulante -> Efecto especial: Duplica el tiempo de expiración de los ALIMENTOS
class DCCocinero(Tripulacion):

    def __init__(self, nombre, experiencia):
        super().__init__(nombre, experiencia)
        self.tipo = "DCCocinero"

    # Duplica el tiempo de expiración de las mercancías tipo "alimentos" del barco
    def efecto_especial(self):
        # El efecto especial solo puede ser usado una vez
        if self.efecto_usado:
            return False
        else:
            print(f"El DCCocinero {self.nombre} usará su efecto especial para conservar alimentos")
            # print(f"El DCCocinero {self.nombre} no podrá usar más su efecto especial\n")
            self.efecto_usado = True
            return True


# Tipo de tripulante -> Efecto especial: Aumenta la carga máxima que soporta el barco
class DCCarguero(Tripulacion):

    def __init__(self, nombre, experiencia):
        super().__init__(nombre, experiencia)
        self.tipo = "DCCarguero"

    # Aumentará la carga máxima del barco en una cantidad igual a CARGA_EXTRA_CARGUERO
    def efecto_especial(self):
        # El efecto especial solo puede ser usado una vez
        if self.efecto_usado:
            return False
        else:
            print(f"El DCCarguero {self.nombre} usará su efecto especial para llevar más carga")
            # print(f"El DCCarguero {self.nombre} no podrá usar más su efecto especial\n")
            self.efecto_usado = True
            return True