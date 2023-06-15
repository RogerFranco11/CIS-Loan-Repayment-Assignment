# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:42:14 2023

@author: rfranco11

Pmt = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month 


"""

def Idunno(PV, r, n):
    
    """
    Parameters 
    ----------
    PV : TYPE Float
    DESCRIPTION, Present value (amt borrow)
    r : TYPE Float 
    DESCRIPTION, Interest rate APR
    n: TYPE Integer
    DESCRIPTION, Number of months to pay back loan 
    
    Returns
    -------
    Pmt : TYPE Float
    DESCRIPTION, amt paid per month 
    
    """
    
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt 

#input the pv
import numpy as np

n = 48
PV = input('enter PV: ')
PV = float(PV)

#equivalently PV = float(input('enter PV: '))

print(f"PV = {PV} \n")

r = input ('interest APR: ')
r = float(r)/100
r = r/12
print(f"interest = {r: 0.3f}")

pmt = Idunno(PV, r, n)
pmt = np.round(pmt, 2)
print (f"payment is {pmt: } per month")
