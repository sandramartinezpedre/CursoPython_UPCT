# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:57:18 2020

@author: Sandra M MartinezPe
"""

import math

def pol(x,coef):   ###crear polinomio
    val= coef[0]
    for i in range (1, len(coef)): ###i acaba siendo el nº al que está elevado x
        val+= (coef[i] * (x**i))   ### 
    return val 


def newton (x0, coef, epsilon):    ###En lugar de x pongo un número, que es el número aleatorio con el que empieza la cosa
    x = x0
    f = pol(x, coef)
    while  math.fabs(f) > epsilon:
        m = (pol(x+0.0001,coef)-pol(x,coef))/0.0001     ### calcular la derivada de mi función original, decir, la pendiente de la tangente (m)
        n = f - m*x   ###estas son la n y la m de la recta tangente 
        x =(-n)/m  ###esta es la función de la recta tangente
        f = pol(x, coef)   ###el valor de f en la x con la que estás trabajando en ese momento 
    return x


if __name__ == '__main__':
    print(newton(-10, [5, 9, 3, 6, 2, -1], 0.0000001))