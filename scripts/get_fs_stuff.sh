#!/bin/bash

# Script to get my full system required files
# Fetched files include:
#	 - Disk Image
#	 - Kernel binary
#	 - rcS template

wget https://www.eecg.toronto.edu/~elsayed9/downloads/fs_stuff.tar.gz --no-check-certificate 
tar -xzvf fs_stuff.tar.gz
