#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
from colorama import *
#######################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ nuevo(0,estado='inicio',modulo=4)
import math
import datetime
#######################################################################################################
limpiar()
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Educacion IT                                 ║
║                                                                             ║
║                                   clase V                                   ║
║                                                                             ║
║                                 Programming                                 ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣\033[0;m
║                                                                             ║
║  ╔═════╗   ╔═════╗   ╔════╗   ╦      ╦  ╔═════╗   ╔════╗  ╔══╦══╗  ╔════╗   ║
║  ║     ╚╗  ║        ╔╝    ╚╗  ║      ║  ║        ╔╝    ╚╗    ║    ╔╝    ╚╗  ║
║  ║      ║  ║        ║      ║  ║      ║  ║        ║           ║    ║         ║
║  ║     ╔╝  ║        ║      ║  ║      ║  ║        ╚╗          ║    ╚╗        ║
║  ╠═╦═══╝   ╠═══╣    ║      ║  ║      ║  ╠═══╣     ╚════╗     ║     ╚════╗   ║
║  ║ ╚═╗     ║        ║      ║  ║      ║  ║              ╚╗    ║          ╚╗  ║
║  ║   ╚═╗   ║        ╚╗    ╔╣  ╚╗    ╔╝  ║        ╚╗    ╔╝    ║    ╚╗    ╔╝  ║
║  ╩     ╚═  ╚═════╝   ╚════╝╚   ╚════╝   ╚═════╝   ╚════╝     ╩     ╚════╝   ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                        REpresentational State Transfer                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");


pausa()
import json

try:
    import requests
except Exception as error_:
    import pip
    pip.main(['install', 'requests'])
import requests
def clima():

    #                   Clima weather map
    #                                                                               api con respuesta con api key

    #https://openweathermap.org/current

    apiKey = "8f7731766827fc49ebeb1991c47baa91"#32 caracteres
    # ~ cityId = "3435910";
    # ~ city="Esquel"

    #"https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"
    # ~ city="Cordoba"
    #https://home.openweathermap.org/

    listaciudades = [
                    "Buenos Aires",
                    "Chaco",
                    "Resistencia",
                    "Esquel",
                    "Cordoba",
                    "Oslo",
                    "Haedo",
                    "Madrid",
                    "Sevilla"
                    ]
    for city in listaciudades:
        print ("registrarse en https://home.openweathermap.org/users/sign_in ")
        # ~ url = f"http://api.openweathermap.org/data/2.5/weather?id={cityId}&lang=en&units=metric&APPID={apiKey}"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
        print(F"""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║                                    Requests                                 ║
        ║{url.center(77)}║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        res = requests.get(url)
        #https://openweathermap.org/find
        print (f"{res=}")

        print(f"{res.status_code=}   {type(res.status_code)=}")
        if res.status_code != 200:
            print ("error de comunicacion con la api")
            exit()


        elif res.status_code==200:
            print("\033[1;37;44m\n"+"="*80+f"{city}\033[0;m")
            dicc=  res.json()
            print (dicc)
            for clave, valor in dicc.items():
                print(f"{clave=}:")
                if isinstance(valor, dict):
                    for sub_clave, sub_valor in valor.items():
                        print (f"           { sub_clave=}   {sub_valor=}")
                elif isinstance(valor, (list,tuple)):
                    for index_, sub_valor in enumerate(valor):
                        print (f"           { sub_clave=}   {sub_valor=}")
                else:
                    print (f"           {valor=}")
                #{'coord': {'lon': 10.7461, 'lat': 59.9127}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 2.67, 'feels_like': -0.36, 'temp_min': 1.55, 'temp_max': 3.72, 'pressure': 1000, 'humidity': 89, 'sea_level': 1000, 'grnd_level': 997}, 'visibility': 10000, 'wind': {'speed': 3.08, 'deg': 354, 'gust': 8.43}, 'clouds': {'all': 100}, 'dt': 1699655618, 'sys': {'type': 1, 'id': 1624, 'country': 'NO', 'sunrise': 1699599638, 'sunset': 1699628474}, 'timezone': 3600, 'id': 3143244, 'name': 'Oslo', 'cod': 200}

            # ~ for clave, valor in res.json().items():
                # ~ print(clave, valor)
            # ~ print("\033[1;37;44m\n"+"="*80+f"{city}\033[0;m")
            # ~ print(f'{res.json()["weather"][0]["main"]=}')
            # ~ print(f'{res.json()["main"]["temp_min"]=}')

            print(f'{dicc["weather"][0]["main"]=}')
            print(f'{dicc["main"]["temp_min"]=}')
            print("\033[1;37;44m\n"+"*"*120+f"\033[0;m")
# ~ clima()
# ~ exit()

#######################################################################################################


def bcra():
    #                   Banco Central de la Republica Argentina
    #                                                                               api con respuesta con token
    #http://estadisticasbcra.com/api/documentacion")
    token="""BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTI5NDkwNDgsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJjdXJzb3MuYWd0QGdtYWlsLmNvbSJ9.wYHVfj6G9tJro_zjjJMJKgFP5X4xZ7eOe0qz39Okr9LRm0YWBXJiIauKkum2xdtW_2jpdY9m2QDgMYOCFlTXbA"""
    # ~ res= requests.get("https://scotch.io")
    #endpoint al que se llama (Ver listado de endpoints)
    # ~ endpoint = "usd"
    print("https://estadisticasbcra.com/api/documentacion")

    print ("registrarse en https://estadisticasbcra.com/api/registracion ")
    puntosfinales = [
                    "usd",
                    "usd_of",
                    "usd_of_minorista",
                    "var_usd_vs_usd_of",
                    "tasa_prestamos_personales"
                    ]
    for endpoint in puntosfinales:
        #datos para el llamado
        url = f"https://api.estadisticasbcra.com/{endpoint}"
        print(F"""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║                                    Requests                                 ║
        ║{url.center(77)}║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        headers = {"Authorization": token}
        res = requests.get(url, headers=headers)

        print(f"{res.status_code=}   {type(res.status_code)=}")
        if res.status_code != 200:
            print ("pagina caida, token no valido o cantidad de requests superada (max 100 x dia)")
            exit()
        elif res.status_code==200:
            # ~ print(f"{res.json()=}")#todo

            print(f"{res.json()[0]=}")
            print(f"{res.json()[-1]=}")

    '''

    ENDPOINTS : Descripcion
    https://api.estadisticasbcra.com/milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
    https://api.estadisticasbcra.com/base : base monetaria
    https://api.estadisticasbcra.com/base_usd: base monetaria dividida USD
    https://api.estadisticasbcra.com/base_usd_of: base monetaria dividida USD Oficial
    https://api.estadisticasbcra.com/reservas : reservas internacionales
    https://api.estadisticasbcra.com/base_div_res : base monetaria dividida reservas internacionales
    https://api.estadisticasbcra.com/usd : cotización del USD
    https://api.estadisticasbcra.com/usd_of : cotización del USD Oficial
    https://api.estadisticasbcra.com/usd_of_minorista : cotización del USD Oficial (Minorista)
    https://api.estadisticasbcra.com/var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
    https://api.estadisticasbcra.com/circulacion_monetaria : circulación monetaria
    https://api.estadisticasbcra.com/billetes_y_monedas : billetes y monedas
    https://api.estadisticasbcra.com/efectivo_en_ent_fin : efectivo en entidades financieras
    https://api.estadisticasbcra.com/depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
    https://api.estadisticasbcra.com/depositos : depósitos
    https://api.estadisticasbcra.com/cuentas_corrientes : cuentas corrientes
    https://api.estadisticasbcra.com/cajas_ahorro : cajas de ahorro
    https://api.estadisticasbcra.com/plazo_fijo : plazos fijos
    https://api.estadisticasbcra.com/tasa_depositos_30_dias : tasa de interés por depósitos
    /////
    https://api.estadisticasbcra.com/prestamos : prestamos
    https://api.estadisticasbcra.com/tasa_prestamos_personales : tasa préstamos personales
    https://api.estadisticasbcra.com/tasa_adelantos_cuenta_corriente : tasa adelantos cuenta corriente
    https://api.estadisticasbcra.com/porc_prestamos_vs_depositos : porcentaje de prestamos en relación a depósitos
    https://api.estadisticasbcra.com/lebac : LEBACs
    https://api.estadisticasbcra.com/leliq : LELIQs
    https://api.estadisticasbcra.com/lebac_usd : LEBACs en USD
    https://api.estadisticasbcra.com/leliq_usd : LELIQs en USD
    https://api.estadisticasbcra.com/leliq_usd_of : LELIQs en USD Oficial
    https://api.estadisticasbcra.com/tasa_leliq : Tasa de LELIQs
    https://api.estadisticasbcra.com/m2_privado_variacion_mensual : M2 privado variación mensual
    https://api.estadisticasbcra.com/cer : CER
    https://api.estadisticasbcra.com/uva : UVA
    https://api.estadisticasbcra.com/uvi : UVI
    https://api.estadisticasbcra.com/tasa_badlar : tasa BADLAR
    https://api.estadisticasbcra.com/tasa_baibar : tasa BAIBAR
    https://api.estadisticasbcra.com/tasa_tm20 : tasa TM20
    https://api.estadisticasbcra.com/tasa_pase_activas_1_dia : tasa pase activas a 1 día
    https://api.estadisticasbcra.com/tasa_pase_pasivas_1_dia : tasa pase pasivas a 1 día
    https://api.estadisticasbcra.com/inflacion_mensual_oficial : inflación mensual oficial
    https://api.estadisticasbcra.com/inflacion_interanual_oficial : inflación inteanual oficial
    https://api.estadisticasbcra.com/inflacion_esperada_oficial : inflación esperada oficial
    https://api.estadisticasbcra.com/dif_inflacion_esperada_vs_interanual : diferencia entre inflación interanual oficial y esperada
    https://api.estadisticasbcra.com/var_base_monetaria_interanual : variación base monetaria interanual
    https://api.estadisticasbcra.com/var_usd_interanual : variación USD interanual
    https://api.estadisticasbcra.com/var_usd_oficial_interanual : variación USD (Oficial) interanual
    https://api.estadisticasbcra.com/var_merval_interanual : variación merval interanual
    https://api.estadisticasbcra.com/var_usd_anual : variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/var_usd_of_anual : variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/var_merval_anual : variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/merval : MERVAL
    https://api.estadisticasbcra.com/merval_usd : MERVAL dividido cotización del USD
    '''

# ~ bcra()
# ~ exit()
#######################################################################################################
from datetime import datetime
def cripto():

    # ~ https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
    print(F"""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                    Requests                                 ║
    ║{url.center(77)}║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
    """);
    res = requests.get(url)#.encode("utf-8")

    print (f"{res=}")
    print(f"{res.json()[0]=}")
    if res.status_code != 200:
        exit()
    elif res.status_code==200:
        print(f"{res.json()[0]=}")
    for clave in res.json():
        print(f"{clave}")
    for clave,valor in res.json()[-1].items():
        print(clave,valor)
        if 'date' in clave:
            date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
            print (f"\t\t{datetime.strptime(valor, date_format)}")
    print (f"un bitcoin equivale a {res.json()[-1]['current_price']} dolares EEUU")
    # ~ for clave, valor in res.json().items():
        # ~ print(clave, valor)
    #   https://apiip.net/?hsa_acc=2805992144&hsa_cam=16167671195&hsa_grp=131936042606&hsa_ad=581368393853&hsa_src=g&hsa_tgt=kwd-332054273884&hsa_kw=ip+geolocation+api&hsa_mt=e&hsa_net=adwords&hsa_ver=3





    #https://openweathermap.org/current
    # ~ https://ipstack.com/dashboard
    # ~ https://ipstack.com/quickstart
    # ~ apiKey="ee24b9c1b884bb441e3b8fc59a58b7d7"#32 caracteres

    # ~ print ("registrarse en  ")
    # ~ ip="2800:810:542:89a1:997:5045:4ef6:6ce0"
    # ~ url = f"http://api.ipstack.com/{ip}?access_key={apiKey}"
    # ~ res = requests.get(url)
    # ~ print (f"{res=}")
    # ~ for clave, valor in res.json().items():
        # ~ print(clave, valor)

# ~ cripto()
# ~ exit()
#######################################################################################################
'''
tep 2: API Endpoints

Overall, there are 3 different methods of using the ipstack API:

Standard Lookup: Look up the data behind an IP address.
Bulk Lookup: Look up the data behind multiple IP addresses at once.
Requester Lookup: Look up the data behind the IP address your API request is coming from.
Base URL: Whichever API method you choose to use, all API requests to the ipstack API start out with the following base URL:

http://api.ipstack.com/


Make API Request: Let's try making an API request to look up the data behind your own IP address, which is 2800:810:542:89a1:997:5045:4ef6:6ce0. Simply attach it along with your API Access Key to the API's base URL:

http://api.ipstack.com/2800:810:542:89a1:997:5045:4ef6:6ce0?access_key=ee24b9c1b884bb441e3b8fc59a58b7d7

'''
'''
data= '["8.8.4.4", "1.1.1.1", "2c0f:fb50:4003::"]'
headers= "Content-Type: application/json"
url=  "http://ipwhois.pro/bulk?key=YOUR_API_KEY"


res = requests.get(url, headers=headers)


print (f"{res=}")
'''
#######################################################################################################
import re
import json
# ~ from urllib2 import urlopen
ip = ''#8.8.4.4

url = 'http://ipwho.is/'
print(F"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                    Requests                                 ║
║{url.center(77)}║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");
res=requests.get(url+ip)
ipwhois =res.json()

print (f"{ipwhois} \n\npais {ipwhois['country']}")

for clave, valor in ipwhois.items():
    print(clave, valor)


