# Operadores aritméticos
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7

# Multiplication
print(a * b)  # 30

# Division (division operator always returns a float)
print(a / b)  # 3.333...

# Module (residuo de la división)
print(a % b)  # 1

# Exponential
print(a ** b) # 1000

# Floor Division (División entera)
print(a // b) # 3

# Operadores de comparación
print(a == b) # False
print(a != b) # True
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False

# Operadores lógicos
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False

# Operadores de asignación
c = 5
c += 2  # c = c + 2, c es ahora 7
c *= 3  # c = c * 3, c es ahora 21

# Operadores bit a bit
d = 4  # 4 en binario es 100
e = 1  # 1 en binario es 001
print(d & e)  # 0, 100 AND 001 es 000
print(d | e)  # 5, 100 OR 001 es 101
print(d ^ e)  # 5, 100 XOR 001 es 101
print(~d)     # -5, complemento a uno de 4 es -5
print(d << 1) # 8, 100 desplazado a la izquierda es 1000
print(d >> 1) # 2, 100 desplazado a la derecha es 010

# Operadores de pertenencia
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)    # True
print("orange" not in fruits) # True

# Operadores de identidad
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)      # True, z es el mismo objeto que x
print(x is y)      # False, aunque x e y tienen el mismo contenido, no son el mismo objeto
print(x == y)      # True, x e y tienen el mismo contenido