from os import path 

""" 
Este archivo contiene todos los parámetros mencionados a lo largo del enunciado de la tarea 1.
Estos parámetros poseen ESTE_FORMATO y se incluyen paths de archivos utilizados.
"""

TENDENCIA_ENCALLAR_PASAJEROS    = 0.2
TENDENCIA_ENCALLAR_CARGUERO     = 0.5
TENDENCIA_ENCALLAR_BUQUE        = 0.3
PONDERADOR_PRINCIPIANTE         = 0.8
PONDERADOR_AVANZADO             = 0.5
PROBABILIDAD_EVENTO_ESPECIAL    = 0.7
DINERO_INTOXICACION             = 200
TIEMPO_AVERIA_BUQUE             = 3
MULTA_PETROLEO                  = 100
MULTA_ROPA                      = 75
MULTA_ALIMENTOS                 = 150
CARGA_EXTRA_CARGUERO            = 200
DINERO_INICIAL                  = 20000
COBRO_USO_PRINCIPIANTE          = 1200
COBRO_USO_AVANZADO              = 700
COSTO_DESENCALLAR               = 500   # Independiente de si el barco ejecuta esa acción con o sin éxito,
PROB_BASE_DESENCALLAR           = 0.7   # el COSTO_DESENCALLAR se cobra.

# Paths de archivos .csv

PATH_BARCOS                     = path.join("csv_files", "barcos.csv")
PATH_CANALES                    = path.join("csv_files", "canales.csv")
PATH_MERCANCIAS                 = path.join("csv_files", "mercancia.csv")
PATH_TRIPULANTES                = path.join("csv_files", "tripulantes.csv")