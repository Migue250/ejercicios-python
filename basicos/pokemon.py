import requests

nombre = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"  

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    
    nombre_pokemon = data['name'].capitalize()
    id_pokemon = data['id']

    print(f"Nombre: {nombre_pokemon}")
    print(f"ID: {id_pokemon}")
else:
    print("Error: No se pudo obtener la información del Pokémon.")

    
