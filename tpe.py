import numpy as np

class MetodoNumerico:

    def funcion(x):
        return 2*x

    def __init__(self,a,b,n):
        self.a = a 
        self.b = b
        self.n = n
        self.h = (b-a) / n
        self.aproximaciones = np.zeros(n) 

    #Revisar el tema del h, como constante en la iteracion
    def Euler(self): 
        self.aproximaciones[0] = MetodoNumerico.funcion(self.a)
        for i in range((int) (self.a + self.h ), self.n):
            self.aproximaciones[i] = self.aproximaciones[i-1] + self.h * MetodoNumerico.funcion(i)
        print(self.aproximaciones)
        return self.aproximaciones[self.n -1]

    def EulerMejorado(self):
        self.aproximaciones[0] = MetodoNumerico.funcion(self.a)
        for i in range((int) (self.a + self.h ), self.n):
            res = MetodoNumerico.funcion(i)
            self.aproximaciones[i] = res + self.h*0.5*(MetodoNumerico.funcion((i+1))+res)
        return self.aproximaciones[self.n -1] 

metodo = MetodoNumerico(0,2,11)

print(metodo.Euler())
print(metodo.h)
print(metodo.aproximaciones)
