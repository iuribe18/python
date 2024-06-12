# Descripción del problema
# En una cierta ciudad, la tarifa de un taxi consiste en una tarifa base de 4000 pesos, más 82 pesos por cada 100 metros recorridos. 
# Escriba una función que reciba como parámetro la distancia recorrida en kilómetros y retorne la tarifa total del viaje.
# No olvide redondear el valor de retorno al entero más cercano.
# Función requerida
# Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
# Nombre de la función:	calcular_tarifa_taxi
# Parámetros
# Nombre: kms_recorridos
# Tipo: float
# Descripción: Kilómetros recorridos en el viaje
# Tipo del retorno: int
# Descipción del retorno: Tarifa a cobrar por el recorrido en taxi, la cual debe estar redondeada al entero mas cercano


def calcular_tarifa_taxi(kms_recorridos):
    tarifa = 4000 + (kms_recorridos*10) * 82
    return tarifa

if __name__ == '__main__':
    kms_recorridos = float(input("Digite los Kilometros Recorridos: "))
    tarifa = calcular_tarifa_taxi(kms_recorridos)
    print("Su tarifa es $",tarifa,"pesos")