# Python Benchmark
Ising model simulation as python version benchmark

## About

As new python releases are released I will test them vs the previous releases.
The benchmark is based on the code from the ising.py file which implemented the 2d ising model simulation.

## packages

I used `numpy-1.23.4` for all different version of python used in the benchmark. This is the latest version of `numpy`. 

## Results

The benchmarks are executed on Macbook pro Apple Silicon M1 version. The python version are installed using `homebrew`

The arguments of the script are L(length of the lattice),  n(number of Monte Carlo cycles). 
### python 3.11

```bash
time python3.11 ising.py 10 10000
Time it took in seconds is = 109.2954261302948
python3.11 ising.py 10 10000  110.82s user 0.79s system 100% cpu 1:51.38 total
```

### python 3.10 

```bash
time python3.10 ising.py 10 10000
Time it took in seconds is = 123.83638191223145
python3.10 ising.py 10 10000  124.80s user 0.69s system 101% cpu 2:04.06 total
```

## python 3.9


```bash
time python3.9 ising.py 10 10000
Time it took in seconds is = 123.56476402282715
python3.9 ising.py 10 10000  123.94s user 1.08s system 101% cpu 2:03.67 total
```

### python 3.8

```bash
time python3.8 ising.py 10 10000
Time it took in seconds is = 135.1741383075714
python3.8 ising.py 10 10000  137.05s user 1.00s system 100% cpu 2:17.24 total
```

### Other versions 

Python started supporting apple silicon starting from `python3.8` and I try to make things as consistent as possible. Not to mention that `numpy` optimization for different version might be unaccounted difference. 