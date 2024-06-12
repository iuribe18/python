# Importar librería CSV
import csv
import collections
from typing import Counter, List

def cargar_datos(archivo) -> list:
    lista = []
    #new_lista=[]
    with open(archivo, encoding='utf-8-sig') as File:
        reader = csv.DictReader(File)
        for row in reader:
            #Agregar elementos a la lista
            lista.append(row)
    return lista

def mas_inasistencias(lista) -> list:
    inasistencia = []
    inasistencia = [con["congresista"] for con in lista if con["dato_asistencia"] == "SIN EXCUSA"]
    cuenta = collections.Counter(inasistencia)
    # Regresa el congresista con mas inasistencias
    valor = cuenta.most_common(1)
    return valor

def mas_asistencias(lista) -> list:
    asistencias = []
    asistencias = [con["congresista"] for con in lista if con["dato_asistencia"] == "ASISTIÓ"]
    cuenta = collections.Counter(asistencias)
    valor = cuenta.most_common(2)
    return valor

def porcentaje_asistencias(lista) -> list:
    asistencia = []
    todas = []
    asistencia = [con["congresista"] for con in lista if con["dato_asistencia"] == "ASISTIÓ"]
    todas = [con["congresista"] for con in lista]
    # Cantidad de sesiones por cada Congresista
    sesiones_asistidas = collections.Counter(asistencia)
    # Cantidad de sesiones asistidas cada Congresista
    sesiones_todas = collections.Counter(todas)

    prom = []
    
    # Hallar promedio usando List_Compre
    new_dict_count = collections.Counter({key : round((sesiones_asistidas[key] / sesiones_todas[key]),2) for key in sesiones_asistidas})
    prom = list(new_dict_count.items())

    return prom

def circunscripcion_mas_inasistencias(lista) -> list:
    circunscripcion = []
    circunscripcion = [cir["circunscripcion"] for cir in lista if cir["dato_asistencia"] == "EX. MÉDICA" or cir["dato_asistencia"] == "OTRAS EXCUSAS" or cir["dato_asistencia"] == "SIN EXCUSA"]
    cuenta = collections.Counter(circunscripcion)
    valor = cuenta.most_common(1)
    return valor

def mas_inasistencias_excusa(lista) -> list:
    inasistencias_excusa = []
    inasistencias_excusa = [con["congresista"] for con in lista if con["dato_asistencia"] == "EX. MÉDICA"]
    cuenta = collections.Counter(inasistencias_excusa)
    # Regresa el congresista con mas inasistencias por excusa médica
    valor = cuenta.most_common(1)
    return valor

def mas_X_inasistencias(lista) -> list:
    x_inasistencias = []
    x_inasistencias = [con["congresista"] for con in lista if con["dato_asistencia"] == "EX. MÉDICA" or con["dato_asistencia"] == "OTRAS EXCUSAS" or con["dato_asistencia"] == "SIN EXCUSA"]
    cuenta = collections.Counter(x_inasistencias)
    return cuenta

def fecha_mas_inasistencias(lista) -> list:
    fecha_mas_inasistencias = []
    fecha_mas_inasistencias = [date["fecha"] for date in lista if date["dato_asistencia"] == "EX. MÉDICA" or date["dato_asistencia"] == "OTRAS EXCUSAS" or date["dato_asistencia"] == "SIN EXCUSA"]
    cuenta = collections.Counter(fecha_mas_inasistencias)
    valor = cuenta.most_common(1)
    return valor

def asistio_fecha(lista, fecha, congresista) -> list:
#def asistio_fecha(lista) -> list:
    asistio_fecha = []
    #fecha = dia+"/"+mes+"/"anio
    asistio_fecha = [con["congresista"] for con in lista if con["fecha"] == fecha and con["congresista"] == congresista]
    return asistio_fecha

def asistencias_partido(lista) -> list:
    asistencias_partido = []
    #todas = []
    asistencias_partido = [con["movimiento"] for con in lista if con["dato_asistencia"] == "ASISTIÓ"]
    todas_partido = [con["movimiento"] for con in lista]
    # Total sesiones por cada movimiento
    sesiones_asistidas_partido = collections.Counter(asistencias_partido)
    # Cantidad de sesiones asistidas cada Congresista
    sesiones_todas_partido = collections.Counter(todas_partido)
    
    # Hallar promedio usando Dictionary Comprehension
    new_dict_count = collections.Counter({key : round((sesiones_asistidas_partido[key] / sesiones_todas_partido[key]),2) for key in sesiones_asistidas_partido})
    prom_partido = list(new_dict_count.items())
    return prom_partido

def mes_mayor_sesiones(lista) -> list:
    resultado = []
    for item in lista:
        if item['fecha'] not in resultado:
            resultado.append(item['fecha'])
    mes_anno = []
    for item in resultado:
        mes_anno.append(item[3:10])
    cuenta = collections.Counter(mes_anno)    
    valor = cuenta.most_common(1)
    return valor


def asistencia_circunscripcion_fecha(lista, mes, anio) -> list:
    tupla_asistencia_circunscripcion = [con["circunscripcion"] for con in lista if con["dato_asistencia"] == "ASISTIÓ" and con["fecha"][3:10] == mes+'/'+anio]
    cuenta = dict(collections.Counter(tupla_asistencia_circunscripcion))
    return cuenta

def estadisticas_anuales_asistencias(lista) -> list:
    inasistencias_anuales = [con["2018"] for con in lista if con["dato_asistencia"] == "OTRAS EXCUSAS" and con["fecha"][6:10] == "2018" and con["dato_asistencia"] == "SIN EXCUSA" and con["fecha"][6:10] == "2018"]
    print()
    return  inasistencias_anuales