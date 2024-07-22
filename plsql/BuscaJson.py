import json
import os

class BuscaJson:
    def __init__(self, json_file):
        # Construir la ruta completa del archivo JSON
        script_dir = os.path.dirname(__file__)  # Directorio del script actual
        self.json_file = os.path.join(script_dir, json_file)
        self.plsql_blocks = self.load_json()
        self.id=0
        self.description=""
        self.code=""

    def load_json(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        return data['plsql_blocks']

    def find_code_by_id(self, id):
        for block in self.plsql_blocks:
            if block['id'] == id:
                return block['code']
        return None

    def find_descripcion_by_id(self, id):
        for block in self.plsql_blocks:
            if block['id'] == id:
                return block['description']
        return None
    
    def find_by_id(self,id):
        for block in self.plsql_blocks:
            if block['id'] == id:
                self.id=id
                self.description=block['description']
                self.code=block['code']
                return None
                
    def getDescripcion(self):
        return self.description
    
    def getCode(self):
        return self.code