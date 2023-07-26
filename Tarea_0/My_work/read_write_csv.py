import parametros as p
from collections import defaultdict

# Función para cargar datos de usuarios a partir de archivo csv
# Recibe path de archivo csv y retorna set con nombre de usuarios registrados
def cargar_usuarios():
    # Open file and read it
    usuarios = set()
    with open(p.PATH_USUARIOS, "r", encoding="UTF-8") as users_file:
        users_file.readline()
        for user_name in users_file:
            usuarios.add(user_name.strip())
    
    return usuarios


# Función para crear nuevo usuario y agregarlo a la base de datos
# Recibe el nombre de usuario, verifica que está disponible, lo agrega en caso positivo
#  y en caso negativo no lo agrega e imprime mensaje de aviso
def crear_usuario(new_name, usuarios):
    # Check rules
    # Between 3 and 15
    if len(new_name) < 3 or len(new_name) > 15:
        print("Nombre de usuario inválido. Debe contener entre 3 a 15 caracteres!")
        return False
    # No ","" in the name
    if "," in new_name:
        print("Ningún nombre de usuario puede contener el caracter ','")
        return False

    # Add new user if not repeated
    if new_name in usuarios:
        print("El nombre de usuario se encuentra ocupado. Piensa en otro nombre!")
        return False
    elif new_name not in usuarios:
        usuarios.add(new_name)
        with open(p.PATH_USUARIOS, "a") as users_file:
            users_file.write("\n" + new_name)

        print("Tu nombre de usuario ha sido creado, ahora puedes iniciar sesión!")
    return True


# Función para cargar datos de contactos a partir de archivo csv
# Recibe path de archivo csv y retorna dict con llave el usuario y valor sus contactos
def cargar_contactos(path_csv):
    # Open file and read it
    contactos = defaultdict(set)
    with open(path_csv, "r", encoding="UTF-8") as contacts_file:
        contacts_file.readline()
        contacts_list = [line.strip().split(",") for line in contacts_file]
        for user, contact in contacts_list:
            contactos[user].add(contact)

    return contactos


# Función para cargar datos de grupos a partir de archivo csv
# Recibe path de archivo csv y retorna dict con llave el grupo y valor sus integrantes
def cargar_grupos(path_csv):
    # Open file and read it
    grupos = defaultdict(set)
    with open(path_csv, "r", encoding="UTF-8") as groups_file:
        groups_file.readline()
        groups_list = [line.strip().split(",") for line in groups_file]
        for group, user in groups_list:
            grupos[group].add(user)

    return grupos


# Función para crear nuevo grupo y agregarlo a la base de datos
# Recibe el nombre del grupo, verifica que está disponible, lo agrega en caso positivo
#  y en caso negativo no lo agrega e imprime mensaje de aviso
def crear_grupo(usuario, new_name, grupos, usuarios):
    # Check rules
    # At least 1 char in the name of the group and no ","
    if len(new_name) < 1:
        print("El nombre del grupo debe ser de al menos un caracter!")
        return False
    elif "," in new_name:
        print("Ningún nombre de grupo puede contener el caracter ','")
        return False
    
    # Create new group if not repeated
    if new_name in grupos:
        print("El nombre del grupo se encuentra ocupado. Piensa en otro nombre!")
        return False
    elif new_name not in grupos:
        # At least 2 users in the group to finally create it
        print("A continuación indica los usuarios a agregar al grupo con el siguiente formato:\n\n")
        print("usuario1;usuario2;...;usuarioN\n\n")
        group_users = input("Tu respuesta --> ")
        print()
        group_users = group_users.split(";")

        # Check members
        if len(group_users) < 1:
            print("Para crear el grupo se requieren al menos dos integrantes!")
            return False
        for member in group_users:
            if member not in usuarios:
                print(f"El usuario {member} no existe! No se creará el grupo")
                return False
        
        print("Los integrantes han sido verificados exitosamente! Ahora crearé el grupo")
        grupos[new_name] = group_users
        with open(p.PATH_GRUPOS, "a") as groups_file:
            groups_file.write("\n" + new_name + "," + usuario)
            for member in group_users:
                groups_file.write("\n" + new_name + "," + member)
            
        print(f"El grupo {new_name} ha sido creado!")
    return True


# Función para cargar datos de mensajes a partir de archivo csv
# Recibe path de archivo csv y retorna dos dict (regular y grupo) con llave el emisor
#  y valor la información del mensaje (receptor, fecha, contenido)
def cargar_mensajes(path_csv):
    # Open file and read it
    msg_regular = defaultdict(list)
    msg_grupo   = defaultdict(list)
    with open(path_csv, "r", encoding="UTF-8") as msg_file:
        msg_file.readline()
        msg_list = [line.strip().split(",", maxsplit=4) for line in msg_file]
        for item in msg_list:
            if item[0] == "regular":
                msg_regular[item[1]].append(item[2:])
            elif item[0] == "grupo":
                msg_grupo[item[1]].append(item[2:])

    return msg_regular, msg_grupo


if __name__ == "__main__":
    import parametros as p
    # Test 1
    usuarios = cargar_usuarios()
    print(usuarios, "\n")

    # Test 2
    contactos = cargar_contactos(p.PATH_CONTACTOS)
    print(contactos, "\n")

    # Test 3
    grupos = cargar_grupos(p.PATH_GRUPOS)
    print(grupos, "\n")

    # Test 4
    msg_regular, msg_grupo = cargar_mensajes(p.PATH_MENSAJES)
    print(msg_regular, "\n")
    print(msg_grupo, "\n")

    # Test 5
    new_user_bool = crear_usuario("Incruento", usuarios)
    print(new_user_bool, "\n")

    #Test 6
    new_group_bool = crear_grupo("lily416", "Los JAJA", grupos, usuarios)
    print(new_group_bool, "\n")