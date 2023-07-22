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
    print(f"Parsed results: {results}")
    return results

def plot_results(results, L, n):
    python_versions = list(results.keys())
    times = [results[v]["time"] for v in python_versions]

    plt.figure(figsize=(10, 6))
    plt.bar(python_versions, times)
    plt.xlabel("Python version")
    plt.ylabel("Execution time (s)")
    plt.title(f"Execution time for different Python versions (L={L}, n={n})")

    # Ensure the plots directory exists
    os.makedirs("plots", exist_ok=True)

    output_file = f"plots/time_L{L}_n{n}.png"
    plt.savefig(output_file)

    print(f"Plot saved to: {output_file}")  

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
