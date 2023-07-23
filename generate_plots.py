import os
import matplotlib.pyplot as plt
import numpy as np

def parse_results(file):
    with open(file) as f:
        lines = f.read().splitlines()
    results = {}
    for line in lines:
        if "Time it took in seconds is" in line:
            results["time"] = float(line.split('=')[-1].strip())
    return results

def plot_results(results, parameter_values, python_versions, fixed_param, fixed_value):
    x = np.arange(len(python_versions))
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, param in enumerate(parameter_values):
        times = [results[v].get((fixed_value, param), {"time": np.nan})["time"] for v in python_versions]
        rects = ax.bar(x - (len(parameter_values)/2 - i)*width, times, width, label=f'{fixed_param}={fixed_value}, varying_param={param}')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Python version')
    ax.set_ylabel('Execution time (s)')
    ax.set_title(f'Execution time for different Python versions and {fixed_param} values')
    ax.set_xticks(x)
    ax.set_xticklabels(python_versions)
    ax.legend()

    fig.tight_layout()

    output_file = f"time_{fixed_param}{fixed_value}_varying.png"
    plt.savefig(output_file)
    plt.close()  
    print(f"Plot saved to: {output_file}") 

def main():
    result_files = [f for f in os.listdir('.') if f.startswith('results_') and f.endswith('.txt')]

    # Group files by python version
    datasets = {}
    python_versions = []
    L_values = []
    n_values = []
    for file in result_files:
        parts = file.split('_')
        L = int(parts[2][1:])
        n = int(parts[3].split('.')[0][1:])
        python_version = parts[1]
        if python_version not in python_versions:
            python_versions.append(python_version)
        if L not in L_values:
            L_values.append(L)
        if n not in n_values:
            n_values.append(n)
        if python_version not in datasets:
            datasets[python_version] = {}
        datasets[python_version][(L, n)] = parse_results(file)

    for L in L_values:
        plot_results(datasets, n_values, python_versions, 'L', L)

    for n in n_values:
        plot_results(datasets, L_values, python_versions, 'n', n)

if __name__ == "__main__":
    main()
