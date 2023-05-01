import unittest
import biseccion
import newton_raphson
from math import *

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: sin(x) - e**-x
        a = 0
        b = 1
        tol = 0.02
        self.assertEqual(biseccion.biseccion(f,a,b,tol),None)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f= lambda x: e**x-3*x**2 #x**2+2*x-8
        df = lambda x: e**x-6*x # 2*x + 2
        x0 = 0.7  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newton_raphson.newthon_raphson(f,df,x0,tol),0.9100079800667897)
        

if __name__ == "__main__":
    unittest.main()




"""FUNCIONA UNICAMENTE PARA BISECCION
import unittest
import biseccion
#import newton
from math import *

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f = lambda x: sin(x) - e**-x
        a = 0
        b = 1
        tol = 0.02
        self.assertEqual(biseccion.biseccion(f,a,b,tol),None)

if __name__ == "__main__":
    unittest.main()




import unittest
#import biseccion
import newton
from math import *

class test_newton(unittest.TestCase):
    def test_newton(self):
        f=lambda x: e**x-3*x**2 #x**2+2*x-8
        df = lambda x: e**x-6*x # 2*x + 2
        x0 = 0.7  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newton.newthon_raphson(f,df,x0,tol))

class test_newton(unittest.TestCase):
    def test_newton(self):
        f=lambda x:x**2+2*x-8
        df = lambda x: 2*x + 2
        x0 = 0.5  # valor inicial de x
        tol = 0.02 # margen
        self.assertEqual(newthon.raiz(),None)

        

if __name__ == "__main__":
    unittest.main()















"""
"""
import unittest
import biseccion
import newton_raphson

class biseccion(unittest.TestCase):
    def biseccion(self):
        f = lambda x: e**x - 3*x**2 #sin (x) - e**-x
        a = 0
        b = 2
        tol = 0.034
        self.assertEqual(biseccion.biseccion(f,a,b,tol))

class newton_rapshon(unittest.TestCase):
    def newton_rapshon(self):
        f = lambda x: e**x - x**2
        df = lambda x: cos(x) + e**-x
        x0 = 0.5
        tol = 0.01
        self.assertEqual(newton_rapshon.raiz())
if __name__ == "__main__":
    unittest.main()


"""