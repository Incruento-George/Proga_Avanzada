import parametros as p

"""
This file only contains definitions of classes related with Mercancia

Mercancia --> Nro de lote, tipo, tiempo de expiración, peso
"""

# No se necesita utilizar ABC para esta clase, ya que generaliza todos lso tipos de mercancía
class Mercancia():
    
    def __init__(self, num_lote, tipo, t_exp, peso):
        # ATRIBUTOS BÁSICOS COMÚN PARA TODAS LAS MERCANCIAS
        self.num_lote = num_lote                    # int
        self.tipo = tipo                            # str
        self.tiempo_exp = t_exp                     # int
        self.peso = peso                            # int
        self.expirado = False

    def __repr__(self):
        return f"Lote {self.num_lote}"

    # Cuando el tiempo de viaje del barco supera al tiempo de expiración, se cobra multa al canal
    def expirar(self, t_viaje):
        # La mercancía solo puede expirar una sola vez
        if self.expirado:
            return False
        
        # El valor de la multa depende del tipo de la mercancía
        multa = 0
        if self.tipo == "petróleo":
            multa = p.MULTA_PETROLEO
        elif self.tipo == "ropa":
            multa = p.MULTA_ROPA
        elif self.tipo == "alimentos":
            multa = p.MULTA_ALIMENTOSA
        else:
            multa = 0
            print("Mercancía desconocida detectada!")

        # Comparación entre tiempo de viaje y tiempo de expiración
        if t_viaje > self.tiempo_exp:
            print(f"La mercancía {self.num_lote} ha expirado!!")
            print(f"El canal deberá pagar una multa de {multa}")
            self.expirado = True
            return multa
        else:
            return False