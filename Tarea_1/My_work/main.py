"""
Archivo principal para ejecución de la Tarea 1 DCCanal
"""

import sys
import menus as m
import instanciador as inst

print("Empezando ejecución del programa DCConecta2... \n")
print("-" * 42)
print("-" * 10 + "¡Bienvenido a DCCanal!" + "-" * 10)
print("-" * 42 + "\n")

flow = "Inicio"
working = True
while working:
    # Menú de inicio
    if flow == "Inicio":
        flow, canal_data = m.menu_inicio()
        if canal_data is not None:
            canal_obj = inst.instanciar_canal(canal_data)

    # Menú de acciones
    elif flow == "Acciones":
        flow = m.menu_acciones(canal_obj)

    # Just in case
    else:
        print("This text should not be printed [I am in main -> while working -> else]")
        sys.exit()

print("FIN")