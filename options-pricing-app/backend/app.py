from flask import Flask, request, jsonify
from flask_cors import CORS
from pricing_models import black_scholes

app = Flask(__name__)
CORS(app)
# This Flask API accepts a JSON object containing option parameters and returns the calculated price.

@app.route('/price_option', methods=['POST'])
def price_option():
    data = request.get_json()
    S = float(data['stock_price'])      # Current Stock price
    X = float(data['strike_price'])     # Strike price (at which the option can be sold/bought)
    T = float(data['time_to_maturity']) # Time to maturity/expiration 
    r = float(data['risk_free_rate'])   # Risk-free interest rate (risk free inv like gov bond etc)
    sigma = float(data['volatility'])   # Volatility 
    option_type = data['option_type']   # 'call' or 'put'

    #Notes:
    # Assume no arbitrage (no way to make risk free profit), efficient markets, long-normal distribution
    # (won't drop < 0), const volatility and int rates, no dividents during option lifespan
    
    # Calculate option price using Black-Scholes model
    price = black_scholes(S, X, T, r, sigma, option_type)
    
    return jsonify({"option_price": price})

if __name__ == '__main__':
    app.run(debug=True)
