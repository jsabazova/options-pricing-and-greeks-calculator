import numpy as np
from scipy.stats import norm
import numpy as np


# this one is for euro options because exercise option only on expiry date
def black_scholes(S, X, T, r, sigma, option_type='call'):
    """
    S: Current stock price
    X: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate (decimal)
    sigma: Volatility of the stock (decimal)
    option_type: "call" for Call option, "put" for Put option
    """

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

# This is good for emarican options? bc can do anytime before expiry
def binomial_option_pricing(S, X, T, r, sigma, N, option_type="call"):
    """
    S: Stock price
    X: Strike price
    T: Time to maturity
    r: Risk-free interest rate
    sigma: Volatility
    N: Number of time steps
    option_type: "call" or "put"
    """

    dt = T / N # Time step, at each step can go up or down
    u = math.exp(sigma * math.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (math.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset prices at maturity
    asset_prices = [S * (u ** j) * (d ** (N - j)) for j in range(N + 1)]

    # Initialize option values at maturity
    if option_type == "call":
        option_values = [max(0, price - X) for price in asset_prices]
    else:
        option_values = [max(0, X - price) for price in asset_prices]

    # Step back through the binomial tree
    for i in range(N - 1, -1, -1):
        option_values = [
            (p * option_values[j + 1] + (1 - p) * option_values[j]) * math.exp(-r * dt)
            for j in range(i + 1)
        ]

    return option_values[0]


# similar flexible, for american or asian option because it can be path-dependent?
#generates a lot of possible future price paths using random vars
def monte_carlo_option_pricing(S, X, T, r, sigma, iterations, option_type="call"):
    """
    S: Current stock price
    X: Strike price
    T: Time to maturity
    r: Risk-free interest rate
    sigma: Volatility of the stock
    iterations: Number of Monte Carlo iterations
    option_type: "call" or "put"
    """
    option_payoffs = []
    
    for _ in range(iterations):
        # Simulate a random stock price at maturity
        ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * np.random.normal())
        
        if option_type == "call":
            payoff = max(0, ST - X)  # Payoff for call option
        elif option_type == "put":
            payoff = max(0, X - ST)  # Payoff for put option
        else:
            return None
        
        option_payoffs.append(payoff)
    
    # Discount the average payoff back to present value
    option_price = np.exp(-r * T) * np.mean(option_payoffs)
    
    return option_price

