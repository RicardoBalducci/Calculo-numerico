from math import * #Importamos la librería de math
#Nombre: Ricardo Balducci.
#Cedula: 28.308.177

def biseccion(f,a,b,tol):#Definimos la función llamada bisección
	m1=a
	m=b
	k=0
	print("\nMétodo de Bisección\n")
	if(f(a)*f(b)>0):
		print('La función no cambia de signo en el intervalo dado.')
		return None

	while (abs(m1-m)>tol):
		m1=m
		m=(a+b)/2
		if(f(a)*f(m)<0): #cambia de signo en el intervalo [a,m]
			b=m
		if(f(m)*f(b)<0): #cambia de signo en el intervalo [a,m]
			a=m
		print('El intervalo',k,'es [',a,',',b,']')
		k=k+1;

	print('m(',k,') =',m1,' es la mejor solución aproximada')
	
f = lambda x: e**x - 3*x**2 #sin (x) - e**-x
a = 0
b = 1
tol = 0.03
solucion = biseccion(f, 0, 1, 0.03) 