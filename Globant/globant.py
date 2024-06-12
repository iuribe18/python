# Land managers
land_managers = [
    { "id": 1, "internalNumber": "123456789", "name": "RAFAEL MORALES SOTO" },
    { "id": 2, "internalNumber": "123456788", "name": "FERNANDO PINTO VARELA" },
    { "id": 3, "internalNumber": "123456787", "name": "ANDRES ROJAS PEÑA" },
    { "id": 4, "internalNumber": "123456786", "name": "MANUEL SALAS ORTIZ" },
    { "id": 5, "internalNumber": "123456785", "name": "MARIO ZUÑIGA ROMERO" },
    { "id": 6, "internalNumber": "123456784", "name": "JOSE ALFARO MOLINA" }
]

# Land type, describe what product is going to be harvested
landType = [
    { "id": 1, "name": 'APPLE' },
    { "id": 2, "name": 'ORANGE' },
    { "id": 3, "name": 'BANANA' },
    { "id": 4, "name": 'PEACH' },
]

# A land is a farm that will be harvested
lands = [
    {"landManagerId": 5, "farmId": 2, "landTypeId": 4, "harvestYear": 2020, "area": 200},
    {"landManagerId": 4, "farmId": 1, "landTypeId": 2, "harvestYear": 2018, "area": 1500},
    {"landManagerId": 6, "farmId": 1, "landTypeId": 3, "harvestYear": 2021, "area": 2000},
    {"landManagerId": 1, "farmId": 2, "landTypeId": 4, "harvestYear": 2020, "area": 4405},
    {"landManagerId": 2, "farmId": 3, "landTypeId": 2, "harvestYear": 2022, "area": 4875},
    {"landManagerId": 3, "farmId": 3, "landTypeId": 2, "harvestYear": 2018, "area": 1905},
    {"landManagerId": 2, "farmId": 2, "landTypeId": 1, "harvestYear": 2017, "area": 10735},
    {"landManagerId": 1, "farmId": 1, "landTypeId": 4, "harvestYear": 2022, "area": 2525},
    {"landManagerId": 6, "farmId": 1, "landTypeId": 3, "harvestYear": 2019, "area": 1555},
    {"landManagerId": 3, "farmId": 2, "landTypeId": 2, "harvestYear": 2016, "area": 400},
    {"landManagerId": 4, "farmId": 1, "landTypeId": 2, "harvestYear": 2017, "area": 3255},
    {"landManagerId": 6, "farmId": 2, "landTypeId": 1, "harvestYear": 2022, "area": 725},
    {"landManagerId": 5, "farmId": 3, "landTypeId": 2, "harvestYear": 2020, "area": 12565},
    {"landManagerId": 1, "farmId": 1, "landTypeId": 2, "harvestYear": 2022, "area": 5000},
    {"landManagerId": 2, "farmId": 2, "landTypeId": 4, "harvestYear": 2021, "area": 23215},
    {"landManagerId": 2, "farmId": 2, "landTypeId": 3, "harvestYear": 2018, "area": 7125},
    {"landManagerId": 3, "farmId": 3, "landTypeId": 3, "harvestYear": 2021, "area": 300},
    {"landManagerId": 1, "farmId": 3, "landTypeId": 2, "harvestYear": 2018, "area": 3235},
    {"landManagerId": 4, "farmId": 1, "landTypeId": 1, "harvestYear": 2019, "area": 13255},
    {"landManagerId": 4, "farmId": 2, "landTypeId": 2, "harvestYear": 2021, "area": 3120},
    {"landManagerId": 5, "farmId": 2, "landTypeId": 2, "harvestYear": 2018, "area": 5300},
    {"landManagerId": 3, "farmId": 3, "landTypeId": 3, "harvestYear": 2019, "area": 20340},
    {"landManagerId": 6, "farmId": 3, "landTypeId": 4, "harvestYear": 2020, "area": 24235}
]

farms = [
    {"id": 1, "name": "Glo Land"},
    {"id": 2, "name": "Chicken Land"},
    {"id": 3, "name": "Wonderful Land"}
]

