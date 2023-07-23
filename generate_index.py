import os

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Ising Model Benchmark Results</title>
</head>
<body>
    <h1>Ising Model Benchmark Results</h1>
    {plots}
</body>
</html>
"""

plot_template = """
<h2>Plot for L={L}, n={n}</h2>
<img src="plot_L{L}_n{n}.png" alt="Plot for L={L}, n={n}">
"""

plots_html = ""
for L in [10, 20]:
    for n in [10000, 20000, 30000]:
        if os.path.exists(f"plots/plot_L{L}_n{n}.png"):
            plots_html += plot_template.format(L=L, n=n)

html = html_template.format(plots=plots_html)

with open("index.html", "w") as f:
    f.write(html)
