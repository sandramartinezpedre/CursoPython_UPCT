# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:21:58 2020

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
    matrizimagen = img2mat(im)
    matrizpatron = img2mat(patron)
            
    coincidencias = [] 
              
    for i, row in enumerate(matrizimagen[: - len(matrizpatron)-1]):
        for j, colum in enumerate(row [: - len(matrizpatron[0]) -1]):
            isMatch = True
            for ip, rowp in enumerate(matrizpatron):
                for jp, colum in enumerate(rowp):
                    if matrizpatron[ip][jp] == (255,255,255):
                        break
                    else:
                        pass
                    if matrizimagen[i+ip][j+jp] != matrizpatron[ip][jp]:
                       isMatch = False
                       break
                if isMatch == False:
                    break
            if isMatch == True:
                coincidencias.append((i + len(matrizpatron)//2,
                                      j + len(matrizpatron[0])//2))
                       
    return coincidencias
  
    

if __name__== '__main__':
    import PIL.Image
    imagen = PIL.Image.open('imagen2.bmp')
    patron = PIL.Image.open('patron2.bmp')
    
    posicion_coincidencias= escaner(imagen, patron)
    print (posicion_coincidencias)
    



