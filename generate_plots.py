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
    return results

def plot_results(results, L, n):
    python_versions = list(results.keys())
    times = [results[v]["time"] for v in python_versions]

    plt.figure(figsize=(10, 6))
    plt.bar(python_versions, times)
    plt.xlabel("Python version")
    plt.ylabel("Execution time (s)")
    plt.title(f"Execution time for different Python versions (L={L}, n={n})")


    output_file = f"plots/"time_L{L}_n{n}.png"
    plt.savefig(output_file)
    plt.close()  
    print(f"Plot saved to: {output_file}")  

def main():
    result_files = [f for f in os.listdir('.') if f.startswith('results_') and f.endswith('.txt')]

    # Group files by (L, n) combination
    datasets = {}
    for file in result_files:
        parts = file.split('_')
        dataset_key = (parts[2][1:], parts[3].split('.')[0][1:])
        if dataset_key not in datasets:
            datasets[dataset_key] = []
        datasets[dataset_key].append(file)

    # Parse results and generate plots for each (L, n) combination
    for (L, n), files in datasets.items():
        results = {}
        for file in files:
            python_version = file.split('_')[1]
            results[python_version] = parse_results(file)
        plot_results(results, L, n)

if __name__ == "__main__":
    main()
