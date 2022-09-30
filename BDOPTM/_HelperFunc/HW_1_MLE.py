import numpy as np
import pandas as pd
import os


def gaussian_func(mu, sig):
    coef = 1/(sig*np.sqrt(2*np.pi))
    exponent = - (val - mu)
    return np.exp


def calculate_MLE(mu=None, Sig2=None, verbose=False):
    if mu is None and sig is not None:
        return calculate_MLE_mu(sig2, verbose)
    elif sig2 is None and mu is not None:
        return calculate_MLE_sig2(mu)
    else:
        print("Error: ")
        print("Function must have at least mu or sig2 given")

def calculate_MLE_mu(sig2, verbose):

    pass

def calculate_MLE_sig2(mu, verbose):
    pass