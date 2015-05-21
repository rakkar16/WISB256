from array import array
from math import sqrt

class Vector(object):
    def __init__(self, n, values=0):
        self.dim = n
        if type(values).__name__ == 'list' or type(values).__name__ == 'array':
            self.value = array('d', values)
        else:
            self.value = array('d', [values]*n)


    def __str__(self):
        out = ''
        for i in range(self.dim):
            out += str(self.value[i])+'\n'
        return out[:-1]
        
        
    def lincomb(self, other, alpha=1, beta=1):
        cons = array('d',[])
        for i in range(self.dim):
            cons += array('d',[alpha * self.value[i] + beta * other.value[i]])
        return Vector(self.dim, cons)
        
    def scalar(self, alpha):
        return self.lincomb(Vector(self.dim),alpha,1)
        
    def inner(self, other):
        out = 0
        for i in range(self.dim):
            out += self.value[i] * other.value[i]
        return out
        
    def norm(self):
        return sqrt(self.inner(self))
        
    def __add__(self, other):
        return self.lincomb(other)
        
    def __sub__(self, other):
        return self.lincomb(other, 1, -1)
        
    def project(v, u): #project self(v) onto other(u)
        return u.scalar(v.inner(u)/u.inner(u))
        
def GrammSchmidt(V):
    U = [0] * len(V)
    E = [0] * len(V)
    for k in range(len(V)):
        U[k] = V[k]
        for j in range(k):
            U[k] -= V[k].project(U[j])
        E[k] = U[k].scalar(1/(U[k].norm()))
    return E