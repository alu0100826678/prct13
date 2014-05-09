#!/usr/bin/python
 #!encoding: UTF-8
import sys
def funcion(n):
    suma=0.0
    for i in range(1,n+1):
            a = float (i-1)/n
            b = float (i)/n
            x_i = (i - 0.5)/n
            fx_i = 4.0/(1.0+x_i*x_i)
            suma = suma+fx_i
    r = suma/float (n)
    return r
    
if __name__ == "__main__":
   if len(sys.argv) == 3:
      n = int (sys.argv[1])
      m = int (sys.argv[2])
   else:
      n = int (raw_input('Introduzca la cantidad de intervalos en los que desea que se aplique la aproximación de pi:'))
      m = int (raw_input ('Introduzca la cantidad de veces que desea invocar a la función:'))
   
   l=[]
   for i in range (1, n+1):
     pi=funcion(n*i)
   l = l + [pi]
   print l 