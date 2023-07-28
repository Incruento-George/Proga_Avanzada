"""
Archivo principal para ejecución de la Tarea 0 DCConecta2
"""

import sys
import menus as m
import read_write_csv as rw


print("Empezando ejecución del programa DCConecta2... \n\n")

flow = "Inicio"
working = True
while working:
    # El flujo del programa se mueve al menú de inicio
    if flow == "Inicio":
        flow , user_name = m.menu_inicio()

    # El flujo del programa se mueve al menú de chats
    elif flow == "Chats":
        flow = m.menu_chats()

    # El flujo del programa se mueve al menú de contactos DEL USUARIO QUE INICIÓ SESIÓN
    elif flow == "Contactos":
        flow = m.menu_contactos()

    # El flujo del programa se mueve al sub-menú que presenta la lista de contactos DEL USUARIO 
    elif flow == "Contactos_lista":
        flow, friend_name = m.lista_contactos(user_name)

    # El flujo del programa se mueve al sub-menú que permite añadir un nuevo contacto DEL USUARIO
    elif flow == "Contactos_añadir":
        flow = m.agregar_contacto(user_name)

    # El flujo del programa se mueve al menú de grupos DEL USUARIO QUE INICIÓ SESIÓN
    elif flow == "Grupos":
        flow = m.menu_grupos()

    # El flujo del programa se mueve al sub-menú que presenta la lista de grupos DEL USUARIO
    elif flow == "Grupos_lista":
        flow, group_name = m.lista_grupos(user_name)

    # El flujo del programa se mueve al sub-menú que permite crear un nuevo grupo DEL USUARIO
    elif flow == "Grupos_crear":
        flow = m.crear_grupo(user_name)

    # En cualquier otro caso no definido, se cierra el programa
    else:
        working = False
        sys.exit()