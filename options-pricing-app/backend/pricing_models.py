import numpy as np
from scipy.stats import norm
"""
S: Current stock price
X: Strike price
T: Time to maturity (in years)
r: Risk-free interest rate (decimal)
sigma: Volatility of the stock (decimal)
option_type: "call" for Call option, "put" for Put option
"""

def black_scholes(S, X, T, r, sigma, option_type='call'):
    # Calculate d1 and d2
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        # Call option price
        price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        # Put option price
        price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return price
