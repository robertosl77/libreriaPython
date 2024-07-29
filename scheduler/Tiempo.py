from datetime import datetime, timedelta

class Tiempo:
    def __init__(self) -> None:
        self.programacion=0
    
    def calcula_proximo(self, intervalo):
        """
        Devuelve la siguiente hora/minuto cuyo minuto sea divisor del parámetro minutos_intervalo.
        
        :param minutos_intervalo: Intervalo de minutos en decimal.
        :return: Objeto datetime que representa el siguiente tiempo.
        """
        if self.programacion!=0:
            self.programacion += timedelta(minutes=intervalo)
            print(self.devuelve_leyenda()) 
            return
        
        ahora = datetime.now().replace(second=0, microsecond=0)
        ahora += timedelta(minutes=1)
        
        # Incrementar los minutos hasta que sean divisibles por el intervalo
        while ahora.minute % intervalo != 0:
            ahora += timedelta(minutes=1)        
        
        #Guardo los datos en la variable programacion
        self.programacion=ahora
        print(self.devuelve_leyenda()) 
        
    def devuelve_proximo(self):
        return self.programacion

    def devuelve_segundos_restantes(self):
        return (self.programacion - datetime.now()).seconds
    
    def devuelve_leyenda(self):
        if self.devuelve_segundos_restantes()>=60:
            return f"\nPróxima ejecución a las {self.programacion.strftime('%H:%M')} dentro de {self.devuelve_segundos_restantes()//60} minutos."
        else:
            return f"\nPróxima ejecución a las {self.programacion.strftime('%H:%M')} dentro de {self.devuelve_segundos_restantes()} segundos."