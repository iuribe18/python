# Descripción del problema
# Cree una función que reciba el costo en pesos de una cuenta de restaurante y luego calcule el IVA asociado y la propina para el mesero
# La tasa del IVA corresponde al 19% y la propina en el restaurante es del 10% del valor de la factura (sin impuestos)
# La función debe retornar una cadena que muestre el IVA, propina y total de la siguiente manera: "X,Y,Z", donde X es el IVA, Y la propina y Z el total.
# No olvide aproximar su resultado al entero más cercano
# Función requerida
# Su solución debe tener una función de acuerdo a la siguiente especificación. Usted puede tener funciones adicionales.
# Nombre de la función:	calcular_iva_propina_total_factura
# Parámetros
# Nombre: costo_factura
# Tipo: int
# Descripción: Costo de la factura del restaurante, sin impuestos ni propina
# Tipo del retorno: str	
# Descipción del retorno: Cadena con el IVA, propina y total de la factura, separados por coma



def calcular_iva_propina_total_factura(costo_factura):
    iva = costo_factura * 0.19
    propina = costo_factura * 0.1
    return iva, propina
    
#def calcular_iva(cuenta):
    #iva = cuenta * 0.19
    #return iva

#def calcular_propina(cuenta):
    #propina = cuenta * 0.1
    #return propina

if __name__ == '__main__':
    costo_factura = int(input("Digite el Valor de la Cuenta: "))
    print(type(costo_factura))
    (iva, propina) = calcular_iva_propina_total_factura(costo_factura)
    ivar = round(iva,2)
    propinar = round(propina,2)
    total_cuenta = costo_factura + ivar + propinar
    total = round(total_cuenta, 2)
    
    print("El valor del IVA es:",ivar,", el valor de la Propina es:",propinar,", el valor TOTAL de la Factura es:",total)