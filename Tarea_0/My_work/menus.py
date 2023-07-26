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
            return "Inicio"
        elif user_name in usuarios:
            print(f"Bienvenido {user_name}! Vamos al menú de chats\n")
            return "Chats"
        
    elif num_option == "2":         # Crear usuario
        print("Has decidido crear un nuevo usuario!")
        user_name = input("Elige un nombre de usuario para verificarlo antes de crearlo --> ")
        register_bool = rw.crear_usuario(user_name, usuarios)

        if register_bool == True:
            return "Chats"
        else:
            return "Inicio"
    
    elif num_option == "3":         # Salir del programa
        print("Has decidido cerrar el programa. Nos vemos!")
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
        print("Has decidido ver tus contactos!")
        return "Contactos"
        
    elif num_option == "2":         # Ver grupos
        print("Has decidido ver tus grupos!")
        return "Grupos"
    
    elif num_option == "3":         # Volver al menú de inicio
        print("Has decidido volver al menú de inicio. Cerraré tu sesión!")
        return "Inicio"


if __name__ == "__main__":
    # Test 1
    # inicio_bool = menu_inicio()
    # print(f"inicio bool = {inicio_bool} \n")

    # Test 2
    chats_bool = menu_chats()

    print(f"chats bool = {chats_bool} \n")