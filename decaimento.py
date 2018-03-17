# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = "Israel S. Melo Batista"
__credits__ = ["Israel S. Melo Batista", "João Gabriel M. de Paulo", 
               "André Luis O. do Nascimento"]
__version__ = "1.0"
__contact__ = "israel.silvino@gmail.com"


import numpy as np
import matplotlib.pyplot as plt

def decaimento(m0, mv, t):
    return m0*2**(-t/mv)

if __name__ == "__main__":
    
    t = np.arange(0, 5, 0.01)

    plt.plot(t, decaimento(20, 1, t))
    plt.ylabel("Massa (kg)")
    plt.xlabel("Tempo (anos)")

    plt.savefig("Decaimento.png")
