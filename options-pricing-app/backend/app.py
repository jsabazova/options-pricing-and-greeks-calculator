from flask import Flask, request, jsonify
from pricing_models import black_scholes

app = Flask(__name__)

# This Flask API accepts a JSON object containing option parameters and returns the calculated price.

@app.route('/price_option', methods=['POST'])
def price_option():
    data = request.json
    S = data['S']  # Current Stock price
    X = data['X']  # Strike price (at which the option can be sold/bought)
    T = data['T']  # Time to maturity/expiration 
    r = data['r']  # Risk-free interest rate (risk free inv like gov bond etc)
    sigma = data['sigma']  # Volatility 
    option_type = data['option_type']  # 'call' or 'put'

    #Notes:
    # Assume no arbitrage (no way to make risk free profit), efficient markets, long-normal distribution
    # (won't drop < 0), const volatility and int rates, no dividents during option lifespan
    
    # Calculate option price using Black-Scholes model
    price = black_scholes(S, X, T, r, sigma, option_type)
    
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
