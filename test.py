import unittest
import biseccion
import newton_raphson
import Integracion_numerica
from math import *

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: e**x - 3*x**2
        a = 0
        b = 1
        tol = 0.02
        ni = 100
        self.assertEqual(biseccion.biseccion(f,a,b,tol,ni),None)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f= lambda x: e**x-3*x**2 #x**2+2*x-8
        df = lambda x: e**x-6*x # 2*x + 2
        x0 = 0.7  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newton_raphson.newthon_raphson(f,df,x0,tol),0.9100079800667897)


class Test_integracion_numerica(unittest.TestCase):
    def Test_integracion_numerica(self):
        f = lambda x: sqrt(x+1) #x**2+2*x-8
        a = -1      # inicio del intervalo
        b = 1     # fin del intervalo
        n = 5   # numero de participaciones
        self.assertEqual(integracion_numerica.trapecio(f,a,b,n), 1.8377382733191294)

if __name__ == "__main__":
    unittest.main()
