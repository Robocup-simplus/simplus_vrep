"""
            A2 Basic Libraris [Basic]

            Created on 2020.May.27

    This Is the first part of RoboCup SimPlus Simulation Tutorial
    For working with this simulator you need basic knowledge about python programming
    In this session we practice some fun trick in python and introducing a few essential libraries
    If you are familiar with following python concepts.

    List of Tutorial Materials:
        ## 1. os
        ## 2. time
        ## 3. random
        ## 4. math
"""

################################
## 1. OS Operations
################################
import os  # import os module

os.getcwd()  # => Current Working Directory same as `pwd` in bash

path = '/'  # Some path
os.listdir(path)  # List files and directories inside the given path same as `ls` in bash
os.chdir(path)  # Change directory to the given path same as `cd` in bash
os.path.join(path, 'new_path')  # merging two path together independent of your current OS

################################
## 2. time
################################
import time

time.time()  # Current time in seconds
time.time_ns() # Current time in nano seconds

# It's useful to measure performance of a part of code
start_time = time.time()
do_something()
end_time = time.time()
end_time - start_time # Time elapsed during your function in seconds


################################
## 3. Random
################################
import random

random.seed(0) # set seed of random to 0

random.random()  # A float random number in range [0,1]
random.randint(a, b) # A integer random number in range of [a,b]
random.randrange(start, stop, step) # a random number between [start,stop] only number divided by step

random.gauss(mu, var ** 0.5) # Generate a random number on normal(gauss) disterbution with median on `mu` and variance of `var`


################################
## 4. Math
################################
import math
# This library contains most of mathematics functions and constant you need
math.e  # NUMBER e = 2.72....
math.pi  # NUMBER pi = 3.1415...

# Trigonometry Functions
math.sin(0)
math.cos(0)
math.tan(0)
math.tanh(0)
math.asin(0)

