
"""
Ejercicio nivel 2: Analizador de examen sanguíneo
Modulo de calculos.

Temas:f
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:

"""

def crear_paciente(id:int, genero:str, edad:int, PPM:int,
                   Hb:int, CGB:float, glicemia:int, LDL:float, HDL:float, trigliceridos:float, CT:float,
                   CL:float, CP:float, tiempo:int, GCH:int) -> dict:
    """Crear un diccionario que representa un paciente que se realizo examen de sangre con todos sus atributos inicializados.
    :param id: Id del paciente y de su muestra sanguínea
    :param genero: Género del paciente que se realizó el examen de sangre
    :param edad: Edad del paciente que se realizó el examen de sangre
    :param PPM: Pulsaciones por minuto del paciente al momento de la toma de la muestra
    :param Hb: Hemoglobina en la muestra de sangre (g/L)
    :param CGB: Conteo de glóbulos blancos en la muestra de sangre (x10^3/uL)
    :param glicemia: glicemia en ayunas detectada en la muestra de sangre (mg/dl)
    :param LDL: Lipoproteínas de baja densidad en la muestra de sangre (mg/dl)
    :param HDL: Lipoproteínas de alta densidad en la muestra de sangre (mg/dl)
    :param trigliceridos: Trigliceridos en la muestra de sangre (mg/dl)
    :param CT: Colesterol total en la muestra de sangre (mg/dl)
    :param CL: Conteo de linfocitos en la muestra sangre (10^3/uL)
    :param CP: Conteo de plaquetas en la muestra de sangre (10^3/uL)
    :param tiempo: Tiempo de procesamiento de la muestra de sangre (min)
    :param GCH: Gonadotropina coriónica humana en la muestra de sangre (mIU/ml)
    :return:
        dict: Diccionario con los resultados del exámen sanguíneo
    """

    #TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def buscar_examen(id:int, e1:dict,e2:dict, e3:dict, e4:dict)->dict:
    """
    Busca en cuál de los 4 diccionarios que se pasan por parámetro está el examen de sagnre
    cuyo id es dado por parametro.
    Si no se encuentra el exámen, se retorna None.
    :param id: El id del exámen de sangre que se desea buscar
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        dict: Diccionario del exámen de sangre cuyo id fue dado por parámetro. Retorna None si no lo encuentra
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

# Especificar genero
def confirmar_embarazo(examen:dict)->bool:
    """
    Valida si hay embarazo dependiendo de los niveles de la GCH en el examen de sangre con
    id dado por parámetro
    :param examen: Diccionario con el examen de sangre a analizar
    :return:
        bool: True si el examen de sangre confirma el embarazo, False de lo contrario
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None


def validar_pulsaciones(examen:dict)->str:
    """
    Valida si el paciente tiene taquicardía, bradicardía o normalidad .
    :param examen: Diccionaro con el examen sanguíneo al cual se le verificará las pulsaciones por minuto (PPM)
    :return:
        str: retorna taquicardia si las PPM están por encima de los límites normales, retorna bradicardia si están
        por debajo de los límites normales y retorna normalidad en cualquier otro caso:
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None


def confirmar_anemia(examen:dict) -> bool:
    """
    Valida si el examen de sangre muestra anémia en la sangre dada la hemoglobina en sangre
    :param examen: Diccionario con el examen de sangre al cual se le verificará anemia
    :return:
        bool: True si hay evidencia de anemia, False de lo contrario
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def contar_hipoglicemicos(e1:dict,e2:dict, e3:dict, e4:dict)->int:
    """
    Cuanto cuantos pacientes son hipoglicémicos
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        int: Número de pacientes que son hipoglicémicos
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def validar_infecciones(e1:dict,e2:dict, e3:dict, e4:dict)-> str:
    """
    Valida cuales exámenes de sangre presentan posiblidad de infecciones dependiendo del conteo de globulos
    blancos (CGB)
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        str: una cadena con todos los id's de los exámenes de sangre que presentan posibilidad de infección
        separados por comas
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def calcular_promedio(e1:dict,e2:dict, e3:dict, e4:dict)->float:
    """
    Calcula el tiempo promedio de procesamiento para las muestras de sangre
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        float: Tiempo promedio de procesamiento de las muestras de sangre en minutos.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None
# Entra el diccionario, tipo y objetivo
def actualizar_glicemia(tipo:int, objetivo:int, examen:dict)-> int:
    """
    Dado el id de un examen de sangre, calcular el número de unidades de insulina, del tipo especificado,
    necesarias para corregir los niveles de azúcar en sangre hasta el nivel objetivo dado por parámetro.
    Se debe actualizar el valor de la glicemia en el examen de sangre especificado, añadir la llave
    de unidades_Suministradas con el valor de las unidades de insulina para corregir el azúcar en sangre
    :param examen: Diccionario con el examen de sangre al cual se le corregirá la glicemia en sangre
    :param tipo: Tipo de insulina que difiere en la concentracion de insulina en la ampolla para la correción.
                De este depende el factor de correción.
    :param objetivo: Nivel de azúcar en sangre objetivo
    :return:
        int: Número de unidades de insulina del tipo especificado para realizar la corrección. Si no se necesita
        ninguna unidad, retorna 0.
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def validar_diabetes(examen:dict)->str:
    """
    Valida si el examen de sangre muestra indices de diabetes de acuerdo a la glicemia en ayunas
    :param examen: Diccionario con el examen de sangre a validar
    :return:
        str: Rertorna diabetes o prediabetes si la glicemia lo soporta, de lo contrario retorna normalidad
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def calcular_riesgo_cardiaco(examen:dict)->int:
    """
    Calular los puntos de riesgo cardíaco a partir del perfil lipídico
    :param examen: Examen de sangre al cual se le calcularan los puntos de riesgo
    :return:
        int: puntos de riesgo cardiaco del examen dado por parámetro. Si hay dos o más pacientes con el mismo 
        nivel de riesgo retorna el primero.
    """

    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def evaluar_prioridad(e1:dict,e2:dict, e3:dict, e4:dict)->dict:
    """
    Retorna el diccionario con el examen de sangre del paciente que tiene mayor prioridad para ser atendido
    dado los puntos de riesgo cardiaco del perfíl lipídico.
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        retorna el diccionario con el paciente prioriatrio dado sus puntos de riesgo cardiaco.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def validar_CLL(examen:dict, frotis:bool) -> int:
    """
    Valida si el paciente debe ser diagnosticado con CLL dado su conteo de linfocitos, plaquetas y si el resultado del
    examen de frotis.
    :param examen: Diccionario con el examen de sangre a validar
    :param frotis: Resultado del examen del frotis de las células sanguíneas.
    :return:
        int: Retorna 0 si es negativo para CLL, retorna 1 si es positivo para CLL y retorna -1 si se debe realizar
        una biopsia de médula osea para confirmar el diagnóstico.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None