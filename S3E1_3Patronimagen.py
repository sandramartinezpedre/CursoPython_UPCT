# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:41:52 2020

@author: Sandra M MartinezPe
"""

def img2mat (im):    
    
    ###crear matrices del patron y de la imagen que se va a analizar
    
    matrizimagen =[]
    
    for i in range (im.width):
        matrizimagen.append([])
                
        for j in range (im.height):
            matrizimagen[i].append(im.getpixel((i,j)))

    return matrizimagen
            
            
def escaner (im, patron):
    matrizimagen = img2mat(imagen)
    matrizpatron = img2mat(patron)
    coincidencias=[]
              
    for i, row in enumerate(matrizimagen[: - len(matrizpatron)-1]):
        for j, colum in enumerate(row [: - len(matrizpatron[0]) -1]):
            isMatch = True
            for ip, rowp in enumerate(matrizpatron):
                for jp, colum in enumerate(rowp):
                   if matrizimagen[i+ip][j+jp] != matrizpatron[ip][jp]:
                       isMatch = False
                       break
                if isMatch == False:
                    break
            if isMatch == True:
                coincidencias.append((i + len(matrizpatron)//2,
                                      j + len(matrizpatron[0])//2))
                       
    return coincidencias
                
                           
def marcarrojo(matrizimagen, coincidencias, tam=(3,3)):
    coincidencias=escaner(imagen,patron)
    matrizpatron = img2mat(patron)
    matrizimagen = img2mat(imagen)
    n=tam[0]
    m=tam[1]
    for i, row in enumerate(matrizimagen[: - len(matrizpatron)-1]):
        for j, colum in enumerate(row [: - len(matrizpatron[0]) -1]):
            for item in coincidencias:
                if item == (i,j):
                    rango_i= (i + n//2 +1, i-n//2-1)
                    rango_j= (j-m//2 -1, j+m//2+1)
                    for ip in range(rango_i[0], rango_i[1]+1):
                        matrizimagen[ip][rango_j[0]]=(255,0,0)
                        matrizimagen[ip][rango_j[1]]=(255,0,0)
                    for jp in range(rango_j[0], rango_j[1]+1):
                        matrizimagen[rango_i[0]][jp]=(255,0,0)
                        matrizimagen[rango_i[1]][jp]=(255,0,0)
    return matrizimagen
                        
                                  
                                      
        
if __name__== '__main__':
    import PIL.Image
    
    imagen = PIL.Image.open('imagen3.bmp')
    patron = PIL.Image.open('patron3.bmp') 
    coincidencias= escaner(imagen, patron)
    nueva_matriz= marcarrojo(imagen,coincidencias, tam= (3,3))
    for row in nueva_matriz:
        print (row)
        