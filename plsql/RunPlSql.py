import os
from bd.oracle import OracleDB
from BuscaJson import BuscaJson


class RunPlSql:

    def __init__(self):
        self.db = OracleDB()

    def ejecutaPlSql(self):
        self.clear_console()
        finder = BuscaJson('plsql.json')
        finder.find_by_id(7)
        print(finder.getDescripcion())
        self.db.connect()
        output = self.db.execute_plsql(finder.getCode())
        self.db.close()
        
        if output!=None:
            for line in output:
                print(line)
                
    def clear_console(self):
        # Verificar el sistema operativo y ejecutar el comando correspondiente
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para Unix/Linux/MacOS
            os.system('clear')                

if __name__ == "__main__":
    run_package = RunPlSql()
    run_package.ejecutaPlSql()
