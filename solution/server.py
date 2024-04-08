from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
# Base de datos simulada de 
characters= {}


# Junior
class Character:
    def __init__(self):
       self.name=None
       self.level=None
       self.role=None
       self.charisma=None
       self.strength=None
       self.dexterity=None

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, Role: {self.role},Charisma{self.charisma},Strength{self.strength},Dexterity{self.dexterity} "

# Builder: Constructor de pizzas
class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self, name):
        self.character.name = name
    def set_level(self, level):
        self.character.level = level
    def set_role(self, role):
        self.character.role = role
    def set_charisma(self, charisma):
        self.character.charisma = charisma
    def set_strength(self, strength):
        self.character.strength = strength
    def set_dexterity(self, dexterity):
        self.character.dexterity = dexterity
    def get_character(self):
        return self.character

# 
class EmpresaVideojuego:
    def __init__(self, builder):
        self.builder = builder

    def create_character(self, name,level,role,charisma,strength,dexterity):
        self.builder.set_name(name)
        self.builder.set_level(level)
        self.builder.set_role(role)
        self.builder.set_charisma(charisma) 
        self.builder.set_strength(strength)
        self.builder.set_dexterity(dexterity)
        
        return self.builder.get_character()


# Aplicando el principio de responsabilidad única (S de SOLID)
class CharacterService:
    #Llama a todos los respo
    def __init__(self):
        self.builder = CharacterBuilder()
        self.empresaVideojuego = EmpresaVideojuego(self.builder)
        #self.characters = characters

    def create_character(self, post_data):
        name = post_data.get("name", None)
        level = post_data.get("level", None)
        name = post_data.get("name", None)
        role = post_data.get("role", None)
        charisma = post_data.get("charisma", None)
        strength = post_data.get("strength", None)
        dexterity = post_data.get("dexterity", None)
        character = self.empresaVideojuego.create_character(name,level,role,charisma,strength,dexterity)
        characters[len(characters) + 1] = character
        
         
        """character = self.empresaVideojuego.create_character(name,level,role,charisma,strength,dexterity)
        self.characters.append(character.__dict__)
"""
        return character

    def read_characters(self):
        #averiguar for index, pizza in pizzas.items()} que tipo de for es 
        return {index: character.__dict__ for index, character in characters.items()}
     
    def read_characters_por_rol_level_charisma(self, rol,level,charisma):
        return [character for character in self.characters if character['rol'] == rol and character['level']==level and character['charisma']==charisma]
    
    
    
    
    def update_character(self, index, post_data):
        if index in characters:
            character = characters[index]
            charisma = post_data.get("charisma", None)
            strength = post_data.get("strength", None)
            dexterity = post_data.get("dexterity", None)
        #Si emcuentra el kind despues lo pone en vacio
            
            if charisma:
                character.charisma = charisma
            if strength:
                character.strength = strength
            if dexterity:
                character.dexterity = dexterity
            
            return character 
        else:
            return None

    def delete_character(self, index):
        if index in characters:
            return characters.pop(index)
        else:
            return None

#para hacer de S SOLID 
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


# Manejador de solicitudes HTTP
class CharacterHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controller = CharacterService()
        super().__init__(*args, **kwargs)
   
   #todos en plural en el objetos 
   
    def do_POST(self):
        if self.path == "/characters":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.create_character(data)
            HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        if self.path == "/characters":
            response_data = self.controller.read_characters()
            HTTPDataHandler.handle_response(self, 200, response_data)
         
        elif self.path.startswith("/characters") and "rol" and "level" and "charisma" in query_params:            
            rol = query_params["rol"][3]
            level = query_params["level"][4]
            charisma = query_params["charisma"][5]
            characters_solucion = self.controller.read_characters_por_rol_level_charisma(rol,level,charisma)                
            if characters_solucion:
                HTTPDataHandler.handle_response(self, 200, characters_solucion)
            else:
                HTTPDataHandler.handle_response(self, 204, [])  
        
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

        

      #split es una cadena es partir las cadenas 
    def do_PUT(self): #actulir por id 
        if self.path.startswith("/characters/"):
            index = int(self.path.split("/")[2])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.controller.update_character(index, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de pizza no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})
  #Pizza Services y lo ponemos controller
    def do_DELETE(self):
        if self.path.startswith("/characters/"):
            index = int(self.path.split("/")[2])
            deleted_character = self.controller.delete_character(index)
            if deleted_character:
                HTTPDataHandler.handle_response(
                    self, 200, {"message": "Character with id 3 has been deleted successfully"}
                )
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"Error": "Índice de pizza no válido"}
                )
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})


def run(server_class=HTTPServer, handler_class=CharacterHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()





""" def do_GET(self):
        if self.path == "/characters":
            response_data = self.controller.read_characters()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})
"""  