#!/bin/bash

# List of python versions
py_versions=("python3.8" "python3.9" "python3.10" "python3.11")

# Parameters for the Python script
L_values=(10 20)  # list of L (size of the lattice) values
n_values=(10000 20000 30000)  # List of n (number of steps) values

# Store the results
results_file="results/results.txt"

# Check if the results file exists and delete it if it does
if [ -e $results_file ]; then
    rm $results_file
fi

# Loop over all python versions
for py_version in "${py_versions[@]}"
do
    # Check if Python version exists
    if command -v $py_version &> /dev/null
    then
        echo "Running tests with $py_version"
        
        # Loop over all values of L and n
        for L in "${L_values[@]}"
        do
            for n in "${n_values[@]}"
            do
                echo "-----------------" >> $results_file
                echo "Python version: $py_version, L: $L, n: $n" >> $results_file
                (time $py_version ising_model.py $L $n) 2>&1 >> $results_file
            done
        done
    else
        echo "$py_version could not be found"
    fi
done

# Check the time it took to finish running the tests
echo "-----------------" >> $results_file
echo "Total time to run the tests are: $(($SECONDS / 60)) minutes and $(($SECONDS % 60)) seconds" >> $results_file