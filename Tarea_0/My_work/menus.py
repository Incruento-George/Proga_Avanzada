import sys
import read_write_csv as rw

# Primer menú de DCConecta2 que se presenta al iniciar el programa
# Opciones: Iniciar sesión, Crear nuevo usuario, Salir del programa
def menu_inicio():
    print("*" * 7 + "  Menú de Inicio  " + "*" * 7 + "\n")
    print("(1) Iniciar sesión"+"\n"+"(2) Crear usuario"+"\n"+"(3) Salir del programa"+"\n")

    num_option = 0
    while num_option not in ("1", "2", "3"):
        num_option = input("Indica el número de la opción que eliges --> ")
        if num_option not in ("1", "2", "3"):
            print("Debes elegir una de las opciones disponibles! 1, 2 o 3", "\n")

    usuarios = rw.cargar_usuarios()
    if num_option == "1":           # Iniciar sesión
        print("Has decidido iniciar sesión!")
        user_name = input("Por favor indica tu nombre de usuario --> ")

        if user_name not in usuarios:
            print("El nombre de usuario no se encuentra registrado. Volviendo al menú de inicio")
            return "Inicio", None
        elif user_name in usuarios:
            print(f"Bienvenido {user_name}! Vamos al menú de chats\n")
            return "Chats", user_name
        
    elif num_option == "2":         # Crear usuario
        print("Has decidido crear un nuevo usuario!")
        user_name = input("Elige un nombre de usuario para verificarlo antes de crearlo --> ")
        register_bool = rw.crear_usuario(user_name, usuarios)

        if register_bool == True:
            return "Chats", user_name
        else:
            return "Inicio", None
    
    elif num_option == "3":         # Salir del programa
        print("Has decidido cerrar el programa. Nos vemos!\n")
        sys.exit()


# Segundo menú de DCConecta2 que permite ver contactos, grupos o volver al inicio
# Opciones: Ver contactos, Ver grupos, Volver al inicio
def menu_chats():
    print("*" * 7 + "  Menú de Chats  " + "*" * 7 + "\n")
    print("(1) Ver contactos"+"\n"+"(2) Ver grupos"+"\n"+"(3) Volver al inicio"+"\n")

    num_option = 0
    while num_option not in ("1", "2", "3"):
        num_option = input("Indica el número de la opción que eliges --> ")
        if num_option not in ("1", "2", "3"):
            print("Debes elegir una de las opciones disponibles! 1, 2 o 3", "\n")

    if num_option == "1":           # Ver contactos
        print("Has decidido ver tus contactos!\n")
        return "Contactos"
        
    elif num_option == "2":         # Ver grupos
        print("Has decidido ver tus grupos!\n")
        return "Grupos"
    
    elif num_option == "3":         # Volver al menú de inicio
        print("Has decidido volver al menú de inicio. Cerraré tu sesión!\n")
        return "Inicio"
    

# Tercer menú de DCConecta2 que permite ver contactos, añadir un contacto nuevo o volver atrás
# Opciones: Ver contactos, Añadir nuevo contacto, Volver al menú de chats
def menu_contactos():
    print("*" * 7 + "  Menú de Contactos  " + "*" * 7 + "\n")
    print("(1) Ver contactos"+"\n"+"(2) Añadir nuevo contacto"+"\n"+"(3) Volver atrás"+"\n")

    num_option = 0
    while num_option not in ("1", "2", "3"):
        num_option = input("Indica el número de la opción que eliges --> ")
        if num_option not in ("1", "2", "3"):
            print("Debes elegir una de las opciones disponibles! 1, 2 o 3", "\n")

    if num_option == "1":           # Ver lista de contactos
        print("Voy a desplegar una lista con tus contactos para que le escribas a uno de ellos!\n")
        return "Contactos_lista"
        
    elif num_option == "2":         # Añadir nuevo contacto
        print("Has decidido añadir un nuevo contacto a tu lista de amigos!\n")
        return "Contactos_añadir"
    
    elif num_option == "3":         # Volver al menú de chats
        print("Has decidido volver al menú de chats. Tu sesión seguirá abierta!\n")
        return "Chats"


