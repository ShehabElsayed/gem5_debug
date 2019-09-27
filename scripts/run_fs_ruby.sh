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
sudo ./build/X86_MOESI_hammer/gem5.opt \
	--debug-flags=LSQUnit,LSQ,Commit,ROB,IEW,IQ,Decode,Fault,MemDepUnit \
	--debug-start=13800000000000000 \
	configs/myconfigs/run_fs_ruby.py \
	--script="fs_stuff/rcs/testing_hello.rcS" \
	--num_cpus ${NUM_THREADS}