## Return an array with the ids of the managers of each land
# def listLandManagerIds():
#     manager_ids = []
#     for land in lands:
#         manager_ids.append(land["landManagerId"])
#     return manager_ids

# Using List Comprehension
def listLandManagerIds():
    manager_ids = [land["landManagerId"] for land in lands]
    return manager_ids

# Return an array with the internal number of the managers of the lands, sorted by name
def listLandManagersByName():
    # Sort the list of dictionaries by the "name" key
    # Get internal Numbers sorted by administrator name
    # Sort the list of dictionaries by the "name" key
    #land_type = sorted(land_managers, key=lambda x: x["name"])
    sorted_internal_numbers = [manager['internalNumber'] for manager in sorted(land_managers, key=lambda x: x['name'])]
    return sorted_internal_numbers

# Return an Array with the names of each land type, sorted dec by the total sum of the harvested hectares of each of them
# Tip: one hectare is 10.000m2
# Steps
# 1. Crear un diccionario para almacenar la suma de las áreas cosechadas por cada tipo de tierra
# 2. Iterar sobre la lista de lands y acumular el área cosechada para cada landTypeId
# 3. Mapear los landTypeId a sus respectivos nombres usando la lista landType
# 4. Ordenar los resultados en orden decreciente por la suma de las áreas cosechadas
# 5. Devolver un arreglo con los nombres de los tipos de tierras ordenados

# Función para obtener el nombre de tipo de tierra a partir de su ID
def get_landtype_name(landTypeId):
    ''' Returns the name of the land type with the given ID '''
    for land in landType:
        if land['id'] == landTypeId:
            return land['name']
    return None

# Función para calcular la suma total de hectáreas cosechadas para cada tipo de tierra
def calculate_total_hectares(lands):
    ''' Returns a dictionary with the total sum of hectares harvested for each land type '''
    total_hectares = {}
    for land in lands:
        land_type_name = get_landtype_name(land['landTypeId'])
        if land_type_name:
            if land_type_name not in total_hectares:
                total_hectares[land_type_name] = 0
            total_hectares[land_type_name] += land['area'] / 10000  # Convert hectares to m2
    return total_hectares

# Función principal para obtener los nombres de los tipos de tierra ordenados por la suma total de hectáreas cosechadas
def get_sorted_land_types(lands):
    total_hectares = calculate_total_hectares(lands)
    sorted_land_types = sorted(total_hectares.items(), key=lambda x: x[1], reverse=True)
    return [land_type[0] for land_type in sorted_land_types]

## Return an array with the names of the land managers, sorted dec by the total sum of the hectares that they manage
# Función para obtener el nombre de un administrador a partir de su ID
def get_land_manager_name(landManagerId):
    ''' Returns the name of the manager with the given ID '''
    for manager in land_managers:
        if manager['id'] == landManagerId:
            return manager['name']
    return None

# Función para calcular la suma total de hectáreas cosechadas par cada administrador
def calculate_total_hectares(lands):
    ''' Returns a dictionary with the total sum of hectares harvested for each manager '''
    total_hectares = {}
    for land in lands:
        manager_name = get_land_manager_name(land['landTypeId'])
        if manager_name:
            if manager_name not in total_hectares:
                total_hectares[manager_name] = 0
            total_hectares[manager_name] += land['area'] / 10000  # Convert hectares to m2
    return total_hectares

# Test the function
print("Array with the ids of the managers of each land")
print(listLandManagerIds())
print("\n")
print("Array with the internal number of the managers, sorted by name")
print(listLandManagersByName())
print("\n")
print("Array with the names of each land type, sorted dec by the total sum of the harvested hectares of each of them")
print(calculate_total_hectares(lands))
sorted_land_types = get_sorted_land_types(lands)
print(sorted_land_types)
print("\n")
print("Array with the names of the land managers, sorted dec by the total sum of the hectares that they manage")
print(get_land_manager_name(1))
print(calculate_total_hectares(lands))