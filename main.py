import numpy as np
import random

v = np.array([3, 1, 4, 1]) # inital
u = np.array([3, 1, 4, 2]) # similar
w = np.array([1, 6, 1, 8]) # different

ALL = 100000
SUC = 0

for _ in range(ALL):
    A = np.random.randint(low=0, high=100, size=(4, 4)) # matrix for v
    # B = np.random.randint(low=0, high=1000, size=(4, 4)) # matrix for u
    # C = np.random.randint(low=0, high=1000, size=(4, 4)) # matrix for w

    r_v = np.random.rand(4) * 10
    
    if np.linalg.norm((np.dot(A, v) - np.dot(A, r_v))) < 16:
        print(r_v)
        SUC += 1

print(SUC, "/", ALL)


