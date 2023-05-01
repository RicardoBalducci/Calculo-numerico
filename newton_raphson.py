from math import  *
#Nombre: Ricardo Balducci.
#Cedula: 28.308.177
def newthon_raphson(f, df, x0, tol, max_iter=5):
    i = 0
    print("\nMétodo de Newton-Raphson\n")
    while i < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol * abs(x1):
            return x1
        x0 = x1
        i += 1
    raise ValueError("El método de Newton-Raphson no converge después de %d iteraciones." % max_iter)#en caso de no poder

def f(x):
    return sin(x) - e**-x # e**x-3*x**2

def df(x):
    return cos(x) + e**-x #e**x-6*x 

x0 = 0.5  # valor inicial de x
tol = 0.02 # margen de error
raiz = newthon_raphson(f, df, x0, tol)  # encontramos la raíz de f
print("La mejor solución aproximacion es: ",raiz)  # mostramos mejor solución aproximacion