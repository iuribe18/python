# Los slices (o rebanadas) en Python son una forma poderosa de acceder a subconjuntos de elementos en secuencias, como listas, cadenas de texto, tuplas, etc. La sintaxis básica de un slice es:

# sequence[start:stop:step]
# Componentes de un slice
# start (opcional): El índice donde comienza el slice. El elemento en este índice está incluido en el resultado. Si no se especifica, se asume que es 0 (el inicio de la secuencia).
# stop: El índice donde termina el slice. El elemento en este índice no está incluido en el resultado. Si no se especifica, se asume que es el final de la secuencia.
# step (opcional): El paso entre cada índice del slice. Si no se especifica, se asume que es 1.

lista = [0, 1, 2, 3, 4, 5]
print("Básico: " + str(lista[1:4]))
# start = 1: Comienza en el índice 1 (valor 1).
# stop = 4: Termina antes del índice 4 (valor 4 no se incluye).
# Resultado: [1, 2, 3]

# Sin start (comienza desde el principio):
print("Sin Start: " + str(lista[:3]))
print("Sin Start: " + str(lista[:5]))
print("Sin Start Con negativos", lista[:-1])
# No se especifica start, comienza en 0.
# stop = 3: Termina antes del índice 3.
# Resultado: [0, 1, 2]

# Sin stop (hasta el final):
print(f"Sin Stop: {lista[3:]}")
# start = 3: Comienza en el índice 3.
# No se especifica stop, sigue hasta el final de la lista.
# Resultado: [3, 4, 5]

# Con step:
print(f"Con Step: {lista[1:6:2]}")
# start = 1: Comienza en el índice 1.
# stop = 6: Termina antes del índice 6.
# step = 2: Avanza cada 2 elementos.
# Resultado: [1, 3, 5]

# Slice con pasos negativos (inverso):
print("Con negativos", lista[::-1])
# No se especifican start ni stop, toma toda la lista.
# step = -1: Avanza en orden inverso.
# Resultado: [5, 4, 3, 2, 1, 0]

# Omitir start, stop, y step:
print("Lista Completa: ", lista[:])
# Copia completa de la lista, ya que no se omite nada.
# Resultado: [0, 1, 2, 3, 4, 5]

# Slices en cadenas de texto:
# Los slices también funcionan en cadenas de texto de la misma manera.
texto = "Hola Mundo"
print(texto[0:4])
# Resultado: 'Hola'

# Importante
# Los índices pueden ser negativos, donde -1 es el último elemento, -2 es el penúltimo, y así sucesivamente.
# Si start es mayor que stop y step es positivo, el resultado será una lista vacía. Para recorrer al revés, usa un step negativo.