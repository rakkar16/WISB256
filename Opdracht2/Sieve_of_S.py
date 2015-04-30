import sys
import time
import math

limit = int(sys.argv[1])
file = str(sys.argv[2])
n = math.ceil((limit - 2)/2)

sieve = list(range(n+1))
out = open(file, 'w')
out.write('2\n')
amount = 1
T1 = time.perf_counter()

for j in range(1, math.ceil((n-1)/3) + 1):
    i = 1
    while i <= j and (i + j + 2 * i * j) <= n:
        sieve[i + j + 2 * i * j] = 0
        i += 1

for x in range(n+1):
    if sieve[x] != 0:
        out.write('%d\n' % (sieve[x] * 2 + 1))
        amount += 1

T2 = time.perf_counter()
out.close()

print('Found %d Prime numbers smaller than %d in %f sec.' % (amount, limit, T2-T1))
print('--------------------------------------------')

