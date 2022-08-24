# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:38:16 2020

@author: Sandra M MartinezPe
"""



def buscar_principionum(dic, ref):
    principionum_lista=[]
    for key,value in dic.items():
        ke = str(key)
        nu=str(value)
        re= str(ref)
        
        result= nu.startswith(re)
        if result == True:
            contacto = ke + ' '+ nu
            principionum_lista.append(contacto)
        else:
            pass
    return principionum_lista


def numeros_agenda(dic):
    dic_num=dic.copy()
    for key_agenda in dic.keys():
        nueva_key='' 
        for i in key_agenda:
            for key, value in abc.items():
                if i == key:
                    nueva_key= nueva_key + str(value)
                else: 
                    pass
        dic_num[nueva_key]=dic_num.pop(key_agenda)
    return dic_num

def buscar_nombre(dic,ref):
    nombre_lista=[]
    re=str(ref)
    dic_num=numeros_agenda(dic)
    for key,value in dic_num.items():
        result= re in key
        if result == True:
            for key_agnom,val_agnom in dic.items():
                if value == val_agnom:
                    contacto = str(key_agnom) + ' '+ str(val_agnom)
                    nombre_lista.append(contacto)
                    
    return nombre_lista

def num_contenido(dic,ref):
    re=str(ref)
    numcontenido_lista=[]
    for key, value in dic.items():
        nu=str(value)
        result= re in nu
        if result ==True:
            contacto = str(key) + ' '+ nu
            numcontenido_lista.append(contacto)
    return numcontenido_lista

def eliminar_repes (dic, ref):
    a=buscar_principionum(dic, ref)
    b=buscar_nombre(dic, ref)
    c=num_contenido(dic, ref)
    prueba=[]
    todo= []
    todo = a[:]
    if todo==prueba:
        for r in b:
            todo.append(r)
    else:
        pass
    for i in b:
        for j in todo:
            result= i in todo
            if result == True:
                pass
            else:
                todo.append(i)
    if todo == prueba:
        for k in c:
            todo.append(k)
        else:
            pass
    for p in c:
        for q in todo:
            result2= p in todo
            if result2== True:
                pass
            else:
                todo.append(p)
    return todo

def lista_def (dic):               ###teniendo en cuenta las busquedas previas
    
    
    busquedaprevia_añadir=[]
    print ('introduzca número')
    numero_ref=input()
    a= eliminar_repes(agenda,numero_ref)
    if busquedas_previas ==[' ']:
        lista_definitiva= a
        pass
    else:    
        for i in busquedas_previas:
            for j in a:
                if i == j:
                    busquedaprevia_añadir.append(j)
                    a.remove(j)
                else:
                    pass
                lista_definitiva= busquedaprevia_añadir + a 
    return lista_definitiva
            
            
            
            
            

    
import json
with open('agenda.json', 'r') as file:
    agenda= json.load(file)
abc= {'a':2 ,'á':2, 'b': 2, 'c': 2,'d':3, 'e':3,'é':3,'f':3, 'g':4, 'h':4,'i':4,'í':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6, 'ó':6,'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'ú':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9, ' ':0}
busquedas_previas=[' ']
while True:
    definitiva= lista_def(agenda)
    print (definitiva)
    print (' escribe "1" si has encontrado el número que buscas' +"\n " +'escribe "2" si no lo has encontrado')
    clave= input()
    if clave == '1':
        bol= False
    else:
        bol=True                   ###Hemos encontrado el numero. hora, fecha...      
        
    if bol == False:
        print ('introduce el numero de orden del contacto que buscas:considerando que la primera posición es 0')
        orden=input()
        ordenint=int(orden)
        coincidencia=(definitiva[ordenint])
        busquedas_previas.insert(0, coincidencia)
        print (coincidencia)
    else:
        pass
        
            



