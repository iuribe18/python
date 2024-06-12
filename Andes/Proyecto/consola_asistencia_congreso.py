import asistencia_congreso as asis

def ejecutar_cargar_datos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de asistencia de los congresistas
        Retorno: list
            La lista de asistencia por parte de congresistas de la camara de representantes a sesiones en el congreso
    """
    asistencias = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la asistencia: ")
    asistencias = asis.cargar_datos(archivo)
    if len(asistencias) == 0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información de la asistencia")
    else:
        print("Se cargaron las asistencias de los siguientes congresistas a partir del archivo")
    for elemento in asistencias:
        print(elemento)
    return asistencias

def ejecutar_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias injustificadas.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) faltó (inasistencias) veces a sesiones de forma injustificada"
    """
    inasistencias = asis.mas_inasistencias(asistencias)

    #print("El congresista (nombre_congresista) faltó (inasistencias) veces a sesiones de forma injustificada")
    for i in inasistencias:
        print("El congresista", (inasistencias[0][0]), "faltó", inasistencias[0][1], "veces a sesiones de forma injustificada")


def ejecutar_mas_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de asistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) asistió (asistencias) veces a sesiones del congreso"
    """
    mas_asistencias = asis.mas_asistencias(asistencias)
    # for i in mas_asistencias:
    #     print("El congresista", (mas_asistencias[0][0]), "asistió", mas_asistencias[0][1], "veces a sesiones del Congreso")
    for i in mas_asistencias:
        print("El congresista", i[0], "asistió", i[1], "veces a sesiones del Congreso")

def ejecutar_porcentaje_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el porcentaje de asistencias por cada congresista.
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo porcentaje de asistencia.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (Porcentaje congresista 1)
        (Nombre congresista 2) : (Porcentaje congresista 2)
    """
    porcentaje = asis.porcentaje_asistencias(asistencias)
    for i in porcentaje:
        print("Congresista", i[0], "Porcentaje: ", i[1])

def ejecutar_circunscripcion_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la circunscripcion con mayor número de inaasistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        La circunscripción (nombre circunscripcion) acumuló (número de fallas) fallas
    """
    circunscripcion_mas_inasistencias = asis.circunscripcion_mas_inasistencias(asistencias)
    for i in circunscripcion_mas_inasistencias:
        print("La circunscripción", (circunscripcion_mas_inasistencias[0][0]), "acumuló", circunscripcion_mas_inasistencias[0][1], "fallas")

def ejecutar_mas_inasistencias_excusa(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias al congreso con excusa médica.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre congresista) falló (numero de inasistencias) veces con excusa médica
    """
    mas_inasistencias_excusa = asis.mas_inasistencias_excusa(asistencias)
    for i in mas_inasistencias_excusa:
        print("El congresista", (mas_inasistencias_excusa[0][0]), "falló", mas_inasistencias_excusa[0][1], "veces con excusa médica")

def ejecutar_mas_X_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar los congresistas que fallan mas de un numero determinado de veces
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo número de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (inasistencias congresista 1)
        (Nombre congresista 2) : (inasistencias congresista 2)
        Si el diccionario está vacío debe retornar el siguiente mensaje: Ningún congresista supera el limite establecido
    """
    limite = int(input("Seleccione Limite de Inasistencias: "))
    mas_X_inasistencias = asis.mas_X_inasistencias(asistencias)
    
    # Cuenta la cantidad de veces que cumple la condición
    contador = 0 
    for i in mas_X_inasistencias:
        if mas_X_inasistencias[i] > limite:
            contador += 1
    
    # Si NO se cumple la condición (el limite es superior a las inasistencias de los congresistas) el contador es Cero [0]
    if contador == 0:
            print("Ningún congresista supera el limite establecido")
    else:
        for i in mas_X_inasistencias:
            if mas_X_inasistencias[i] > limite:
                print("Cogresista:", i, "Inasistencias:", mas_X_inasistencias[i])

def ejecutar_asistencias_partido(asistencias:list)->None:
    """Ejecuta la opción de consultar los porcentajes de asistencias de los partidos politicos
        Se debe mostrar al usuario el nombre de cada partido con su respectivo porcentaje de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre partido 1) : (porcentaje partido 1)
        (Nombre partido 2) : (porcentaje partido 2)
    """
    porcentaje_asistencias_partido = asis.asistencias_partido(asistencias)
    for i in porcentaje_asistencias_partido:
        print("Partido", i[0], "Porcentaje: ", i[1])

def ejecutar_fecha_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la fecha con mayor número de inasistencias
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En la fecha (fecha) hubo (número de inasistencias) fallas
    """
    fecha_mas_inasistencias = asis.fecha_mas_inasistencias(asistencias)
    for i in fecha_mas_inasistencias:
        print("En la Fecha", (fecha_mas_inasistencias[0][0]), "hubo", fecha_mas_inasistencias[0][1], "fallas")


