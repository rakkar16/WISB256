from scipy import integrate
import numpy

class Lorenz(object):
    def __init__(self, state, sigma=10, rho=28, beta=8/3):
        self._state = state
        self._sigma = sigma
        self._rho = rho
        self._beta = beta
        
    def solve(self, T, dt):
        def lorfun(state,s,r,b):
            return [s*(state[1]-state[0]), state[0]*(r-state[2])-state[1], state[1]*state[0] - b*state[2]]
        tlist = numpy.arange(0,T+dt,dt)
        """
        i = 0
        while i <= T:
            tlist.append(i)
            i += dt
        """
        return integrate.odeint(lambda xyz,t:lorfun(xyz, self._sigma, self._rho, self._beta), self._state, tlist)#, (), None, 0, 0, None,None,None,None,None,dt,dt,dt)