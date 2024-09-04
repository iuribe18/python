# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
# Example
# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']
# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results[2,1,0].

import math
import os
import random
import re
import sys

# Complete the 'matchingStrings' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries

def matchingStrings(strings, queries):
    # Create a dictionary to count the occurrences of each string in 'strings'
    string_count = {}
    
    # Count the occurrences of each string in 'strings' 
    for s in strings:
        if s in string_count:
            string_count[s] += 1
        else:
            string_count[s] = 1
    
    # Para cada query, obtenemos el número de veces que aparece en 'strings'
    # For each query, we get the number of times it appears in 'strings'
    results = []
    for q in queries:
        results.append(string_count.get(q, 0))
    return results

if __name__ == '__main__':
    print("Bienvenido al programa de búsqueda de coincidencias de strings...!!!")
    #strings_count = int(input().strip())
    strings_count = int(input("Por favor, ingresa el número de strings: ").strip())
    print(f"Ingrese los {strings_count} strings uno por uno: ")

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    #queries_count = int(input().strip())
    #queries_count = int(input("Por favor, ingresa el número de consultas (queries): ").strip())
    queries_count = int(input("Por favor, ingresa el número de consultas (queries): "))
    print(f"Ingrese las {queries_count} consultas uno por uno:")

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print("\nResultados:")
    print('\n'.join(map(str, res)))

### Version 2
# if __name__ == '__main__':
#     print("Bienvenido al programa de búsqueda de coincidencias de strings...!!!")
#     with open('output.txt', 'w') as fptr:
#         #strings_count = int(input().strip())
#         strings_count = int(input("Por favor, ingresa el número de strings: ").strip())
#         print(f"Ingrese los {strings_count} strings uno por uno: ")

#         strings = []

#         for _ in range(strings_count):
#             strings_item = input()
#             strings.append(strings_item)

#         queries_count = int(input().strip())

#         queries = []

#         for _ in range(queries_count):
#             queries_item = input()
#             queries.append(queries_item)

#         res = matchingStrings(strings, queries)

#         fptr.write('\n'.join(map(str, res)))
#         fptr.write('\n')