def ejecutar_mes_mayor_sesiones(asistencias:list)->None:
    """Ejecuta la opción de consultar el mes y año con mayor numero de sesiones
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En el mes (mes/año) hubo (número de sesiones) sesiones
    """
    mes_mayor_sesiones = asis.mes_mayor_sesiones(asistencias)
    for i in mes_mayor_sesiones:
        print("En el mes", (mes_mayor_sesiones[0][0]), "hubo", mes_mayor_sesiones[0][1], "sesiones")

def ejecutar_asistio_fecha(asistencias:list):
    """Ejecuta la opción de consultar la asistencia de un congresista en una fecha determinada
        Si el congresista asistió a la sesion de la fecha, se debe mostrar el siguiente mensaje:
            El congresista (nombre congresista) asistió a la sesión de la fecha (dia)/(mes)/(anio)
        Si el congresista no asistio o no habia sesion ese dia, se muestra el siguiente mensaje:
            El congresista no asistio a la sesion o no hubo sesion ese dia
    """
    anio = input("Digite Anio: ")
    mes = input("Digite Mes: ")
    if len(mes) == 1:
        mes = '0' + mes
    dia = input("Digite Día: ")
    if len(dia) == 1:
        dia = '0' + dia
    fecha = dia+'/'+mes+'/'+anio
    congresista = input("Digite Nombre Congresista: ")
    asistio_fecha = asis.asistio_fecha(asistencias, fecha, congresista)
    if len(asistio_fecha) == True:
        print("El congresista", asistio_fecha[0], "asistió a la sesión de la fecha: ", dia,'/',mes,'/',anio)
    else:
        print("El congresista no asistio a la sesion o no hubo sesion ese dia")

def ejecutar_asistencia_circunscripcion_fecha(asistencia:list)->None:
    """Ejecuta la opción de consultar la asistencia por circunscripcion en un mes y año determinado
        Se debe mostrar al usuario cada circunscripcion y su respectiva asistencia como se muestra a continuación:
        "(nombre circunscripcion) : (asistencia)"
    """
    anio = input("Digite Año: ")
    mes = input("Digite Mes: ")
    if len(mes) == 1:
        mes = '0' + mes
    asistencia_circunscripcion_fecha = asis.asistencia_circunscripcion_fecha(asistencia,mes,anio)
    print(asistencia_circunscripcion_fecha)

def ejecutar_estadisticas_anuales_asistencias(asistencia:list)->None:
    estadisticas_anuales_asistencias = 


def mostrar_menu():
    print("\nOpciones")
    print("1. Cargar el archivo con la asistencia al congreso")
    print("2. Consultar congresista con más inasistencias injustificadas")
    print("3. Consultar congresista con más asistencias")
    print("4. Calcular porcentaje de asistencia de los congresistas")
    print("5. Consultar la circunscripcion con mas inasistencias")
    print("6. Consultar el congresista con más inasistencias con excusa médica")
    print("7. Consultar congresistas que fallan más de un número determinado de veces")
    print("8. Consultar porcentaje de asistencias por partido político")
    print("9. Consultar fecha con más fallas")
    print("10. Consultar mes y año con mayor número de sesiones realizadas")
    print("11. Consultar asistencias de congresista por fecha")
    print("12. Consultar asistencia por circunscripcion por mes y año")
    print("13. Salir de la aplicacion")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario"""
    continuar  = True
    asistencia = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            asistencia = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 3:
            ejecutar_mas_asistencias(asistencia)
        elif opcion_seleccionada == 4:
            ejecutar_porcentaje_asistencias(asistencia)
        elif opcion_seleccionada == 5:
            ejecutar_circunscripcion_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 6:
            ejecutar_mas_inasistencias_excusa(asistencia)
        elif opcion_seleccionada == 7:
            ejecutar_mas_X_inasistencias(asistencia)
        elif opcion_seleccionada == 8:
            ejecutar_asistencias_partido(asistencia)
        elif opcion_seleccionada == 9:
            ejecutar_fecha_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 10:
            ejecutar_mes_mayor_sesiones(asistencia)
        elif opcion_seleccionada == 11:
            ejecutar_asistio_fecha(asistencia)
        elif opcion_seleccionada == 12:
            ejecutar_asistencia_circunscripcion_fecha(asistencia)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()