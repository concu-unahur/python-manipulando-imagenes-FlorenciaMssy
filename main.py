import logging
from api import PixabayAPI
import threading
from concatenacion import concatenar_horizontal, concatenar_vertical

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'

query = input('Imagenes sobre que queres bajar?\n')
cantidad = (input(f"Que cantidad de imagenes de {query} queres bajar?\n"))
api = PixabayAPI('15323593-4886427c532904360a1070940', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cantidad)

for i in api.imagenes_descargadas:

  api.descargar_imagen(i)
  logging.info(f'Descargando {i}')
  print(api.imagenes_descargadas)

  #concatenar_horizontal(api.imagenes_descargadas)
