lista = ["https://www.rei.com/c/mountain-bike-helmets", "https://www.rei.com/b/arcteryx/c/mens-insulated-jackets?ir=brand%3Aarcteryx%3Bcategory%3Amens-clothing&r=b%3Bcategory%3Amens-clothing%7Cmens-"
"jackets%7Cmens-insulated-jackets"]
nueva_lista = []

urls = []  # Inicializa una lista vacía para almacenar las URLs completas
current_url = ""  # Inicializa una cadena vacía para construir la URL actual

# Itera sobre cada línea del archivo
for line in lista:
    # Elimina todos los caracteres de espacio en blanco del inicio y final de la línea
    stripped_line = line.strip()
    print(f"Striped_line: {stripped_line}")
    if stripped_line == "":  # Si la línea no está vacía después de eliminar los espacios
        if current_url != "":  # Si ya hay contenido en current_url (es decir, estamos construyendo una URL fragmentada)
            current_url += stripped_line  # Añade la línea actual a current_url
            print(f"Current_line: {current_url}")
        else:  # Si current_url está vacía, esto significa que es el comienzo de una nueva URL
            current_url = stripped_line  # Asigna la línea actual a current_url
    else:  # Si la línea está vacía (es decir, encontramos una línea en blanco)
        current_url = ""  # Reinicia current_url para empezar a construir la siguiente URL
        nueva_lista.append(line)

# Si current_url contiene algo al final del archivo, añádelo a la lista de URLs
#if current_url:
    #urls.append(current_url)




# for i in lista:
#     stripped_line = i.strip()
#     nueva_lista.append(i.strip()) 
#print(lista)
print("\n")
print(nueva_lista)