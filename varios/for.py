# for i in range(10):
#     print("i is: ", i)

for i in range(1, 101):  # Rango para incluir 1 a 100
    # if i % 15 == 0:
    #     print("fizzbuzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# x = 'abcd'
# for i in x:
#     print(i)
#     x.upper()

x = 'abcd'
for i in range(len(x)):
    print(i)

for num in range(0, 11):
    if num % 2 == 0:
        continue
    print(num)

frutas = ["manzana", "banana", "cereza"]

for i, fruta in enumerate(frutas):
    print(f"Indice: {i}, Fruta: {fruta}")