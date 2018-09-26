import numpy as np
import algorithm as al
import sys
print(sys.version)
N=100

data1 = np.arange(N)
data2 = np.arange(50,N)

# print(data1)
# print(data2)
print(np.cumsum(data1))
print((np.arange(N) + 1))
cumulative_average = np.cumsum(data1) / (np.arange(N) + 1)

print(cumulative_average)

""" print(al.Algorithm())
print(al.eGreddy())
print(al.UCB1())
print(al.TS()) """