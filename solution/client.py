import requests

url = "http://localhost:8000/characters"
headers = {'Content-type': 'application/json'}

# POST /characters 
mi_characters = {
    "name": "Gandalf",
    "level": 10,
    "role": "Wizard",
    "charisma": 15,
    "strength": 10 ,
    "dexterity": 10,
    
}
response = requests.post(url, json=mi_characters, headers=headers)
print(response.json())

# GET /haracters
response = requests.get(url)
print(response.json())







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