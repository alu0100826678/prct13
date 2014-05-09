#!/usr/bin/python
#!encoding: UTF-8      #Acepta español solo los comentarios.
 
import sys
import time
import modulopi
import timeit
import matplotlib.pylab as pl  #Para que podamos mostrar más de una a la vez.
x1=(10,50,100,150,500,550,1000)  # Creamos una lista con los intervalos.
y1=[]   # Para la primera gráfica
y2=[]   #Para la segunda gráfica

#Introducimos la función creda en prácticas anteriores:
def error(interv,n_test,umbral):
    resta=0.0
    y = modulopi.PI
    fallos = 0
    for i in range(0,n_test):
      x = modulopi.funcion(interv)
      resta = abs(x -y)
      if resta > umbral:
         fallos=fallos+1
    porcentaje= (fallos/n_test)*100
    return porcentaje
    
if __name__ == "__main__":
   if len(sys.argv) == 4:
      n = int (sys.argv[1])
      m = int (sys.argv[2])
      u = float (sys.argv[3])    
 else:
      n = int (raw_input('Introduzca la cantidad de intervalos en los que desea que se aplique la aproximación de pi:'))
      m = int (raw_input ('Introduzca la cantidad de veces que quiere realizarlo: '))
      u = float (raw_input('Introduzca el valor del umbral:'))
      
#Modificamos la función.
      for i in x1:
	inicio=time.clock()
        error()
      fin=time.clock()
      t = fin - inicio
      x1=fin+[y1]  
      x2=fin+[y2]
      
      
 ## ## ## ## ## ## ## ## ## ## ## ## "CREAMOS" LA PRIMERA GRÁFICA ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
      
      graf1=pl.subplot(211)    #Hay dos filas,una columna y lo localizamos en el primer cuadrado.
      pl.title('Umbral respecto al error') #Título de la gráfica
      pl.xlabel('Umbral') #Título del eje X
      pl.ylabel('Numero de intervalos') #Título del eje Y
      pl.plot(x1,y1,marker='p',linestyle= '-',color='g',label='Funcion del Umbral') #La queremos con pentágonos,continua y de color verde.
      pl.legend(['Función del error'],loc=0,numpoints=1) #Localizamos la leyenda en el mejor lugar
      
##  ## ## ## ## ## ## ## ## ## ## ## ## "CREAMOS" LA SEGUNDA GRÁFICA ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

      graf2=pl.subplot(212) #Dos filas,una columna y lo localizamos en el segundo cuadrado.
      pl.title('Tiempo respecto al numero de intervalos') #Título de la gráfica
      pl.xlabel('Tiempo')     #Título en el eje X
      pl.ylabel('Numero de intervalos')  #Título en el eje Y
      pl.plot(x1,y2,marker='*',linestyle='--',color='m',label='Funcion del Tiempo')  # La queremos con estrellas,discontinua y de color magenta.
      pl.legend(['Funcion del Tiempo'],loc=0,numpoints=1) #Localizamos la leyenda en el mejor lugar con un sólo punto que indique la función.
      
      
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
      pl.savefig("Representacion.eps",dpi=72)  #Guardamos las gráficas con el nombre "Representación".
      pl.show() #Para que la muestre.
      