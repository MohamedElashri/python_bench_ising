import os
import matplotlib.pyplot as plt

def parse_results(file):
    with open(file) as f:
        lines = f.read().splitlines()
    results = {}
    for line in lines:
        if "Time it took in seconds is" in line:
            results["time"] = float(line.split('=')[-1].strip())
        if "Average energy" in line:
            results["Average energy"] = float(line.split(':')[-1].strip())
        if "Average magnetization" in line:
            results["Average magnetization"] = float(line.split(':')[-1].strip())
        if "Average heat capacity" in line:
            results["Average heat capacity"] = float(line.split(':')[-1].strip())
        # add more keys as needed
    return results

def plot_results(results, L, n):
    python_versions = results.keys()
    times = [results[v][0] for v in python_versions]
    avg_energies = [results[v][1] for v in python_versions]
    avg_magnetizations = [results[v][2] for v in python_versions]
    avg_heat_capacities = [results[v][3] for v in python_versions]

    plt.figure(figsize=(10, 6))
    plt.plot(python_versions, times, label='Execution Time')
    plt.plot(python_versions, avg_energies, label='Average Energy')
    plt.plot(python_versions, avg_magnetizations, label='Average Magnetization')
    plt.plot(python_versions, avg_heat_capacities, label='Average Heat Capacity')
    plt.legend()
    plt.savefig(f'plots_L{L}_n{n}.png')

def main():
    results = {}
    for file in os.listdir('.'):
        if file.startswith('results_') and file.endswith('.txt'):
            parts = file.split('_')
            python_version = parts[1].split('.')[0]
            L = parts[2][1:]
            n = parts[3].split('.')[0][1:]
            results[python_version] = parse_results(file)
            plot_results(results, L, n)
            results.clear()

if __name__ == "__main__":
    main()
