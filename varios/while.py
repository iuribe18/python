# while something_is_true:
    # Do Something repetedly

# secret_number = 3
# guess = int(input("Guess a Number: "))
# while guess != secret_number:
#     guess = int(input("Guess a Number: "))
# else:
#     print("Congratulations, you got it")

i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1
print("\n\n")

# x = 1
# while ( x <= 5 ):
#   x += 1
# print(x)
# print("\n\n")

y = 2
while True:
    if y%3 == 0:
        break
    print(y)
    y += 2
print("\n\n")

z = 5
while True:
    if z % 0o11 == 0:
        break
    print(z)
    z += 1
print("\n\n")

# x = 0
# while (x < 50):
#   x+=2
# print(x)
# print("\n\n")

# x = 1
# while ( x < 20 ):
#  x = x * 2
# print(x)

i = 1
x = 3
sum = 0
while ( i <= x ):
 print("i=", i, "x=", x, "sum=", sum)
 sum += i
 i += 1
print(sum)