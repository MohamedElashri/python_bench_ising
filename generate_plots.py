import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

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

def assign_colors(unique_values):
    cmap = plt.cm.get_cmap('viridis', len(unique_values))
    color_dict = {val: cmap(i) for i, val in enumerate(unique_values)}
    return color_dict

def plot_results(python_results, L, color_dict):
    python_versions = list(python_results.keys())
    bar_width = 0.8 / len(python_versions) # determine the width of the bars

    for i, version in enumerate(python_versions):
        n_values = [int(n) for n in python_results[version].keys()]
        times = [python_results[version][str(n)]["time"] for n in n_values]
        colors = [color_dict[str(n)] for n in n_values]
        plt.bar(np.array(n_values) + i*bar_width, times, color=colors, width=bar_width, label=f"Python {version}")

    plt.xlabel("n")
    plt.ylabel("Execution time (s)")
    plt.legend()
    plt.title(f"Execution time for different Python versions (L={L})")
    plt.grid()

    output_file = f"time_L{L}.png"
    plt.savefig(output_file)
    plt.close()  
    print(f"Plot saved to: {output_file}")  

def main():
    result_files = [f for f in os.listdir('.') if f.startswith('results_') and f.endswith('.txt')]

    # Group files by Python version and (L, n) combination
    python_results = {}
    for file in result_files:
        parts = file.split('_')
        python_version = parts[1]
        L = parts[2][1:]
        n = parts[3].split('.')[0][1:]
        if python_version not in python_results:
            python_results[python_version] = {}
        if L not in python_results[python_version]:
            python_results[python_version][L] = {}
        python_results[python_version][L][n] = parse_results(file)

    # Generate plots for each L
    L_values = set([L for python_version in python_results.values() for L in python_version.keys()])
    n_values = set([n for L_dict in python_results.values() for n_dict in L_dict.values() for n in n_dict.keys()])
    color_dict = assign_colors(n_values)
    for L in L_values:
        L_python_results = {python_version: results[L] for python_version, results in python_results.items() if L in results}
        plot_results(L_python_results, L, color_dict)

if __name__ == "__main__":
    main()
