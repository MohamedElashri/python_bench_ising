import sys
import numpy as np  
import random  
import time  

# Define parameters 

L = int(sys.argv[1]) # lattice size
J = 1.0 # coupling constant
n = int(sys.argv[2]) # number of time steps
s = np.random.choice([-1, 1], size=(L, L)) # initialize spin configuration
Temperature = np.arange(1.6, 3.25,0.01) # temperature range (the range includes critical temperature)


'''
Energy of the lattice calculations. 
The energy here is simply the sum of interactions between spins divided by the total number of spins
'''


def calcE(s):
    E = 0
    for i in range(L):
        for j in range(L):
            E += -dE(s, i, j) / 2
    return E / L ** 2


'''
Calculate the Magnetization of a given configuration
Magnetization is the sum of all spins divided by the total number of spins
'''


def calcM(s):
    m = np.abs(s.sum())
    return m / L ** 2


# Calculate interaction energy between spins. Assume periodic boundaries
# Interaction energy will be the difference in energy due to flipping spin i,j 
# (Example: 2*spin_value*neighboring_spins)
def dE(s, i, j):  # change in energy function
    # top
    if i == 0:
        t = s[L - 1, j]  # periodic boundary (top)
    else:
        t = s[i - 1, j]
    # bottom
    if i == L - 1:
        b = s[0, j]  # periodic boundary (bottom)
    else:
        b = s[i + 1, j]
    # left
    if j == 0:
        l = s[i, L - 1]  # periodic boundary (left)
    else:
        l = s[i, j - 1]
    # right
    if j == L - 1:
        r = s[i, 0]  # periodic boundary  (right)
    else:
        r = s[i, j + 1]
    return 2 * s[i, j] * (t + b + r + l)  # difference in energy is i,j is flipped


# Monte-carlo sweep implementation
def mc(s, Temp, n):
    for m in range(n):
        i = random.randrange(L)  # choose random row
        j = random.randrange(L)  # choose random column
        ediff = dE(s, i, j)
        if ediff <= 0:  # if the change in energy is negative
            s[i, j] = -s[i, j]  # accept move and flip spin
        elif random.random() < np.exp(-ediff / Temp):  # if not accept it with probability exp^{-dU/kT}
            s[i, j] = -s[i, j]
    return s


# Compute physical quantities
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
    Eng = En / n
    mag = Mg / n
    CV = (En_sq / n - (En / n) ** 2) / (T ** 2)
    S = (Mg_sq / n - (Mg / n) ** 2) / T
    return Eng, mag, CV, S


# Inititalize magnetization, average energy and heat capacity
mag = np.zeros(len(Temperature))
Eng = np.zeros(len(Temperature))
CV = np.zeros(len(Temperature))
S= np.zeros(len(Temperature))

start = time.time()

# Simulate at particular temperatures (T) and compute physical quantities (Energy, heat capacity and magnetization)
for ind, T in enumerate(Temperature):
    # Sweeps spins
    s = mc(s, T, n)
    # Compute physical quanitites with 1000 sweeps per spin at temperature T
    Eng[ind], mag[ind], CV[ind], S[ind] = physics(s, T, n)
end = time.time()
print("Time it took in seconds is = %s" % (end - start))