# Sub-menú del menú contactos que presenta lista de contactos del usuario que inició sesión
# Cada contacto del usuario es una opción elegible para abrir el chat con este
def lista_contactos(user_name):
    contactos_all = rw.cargar_contactos()           # Red completa de contactos de DCConecta2
    contactos_user = contactos_all[user_name]       # Set con contactos del usuario

    num_option = 0
    while num_option not in range(1, len(contactos_user) + 1):
        print("Esta es tu lista de contactos: \n")
        for num, friend in enumerate(contactos_user, start=1):
            print(f"({num}) {friend}")
    
        print()
        friend_name = input("Escribe el nombre del contacto con el que vas a chatear --> ")
        if friend_name not in contactos_user:
            print("Escribe correctamente el nombre de alguno de tus contactos!\n")
        else:
            print(f"Voy a abrir el chat con tu amigo {friend_name}")
            return "Chat_contacto", friend_name

# Sub-menú del menú contactos que permite añadir un nuevo contacto
def agregar_contacto(user_name):
    friend_name = input("Escribe el nombre del contacto que quieres añadir --> ")
    new_bool = rw.nuevo_contacto(user_name, friend_name)

    if new_bool == False:
        print("No fue posible añadir el nuevo contacto. Regresando a tu menú de contactos!\n")
    else:
        print("Ya tienes un nuevo contacto. Desde tu menú de contactos puedes escribirle!\n")    
        
    return "Contactos"


# Cuarto menú de DCConecta2 que permite ver grupos, crear un grupo nuevo o volver atrás
# Opciones: Ver grupos, Crear nuevo grupo, Volver al menú de chats
def menu_grupos():
    print("*" * 7 + "  Menú de Grupos  " + "*" * 7 + "\n")
    print("(1) Ver grupos"+"\n"+"(2) Crear nuevo grupo"+"\n"+"(3) Volver atrás"+"\n")

    num_option = 0
    while num_option not in ("1", "2", "3"):
        num_option = input("Indica el número de la opción que eliges --> ")
        if num_option not in ("1", "2", "3"):
            print("Debes elegir una de las opciones disponibles! 1, 2 o 3", "\n")

    if num_option == "1":           # Ver lista de grupos
        print("Voy a desplegar una lista con tus grupos para que le escribas a uno de ellos!\n")
        return "Grupos_lista"
        
    elif num_option == "2":         # Crear nuevo grupo
        print("Has decidido crear un nuevo grupo!\n")
        return "Grupos_crear"
    
    elif num_option == "3":         # Volver al menú de chats
        print("Has decidido volver al menú de chats. Tu sesión seguirá abierta!\n")
        return "Chats"    


# Sub-menú del menú grupos que presenta lista de grupos del usuario que inició sesión
# Cada grupo del usuario es una opción elegible para abrir el chat con este
def lista_grupos(user_name):
    groups_members = rw.cargar_grupos().items()
    grupos_user = []

    num_option = 0
    while num_option not in range(1, len(groups_members) + 1):
        print("Esta es tu lista de grupos: \n")
        id = 1
        for group_name, members in groups_members:
            if user_name in members:
                print(f"({id}) {group_name}")
                grupos_user.append(group_name)
                id += 1
    
        print()
        group_name = input("Escribe el nombre del grupo cuyo chat quieres abrir --> ")
        if group_name not in grupos_user:
            print("Escribe correctamente el nombre de alguno de tus grupos!\n")
        else:
            print(f"Voy a abrir el chat del grupo {group_name}")
            return "Chat_grupo", group_name


if __name__ == "__main__":
    # Test 1
    # inicio_bool = menu_inicio()
    # print(f"inicio bool = {inicio_bool} \n")

    # Test 2
    # chats_bool = menu_chats()
    # print(f"chats bool = {chats_bool} \n")

    # Test 3
    # contactos_bool = menu_contactos()
    # print(f"contactos bool = {contactos_bool} \n")

    # Test 4
    # lista_bool = lista_contactos("Gatochico")
    # print(f"lista bool = {lista_bool}")

    # Test 5
    # new_friend_bool = agregar_contacto("Gatochico")
    # print(f"new friend bool = {new_friend_bool} \n")

    # Test 6
    # grupos_bool = menu_grupos()
    # print(f"grupos bool = {grupos_bool} \n")

    # Test 7
    lista_bool = lista_grupos("Gatochico")
    print(f"lista bool = {lista_bool} \n")