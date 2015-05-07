import sys
import math
import random

def drop_needle(L):
    x = random.random()
    a = random.vonmisesvariate(0,0)
    if math.floor(x) - math.floor(x + L * math.cos(a)) != 0:
        return True
    else:
        return False

hits = 0

try:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
except IndexError:
    print('Use: estimate_pi.py N L')
    exit()

try:
    random.seed(float(sys.argv[3]))
except IndexError:
    pass
    
if L > 1:
    print('AssertionError: L should be smaller than 1')
    exit()

for i in range(N):
    if drop_needle(L):
        hits += 1
        
print('%d hits in %d tries' % (hits, N))

pi = 2 * L * N / hits

print('Pi = '+ str(pi))