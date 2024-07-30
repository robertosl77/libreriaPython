import schedule
import time
from Tiempo import Tiempo
from RunPlSql import RunPlSql  # Asegúrate de que el nombre del archivo donde está la clase sea 'run_pl_sql.py'

class Programador:
    def __init__(self, intervalo):
        self.plsql = RunPlSql()
        self.tiempo = Tiempo()
        self.intervalo=intervalo
        self.tarea_ejecutada=False
        
    def inicia_programacion(self):
        #1 calculo proxima ejecucion
        proximo= self.__calcula_tiempo()
        #2 programo evento
        schedule.every(proximo).seconds.do(self.__ejecuta_tarea)
        self.tarea_ejecutada=False
        self.__espera_evento()
        schedule.clear()
        #3 ejecuta tarea 
        # self.__ejecuta_tarea()
        #4 reejecuto
        self.inicia_programacion()

    def __calcula_tiempo(self):
        self.tarea_ejecutada=True
        self.tiempo.calcula_proximo(self.intervalo)
        return self.tiempo.devuelve_segundos_restantes()

    def __espera_evento(self):
        while True:
            schedule.run_pending()
            if self.tarea_ejecutada:
                break
            time.sleep(1)
    
    def __ejecuta_tarea(self):
        # Aquí va la lógica para ejecutar periódicamente
        self.plsql.ejecutaPlSql()
        # 
        self.tarea_ejecutada=True


if __name__ == "__main__":
    scheduler = Programador(1)
    scheduler.inicia_programacion()
