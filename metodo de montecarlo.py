# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:42:30 2021

@author: JOSE
"""
import random #importamos la libreria
ladoventana=500#seinserta el tamaño de la ventana
radioventana=ladoventana/2# se almacena los valores en la variableventana 
encirculo=0#se crea una variable que incialice en cero

print("estimacion de pi por el metodo de montecarlo")#se inserta un mensaje
puntos=int(input("ingresa la cantidad de tiradas-puntos aleatorios \n "))#se pide un valor desde el teclado 
if(puntos<1):#se ocupa para indicar la cantidad de tiradas que vamos a intriducir en el programa
    puntos=2

for n in range (puntos):#ocupamos un for para indicar cada unos de los valores 
   x=random.uniform(-radioventana,radioventana)#ocupamos random para indicar que los valores sean aleatorios
   y=random.uniform(-radioventana,radioventana)
   
   if((x**2+y**2)<=radioventana**2):# si ese punto cayo dentro del circulo, si xcuadrado y ycuadrado es menor al radio cuadrado
       encirculo+=1# se suma 1 a la variable en circulo
       
valorpi=4. *encirculo/puntos# se calcula el valor de pi  por 4 por encirculo divido por la cantidad de puntos
       
print("valor estimado de pi =",valorpi)# se muestra el valor de pi 
print("------------------")
