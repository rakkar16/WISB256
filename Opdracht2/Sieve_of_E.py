import sys
import time

limit = int(sys.argv[1])
file = str(sys.argv[2])

sieve = [0, 0] + list(range(2,limit+1))
out = open(file, 'w')
amount = 0
T1 = time.perf_counter()

"""
while sieve != []:
    n = sieve[0]
    amount += 1
    out.write('%d\n' % n)
    for i in range(len(sieve)):
        if sieve[i] % n == 0:
            sieve[i] = 0
    for x in range(sieve.count(0)):
        sieve.remove(0)
"""

for i in range(2, limit+1):
    if sieve[i] != 0:
        n = sieve[i]
        amount += 1
        out.write('%d\n' % n)
        for x in range(n, limit+1, n):
            sieve[x] = 0
        
T2 = time.perf_counter()
out.close()

print('Found %d Prime numbers smaller than %d in %d sec.' % (amount, limit, T2-T1))
print('--------------------------------------------')

