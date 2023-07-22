import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Parse the results.txt file
results_file = "results/results.txt"
data = []
with open(results_file, "r") as file:
    for line in file:
        if line.startswith('Python version:'):
            parts = line.split()
            version = parts[2].rstrip(',')
            L = int(parts[4].rstrip(','))
            n = int(parts[6])
        elif line.startswith('Time it took in seconds is ='):
            time = float(line.split('=')[1].strip())
            data.append({"Python Version": version, "L": L, "n": n, "Time": time})

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Specify the unique values for L and n you used in your tests
L_values = [10, 20]
n_values = [10000, 20000, 30000]

python_versions = df['Python Version'].unique()

bar_width = 0.15
indices = np.arange(len(python_versions))

# Plot time vs L for each n
for n in n_values:
    plt.figure(figsize=(10, 6))
    bar_shift = 0
    for L in L_values:
        df_fixed_n_L = df[(df['n'] == n) & (df['L'] == L)]
        times = []
        for version in python_versions:
            time = df_fixed_n_L[df_fixed_n_L['Python Version'] == version]['Time']
            if len(time) > 0:
                times.append(time.values[0])
            else:
                times.append(0)  # No data for this Python version
        plt.bar(indices + bar_shift, times, width=bar_width, label=f"L={L}")
        bar_shift += bar_width
    plt.title(f'Time vs Python Version (for n = {n})')
    plt.xlabel('Python Version')
    plt.ylabel('Time (s)')
    plt.xticks(indices + bar_width/2, python_versions)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'results/plots/Time_vs_Python_Version_n_{n}.pdf')

# Plot time vs n for each L
for L in L_values:
    plt.figure(figsize=(10, 6))
    bar_shift = 0
    for n in n_values:
        df_fixed_L_n = df[(df['L'] == L) & (df['n'] == n)]
        times = []
        for version in python_versions:
            time = df_fixed_L_n[df_fixed_L_n['Python Version'] == version]['Time']
            if len(time) > 0:
                times.append(time.values[0])
            else:
                times.append(0)  # No data for this Python version
        plt.bar(indices + bar_shift, times, width=bar_width, label=f"n={n}")
        bar_shift += bar_width
    plt.title(f'Time vs Python Version (for L = {L})')
    plt.xlabel('Python Version')
    plt.ylabel('Time (s)')
    plt.xticks(indices + bar_width/2, python_versions)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'results/plots/Time_vs_Python_Version_L_{L}.pdf')
