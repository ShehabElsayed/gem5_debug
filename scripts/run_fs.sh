#!/bin/bash

# Script to run multithreaded hello benchmark with a given number of threads
# on system with the same number of cores
# Takes number of threads as an argument

NUM_THREADS=$1

# Create rcS file form template
if [ -f fs_stuff/rcs/testing_hello.rcS ]; then
	rm fs_stuff/rcs/testing_hello.rcS
fi
cp fs_stuff/rcs/testing_hello_template.rcS fs_stuff/rcs/testing_hello.rcS
sed -i "s/_NUM_THREADS_/${NUM_THREADS}/g" fs_stuff/rcs/testing_hello.rcS

# Run gem5
sudo ./build/X86/gem5.opt configs/myconfigs/run_fs.py --script="fs_stuff/rcs/testing_hello.rcS" --cpus ${NUM_THREADS}
