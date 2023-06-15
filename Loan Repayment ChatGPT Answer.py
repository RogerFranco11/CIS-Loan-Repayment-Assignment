# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:33:10 2023

@author: rfranco11
"""

def calculate_monthly_repayment(PV, r, n):
    """
    Calculate the monthly repayment amount for a loan.
    
    Arguments:
    PV -- Present Value (Principal loan amount) (float)
    r -- Annual interest rate (APR) (float)
    n -- Number of months (int)
    
    Returns:
    Monthly repayment amount (float)
    """
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    pmt = monthly_interest_rate * PV / (1 - (1 + monthly_interest_rate) ** -n)
    return pmt

# Example usage
PV = 12000  # Present Value (Principal loan amount)
r = 7.45  # Annual interest rate (APR)
n = 48  # Number of months

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly repayment amount:", round(monthly_repayment, 2))
