# 2d Ising Model Montecarlo Simulation using Metropolis Algorithm
# This script is being used for python benchmarking
# Author: Mohamed Elashri
# Email: mohamed.elashri@cern.ch
# Uagent: python ising_model.py <Lattice_size> <Number_of_time_steps>




import sys
import random
import time

# Define parameters 

B = 0  # Magnetic field strength (zero as we don't consider)
L = int(sys.argv[1]) # Lattice size (width)

# Begin with random spin sites with values (+1 or -1) for up or down spins.
s = [[random.choice([1, -1]) for _ in range(L)] for _ in range(L)]

n = int(sys.argv[2]) # number of time steps

Temperature = [t / 100 for t in range(160, 325, 1)]  # Initlaize temperature range

def calcE(s):
    E = 0
    for i in range(L):
        for j in range(L):
            E += -dE(s, i, j) / 2
    return E / L ** 2

def calcM(s):
    m = sum([sum(row) for row in s])
    return abs(m) / L ** 2

def dE(s, i, j):
    t = s[L - 1][j] if i == 0 else s[i - 1][j]
    b = s[0][j] if i == L - 1 else s[i + 1][j]
    l = s[i][L - 1] if j == 0 else s[i][j - 1]
    r = s[i][0] if j == L - 1 else s[i][j + 1]
    return 2 * s[i][j] * (t + b + r + l)

def mc(s, Temp, n):
    for m in range(n):
        i = random.randrange(L)  # choose random row
        j = random.randrange(L)  # choose random column
        ediff = dE(s, i, j)
        if ediff <= 0:
            s[i][j] = -s[i][j]  # accept move and flip spin
        elif random.random() < __import__('math').exp(-ediff / Temp):  
            s[i][j] = -s[i][j]
    return s

def physics(s, T, n):
    En = 0
    En_sq = 0
    Mg = 0
    Mg_sq = 0
    for p in range(n):
        s = mc(s, T, 1)
        E = calcE(s)
        M = calcM(s)
        En += E
        Mg += M
        En_sq += E * E
        Mg_sq += M * M
    En_avg = En / n
    mag = Mg / n
    CV = (En_sq / n - (En / n) ** 2) / (T ** 2)
    return En_avg, mag, CV

mag = [0 for _ in Temperature]
En_avg = [0 for _ in Temperature]
CV = [0 for _ in Temperature]

start = time.time()

for ind, T in enumerate(Temperature):
    s = mc(s, T, n)
    En_avg[ind], mag[ind], CV[ind] = physics(s, T, n)


# Calculate statistics
avg_energy = sum(En_avg) / len(En_avg)
avg_magnetization = sum(mag) / len(mag)
avg_heat_capacity = sum(CV) / len(CV)

min_energy = min(En_avg)
min_magnetization = min(mag)
min_heat_capacity = min(CV)

max_energy = max(En_avg)
max_magnetization = max(mag)
max_heat_capacity = max(CV)

end = time.time()  # stop the timer here

# Print execution time
print("Time it took in seconds is = %s" % (end - start))
time = (end - start) / 60
print('It took ' + str(time) + ' minutes to execute the code')

# Print statistics
print(f'Average energy: {avg_energy}')
print(f'Average magnetization: {avg_magnetization}')
print(f'Average heat capacity: {avg_heat_capacity}')

print(f'Minimum energy: {min_energy}')
print(f'Minimum magnetization: {min_magnetization}')
print(f'Minimum heat capacity: {min_heat_capacity}')

print(f'Maximum energy: {max_energy}')
print(f'Maximum magnetization: {max_magnetization}')
print(f'Maximum heat capacity: {max_heat_capacity}')    