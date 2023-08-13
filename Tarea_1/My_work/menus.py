import sys
import rw_files as rw
import parametros as p

"""
This file only contains functions to display menus from the simulation
"""

# Menú de Inicio: comenzar nueva simulación o salir del programa
def menu_inicio():
    print("¿Qué te gustaría hacer?\n")
    print("(1) Comenzar nueva simulación")
    print("(2) Salir del programa\n")

    # Se pregunta por el canal a simular antes de pasar al menú de acciones
    num_option = input("Escribe el NÚMERO de la opción elegida -> ")
    if num_option == "1":
        print("OK. ¡Deberás elegir un canal de la base de datos para la simulación!\n")
        canales_data = rw.cargar_canales()
        for num, canal_nombre in enumerate(canales_data.keys(), start=1):
            print(f"({num}) {canal_nombre}")
        nombre_option = input("\nEscribe el NOMBRE del canal que quieres simular -> ")
        
        if nombre_option not in canales_data.keys():
            print("No reconozco el nombre de este canal. Intenta nuevamente ...\n")
        else:
            print(f"Muy bien. Simularemos usando el {nombre_option}\n")
            return "Acciones", canales_data[nombre_option]
    # Fin del programa
    elif num_option == "2":
        print("OK. Voy a cerrar el programa ...")
        sys.exit()
    # Respuesta no válida
    else:
        return menu_inicio()

# Menú de Acciones: mostrar riesgo, desencallar barco, simular nueva hora o mostrar estado
def menu_acciones(canal):
    print("¿Qué te gustaría hacer?\n")
    print("(1) Mostrar riesgo de encallamiento")
    print("(2) Desencallar barco")
    print("(3) Simular nueva hora")
    print("(4) Mostrar estado de la simulación")
    print("(5) Volver al menú anterior")
    print("(6) Salir del programa\n")
    
    num_option = input("Escribe el NÚMERO de la opción elegida -> ")
    # Se listan barcos en el canal y sus respectivas probabilidades de encallar
    if num_option == "1":
        if len(canal.barcos) == 0:
            print("No hay barcos en el canal para mostrar sus riesgos ...\n")
            return "Acciones"
        else:
            print("Estos son los barcos presentes en el canal y sus riesgos de encallar:\n")
            for barco in canal.barcos:
                print(f"{barco.nombre} - Riesgo: {barco.calcular_riesgo(canal.dificultad) * 100}%")
            return "Acciones"
    
    # Se revisa el dinero del canal y luego se listan barcos encallados para elegir uno
    elif num_option == "2":
        if canal.dinero < p.COSTO_DESENCALLAR:
            print("El canal no cuenta con suficiente dinero para desencallar un barco ...\n")
            return "Acciones"
        else:
            print("Estos son los barcos encallados en el canal:\n")
            barcos_encallados = []
            for barco in canal.barcos:
                if barco.encallado:
                    print(f"*) {barco.nombre} - Posición: {barco.posicion} km")
                    barcos_encallados.append(barco.nombre)
            barco_nombre = input("\nEscribe el nombre del barco a intentar desencallar -> ")
            if barco_nombre not in barcos_encallados:
                print("El barco indicado no se encuentra en la lista de encallados ...\n")
            else:
                desencallar_resultado = canal_obj.desencallar_barco(barco_nombre)
            return "Acciones"
    
    # Revisar si canal bloqueado, ingresar barco, calcular si encallaron barcos, evento especial
    # de cada barco, simular desplazamiento de barcos, verificar si salieron barcos
    elif num_option == "3":
        # Se revisa si el canal está bloqueado por algún barco encallado
        canal_bloqueado = False
        for barco in canal.barcos:
            if barco.encallado:
                canal_bloqueado = True
        
        if canal_bloqueado:
            print("El canal se encuentra bloqueado debido a uno o más barcos encallados")
            print("No podrán ingresar nuevos barcos al canal en esta hora\n")
        # Si el canal no está bloqueado, puede ingresar hasta un barco al canal en esta hora
        else:
            print("A continuación verás una lista de los barcos que pueden ingresar al canal\n")
            barcos_data = rw.cargar_barcos()
            for barco_nombre in barcos_data.keys():
                if barco_nombre not in canal.barcos_nombres:
                    print(f"- {barco_nombre}")
            
            print("\nEscribe el NOMBRE del barco que ingresará al canal o 0 si ninguno ...")
            barco_entrar = input(" --> ")
            if barco_entrar == "0":
                print(f"En esta hora de simulación no ingresará ningún barco al canal\n")
            if barco_entrar in canal.barcos_nombres:
                print("¡Debes elegir un barco que no esté dentro del canal!\n")
                return "Acciones"
            elif barco_entrar not in barcos_data.keys():
                print(f"El barco {barco_entrar} no se encuentra en la base de datos\n")
                return "Acciones"
            else:
                print(f"¡El barco {barco_entrar} se dirige a la entrada del canal!\n")
                barco = inst.instanciar_barco(barcos_data[barco_entrar])
                canal.barcos.append(barco)
                canal.barcos_nombres.append(barco.nombre)
            
            # Se determina si barcos en el canal encallaron o no
            

    
    # Se despliega en consola toda la información relevante del estado de la simulación
    elif num_option == "4":
        print("-" * 9 + " ESTADO DEL CANAL Y SIMULACIÓN " + "-" * 9)
        print("-" * 59 + "\n")
    
        print(f"{canal.nombre} | Largo de {canal.largo} Km | Dificultad: {canal.dificultad}")
        print(f"Horas simuladas: {canal.horas_sim}")
        print(f"Dinero disponible: {canal.dinero}")
        print(f"Dinero recibido: {canal.dinero_recibido}")
        print(f"Dinero gastado: {canal.dinero_gastado}\n")

        print(f"Un total de {canal.num_barcos_idos} han pasado por el canal")
        print(f"Un total de {canal.num_barcos_encallados} encallamientos han ocurrido")
        print(f"Un total de {canal.num_eventos_ocurridos} han ocurrido en este tiempo")
        return "Acciones"
    
    # Usuario regresa al menú de inicio
    elif num_option == "5":
        print("OK. ¡Volviendo al menú de inicio!")
        return "Inicio"
    # Usuario decide cerrar el programa
    elif num_option == "6":
        print("OK. Voy a cerrar el programa ...")
        sys.exit()
    # Respuesta no válida
    else:
        return menu_acciones()


if __name__ == "__main__":
    import instanciador as inst
    # Test 1
    flow, canal_data = menu_inicio()
    canal_obj = inst.instanciar_canal(canal_data)

    canal_obj.ingresar_barco()
    canal_obj.barcos[0].encallado = True

    # Test 2
    result_2 = menu_acciones(canal_obj)
    print(f"Barco {canal_obj.barcos[0].nombre} -> Encallado? {canal_obj.barcos[0].encallado}")