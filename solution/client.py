import requests

url = "http://localhost:8000/characters"
headers = {'Content-type': 'application/json'}

# POST /char 
mi_characters = {
    "name": "Gandalf",
    "level": 10,
    "role": "Wizard",
    "charisma": 15,
    "strength": 10 ,
    "dexterity": 10
    
}
response = requests.post(url, json=mi_characters, headers=headers)
print(response.json())
#response = requests.get(url)
#print(response.json())
#POST
mi_characters = {
    "name": "Robin",
    "level": 5,
    "role": "Archer",
    "charisma": 10,
    "strength": 10 ,
    "dexterity": 10
    
}
response = requests.post(url, json=mi_characters, headers=headers)

response = requests.get(f"{url}/{1}")
print(response.json())


mi_characters = {
    "name": "Juan",
    "level": 12,
    "role": "Inge",
    "charisma": 20,
    "strength": 30 ,
    "dexterity": 30
    
}
response = requests.post(url, json=mi_characters, headers=headers)



print("ACTUALIZAR")
edit_character= {
    "charisma": 20,
    "strength": 15 ,
    "dexterity": 15
}
response = requests.put(f"{url}/{2}", json=edit_character, headers=headers)
print(response.json())



print("--- DELETE pacinte ---")
ci = 3
response_delete = requests.delete(f"{url}/{ci}")
print(response_delete.json())
mi_characters = {
    "name": "Legolas",
    "level": 5,
    "role": "Archer",
    "charisma": 15,
    "strength": 10,
    "dexterity": 10
    
}
response = requests.post(url, json=mi_characters, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())








"""
print("--- PUT paciente con CI---")
ci = 456789
actualizacion_paciente = {
    "edad": 60,
    "doctor": "Doctor Pedro Perez",
}
response = requests.put(f"{url}/{ci}", json=actualizacion_paciente)
print(response.text)
"""


"""# PUT /pizzas/1
edit_pizza = {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Queso"]
}
response = requests.put(url, json=edit_pizza, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())"""