numbers = [1, 2, 3, 4]
results = []
compresion = []
for n in numbers:
    results.append(n + 1)
    
compresion = [n for n in numbers]    
print(results)
print(compresion)