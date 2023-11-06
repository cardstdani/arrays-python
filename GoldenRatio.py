from decimal import *
fibonacciSequence = [0, 1, 1]
precision = 200
getcontext().prec = precision

for i in range(2, precision):
    fibonacciSequence.append(fibonacciSequence[i] + fibonacciSequence[i - 1])

print("Fibonacci sequence: " + str(fibonacciSequence))
phi = Decimal(fibonacciSequence[len(fibonacciSequence) - 1]) / fibonacciSequence[len(fibonacciSequence) - 2]
print("Golden ratio: " + str(phi))
