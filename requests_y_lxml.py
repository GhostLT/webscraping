"""
OBJETIVO: 
  - Extraer los titulos de Wikipedia
  - Aprender a utilizar requests para parsear el arbol HTML
CREADO POR: JAVIER VIVEROS
ULTIMA VEZ EDITADO: 14 SEP 2022
"""

import requests

# USER AGENT PARA PROTEGERNOS DE BANEOS, ENCABEZADOS DE QUIEN ESTA HACIENDO EL REQUERIMIENTO, CASO CONTRARIO ES ROBOT
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

# URL SEMILLA
url = 'https://www.wikipedia.org/'

# REQUERIMIENTO AL SERVIDOR WIKIPEDIA
# respuesta = arbol HTML
# PASAMOS EL DICCIONARIO DE ENCABEZADOS
respuesta = requests.get(url, headers=headers)


print(respuesta.text)
