import numpy as np
from pprint import pprint

# -*- coding: utf-8 -*-

"""
A2-Part-1: Generate a sinusoid

Write a function to generate a real sinusoid (use np.cos()) given its amplitude A, frequency f (Hz), initial phase phi (radians), 
sampling rate fs (Hz) and duration t (seconds). 

All the input arguments to this function (A, f, phi, fs and t) are real numbers such that A, t and fs are 
positive, and fs > 2*f to avoid aliasing. The function should return a numpy array x of the generated 
sinusoid.

EXAMPLE: If you run your code using A=1.0, f = 10.0, phi = 1.0, fs = 50.0 and t = 0.1, the output numpy 
array should be: array([ 0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906])
"""

def genSine(A, f, phi, fs, t):
    x = []
    """
    Inputs:
        A (float) =  amplitude of the sinusoid
        f (float) = frequency of the sinusoid in Hz
        phi (float) = initial phase of the sinusoid in radians
        fs (float) = sampling frequency of the sinusoid in Hz
        t (float) =  duration of the sinusoid (is second)
    Output:
        The function should return a numpy array
        x (numpy array) = The generated sinusoid (use np.cos())
    """
    ## Your code here

    ## Your code here

    #   where, x is the array of real values of the sinusoid, n is an integer value expressing
    #   the time index, A is the amplitude value of the sinusoid, f is the frequency value
    #   of the sinusoid in Hz, T is the sampling period equal to 1/fs, fs is the sampling
    #   frequency in Hz, and phi is the initial phase of the sinusoid in radians.

    i = 0
    # while i < round(fs * t):
    for i in range(0, int(round(fs * t))):
      x.append(np.cos (2 * np.pi * f * i * (1/fs) + phi))

    return np.array(x);


"""
EXAMPLE: If you run your code using A=1.0, f = 10.0, phi = 1.0, fs = 50.0 and t = 0.1, the output numpy 
array should be: array([ 0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906])
"""


# A = 1.0
# f = 10.0
# phi = 1.0
# fs = 50.0
# t = 0.1
# x = genSine(A, f, phi, fs, t)
# 
# pprint(x)
# np.testing.assert_almost_equal(x, [ 0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906 ])

# vim: set fileencoding=utf-8
