import schedule
import time
from RunPlSql import RunPlSql  # Asegúrate de que el nombre del archivo donde está la clase sea 'run_pl_sql.py'

class Main:
    def __init__(self):
        self.runner = RunPlSql()
        self.ejecuta_periodicamente()

    def ejecuta_periodicamente(self):
        self.runner.ejecutaPlSql()

    def start_scheduler(self):
        tiempo=15
        schedule.every(tiempo).minutes.do(self.ejecuta_periodicamente)
        print(f"\nProxima ejecucion dentro de {tiempo} minutos.")
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main = Main()
    main.start_scheduler()
