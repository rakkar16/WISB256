import sys
import math

fin = open(str(sys.argv[1]))
primes = fin.read().splitlines()
fin.close()
C2 = 0.6601618

piN = len(primes)
N = int(primes[piN - 1])
piNdiv = N / math.log(float(N))

pi2N = 0
for i in range(1, piN):
    if int(primes[i]) - int(primes[i - 1]) == 2:
        pi2N += 1

pi2Ndiv = 2 * C2 * N / (math.log(float(N)) ** 2)

print('Largest Prime =  ' + str(N))
print('--------------------------------')
print('pi(N)         =  ' + str(piN))
print('N/log(N)      =  ' + str(piNdiv))
print('ratio         =  ' + str(piN/piNdiv))
print('--------------------------------')
print('pi_2(N)       =  ' + str(pi2N))
print('2CN/log(N)^2  =  ' + str(pi2Ndiv))
print('ratio         =  ' + str(pi2N/pi2Ndiv))

