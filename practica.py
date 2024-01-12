## Buscador nº de serie ##

'''
Recorrer todas las carpetas y ficheros de "Mi gran directorio". Utilizando el módulo OS y método walk().
El formato de nº de serie es --> - [N] + [tres carateres de texto] + [-] + [5 números] Ejemplo : 'Nryu-12365'.

Representar en una tabla (usar \t para tabular y hacer una tabla de buenas maneras):
    - Fecha de la búsqueda actual con formato dd/mm/aa
    - archivo con el n.º de serie.
    - archivos encontrados.
    - Duración de la búsqueda. (redondeada siempre hacia arriba). Módulo time

    ej:
        Fecha de búsqueda: [fecha de hoy]

        ARCHIVO		NRO. SERIE
        -------		----------
        texto1.txt	Nter-15496
        texto25.txt	Ngba-85235

        Números encontrados: 2
        Duración de la búsqueda: 1 segundos
'''
import re
import time
from _datetime import datetime
import os
import math

keyword = r'N\w{3}-\d{5}'


def fecha_actual():
    # devuelve la fecha en formato dd/mm/aa
    fecha = datetime.now()
    return fecha.strftime("%d/%m/%y")


ruta = '/Users/alejandrobueno/Documents/DAW/Cursos,ejercicios,' \
       'proyectos/Python/PythonTOTAL/Day9/PracticaDay9/Mi_Gran_Directorio'

print(f'Fecha de búsqueda: {fecha_actual()}\n')
print('ARCHIVO\t\t\tNRO. SERIE')
contador = 0
inicio = time.time()
for carpeta, subcarpeta, archivos in os.walk(ruta):
    for arch in archivos:
        ruta_completa = os.path.join(carpeta, arch)

        with open(ruta_completa, 'r', encoding='latin-1') as abrir_archivo:
            contenido = abrir_archivo.read()
            coincidencias = re.findall(keyword, contenido)

            if coincidencias:
                contador += 1
                print(f'{arch}\t{coincidencias}')

final = time.time()
resultado = final - inicio
resultado = math.ceil(resultado)

print('\n')
print(f'Archivos encontrados:\t {contador}')
print(f'Duración de la búsqueda: {resultado} segundos')
