# Si el programa detecta que se ingresó este input en una conversación de grupo
# deberá sacar al usuario del grupo.
ABANDONAR_FRASE = "\\salir"

# Si el programa detecta que se ingresó este input en cualquier conversación,
# debe volver al menú anterior.
VOLVER_FRASE = "\\volver"

import os
# Path de archivos csv para carga de base de datos
PATH_USUARIOS   = os.path.join("csv_files", "usuarios.csv")
PATH_CONTACTOS  = os.path.join("csv_files", "contactos.csv")
PATH_GRUPOS     = os.path.join("csv_files", "grupos.csv")
PATH_MENSAJES   = os.path.join("csv_files", "mensajes.csv")


if __name__ == "__main__":
    print(PATH_USUARIOS)
    print(PATH_CONTACTOS)
    print(PATH_GRUPOS)
    print(PATH_MENSAJES)