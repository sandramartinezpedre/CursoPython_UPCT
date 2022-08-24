import math 
import random
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:50:08 2020

@author: Sandra M MartinezPe
"""


#### random.gauss(mu, sigma) Gaussian distribution. mu is the mean, and sigma is the standard deviation. 
###This is slightly faster than the normalvariate() function defined below.

###random.normalvariate(mu, sigma): Normal distribution. mu is the mean, and sigma is the standard deviation.

horas_periodocompleto = 87600
area_total = 500


def simulacion( area_bombilla, precio_bombilla, esp_vida, desv_tip):

   
    n_plazas= area_total // area_bombilla
    randoml=[]
    num_bombillas = n_plazas    
        
        
        
    for i in range (n_plazas):
        n = random.normalvariate(esp_vida, desv_tip)  ###crear lista de números random
        randoml.append (n)
     
    
    
    for i in range(len(randoml)):
        while randoml[i] < 87600:   ### Mientras todas no estén completas...
            randoml[i] += random.normalvariate(esp_vida, desv_tip)
            num_bombillas += 1
    
    preciototal = num_bombillas*precio_bombilla
    return preciototal



if __name__== '__main__': 
    suma1=0
    suma2=0
    
    for i in range(10000):
        suma1 += simulacion(20,30,30000,1500)
    
    media1 = suma1/10000
    
    for i in range(10000):
        suma2 += simulacion(30,36,28000,1800)
    
    media2 = suma2/10000
    
  
           
        
        
        
        
        
    
            












