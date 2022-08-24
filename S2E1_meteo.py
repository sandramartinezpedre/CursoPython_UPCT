# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:19:12 2019

@author: Sandra M MartinezPe
"""

def extraerdatos(file_content):
    listadatos = []
    for line in file_content.split('\n'):
        dic = {}
        for item in line.split('-'):
            key=''
            value=''
            status=0                   ### si status vale 0 es clave, sino es valor
            for letra in item:
                if letra == ':':
                    status=1
                else:
                    if status == 0:
                        key += letra
                    else:
                        value += letra
            dic[key]= float(value)
        listadatos += [dic] 
    return listadatos

def organizardatos(listadatos, param):      
    ltemp=[]
    lhum=[]
    lprec=[]
    for item in listadatos:
        ltemp += [item['temp']-273.2]     ### el objeto (item) que se accede a través de 'temp' lo añades a la lista ltemp
        lhum += [item['hum']]
        lprec += [item['rain']]    
    if param == 'temperatura minima':
        tmin= min(ltemp)
        print (tmin)
    elif param == 'temperatura maxima':
        tmax= max(ltemp)
        print (tmax)
    elif param == 'temperatura media':
        tsuma = 0
        for item in ltemp:
           tsuma = sum(ltemp)
        tmed = tsuma / len(ltemp)
        print (tmed)
    elif param == 'humedad maxima':
        hmax = max(lhum)
        print (hmax)
    elif param == 'humedad minima':
        hmin = min(lhum)
        print (hmin)
    elif param == 'precipitacion acumulada':
        psuma = sum(lprec)
        print (psuma)
    else:
        pass
            

if __name__ == '__main__':
    file = open('ejemploMeteo.txt').read()
    listadic= extraerdatos(file)       ###para crear una variable que sea el return de extraerdatos y así puedo usarla con la siguiente funcion        
    organizardatos(listadic, 'temperatura media')
    organizardatos(listadic, 'temperatura minima')
    organizardatos(listadic, 'temperatura maxima')
    organizardatos(listadic, 'humedad maxima')
    organizardatos(listadic, 'humedad minima')
    organizardatos(listadic, 'precipiracion acumulada')