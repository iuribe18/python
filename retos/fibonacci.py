print("Welcome to Fibonacci...!!!")
n = int(input("Limite de Fibonacci: "))

def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor a 0"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            print("Último Elemento: ", fib_series[-1])
            fib_series.append(fib_series[-1] + fib_series[-2])
            # n = 3
            # fib_series[-1] es 1 (último elemento de la lista)
            # fib_series[-2] es 0 (penúltimo elemento de la lista)
            # La suma es 1, lo adiciona a la lista fib_series = [0, 1, 1]
            # n = 4
            # fib_series[-1] es 1 (último elemento de la lista)
            # fib_series[-2] es 1 (penúltimo elemento de la lista)
            # La suma es 2, lo adiciona a la lista fib_series = [0, 1, 1, 2]
            # n = 5
            # fib_series[-1] es 2 (último elemento de la lista)
            # fib_series[-2] es 1 (penúltimo elemento de la lista)
            # La suma es 3, lo adiciona a la lista fib_series = [0, 1, 1, 2, 3]
            # n = 6
            # fib_series[-1] es 3 (último elemento de la lista)
            # fib_series[-2] es 2 (penúltimo elemento de la lista)
            # La suma es 5, lo adiciona a la lista fib_series = [0, 1, 1, 2, 3, 5]
            
        return fib_series

# Ejemplo de uso
print(f"La serie Fibonacci hasta el {n}-ésimo término es:")
print(fibonacci(n))