import React, { useState } from 'react';
import './App.css';

function App() {
  const [stockPrice, setStockPrice] = useState('');
  const [strikePrice, setStrikePrice] = useState('');
  const [timeToMaturity, setTimeToMaturity] = useState('');
  const [riskFreeRate, setRiskFreeRate] = useState('');
  const [volatility, setVolatility] = useState('');
  const [optionType, setOptionType] = useState('call');
  const [optionPrice, setOptionPrice] = useState(null);

  const calculateOption = async () => {
    const response = await fetch('http://127.0.0.1:5000/price_option', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        stock_price: stockPrice,
        strike_price: strikePrice,
        time_to_maturity: timeToMaturity,
        risk_free_rate: riskFreeRate,
        volatility: volatility,
        option_type: optionType,
      }),
    });
    const data = await response.json();
    setOptionPrice(data.option_price);
  };

  return (
    <div className="App">
      <h1>Black-Scholes Option Pricing Calculator</h1>
      <div className="input-group">
        <label>Stock Price:</label>
        <input
          type="number"
          value={stockPrice}
          onChange={(e) => setStockPrice(e.target.value)}
        />
      </div>

      <div className="input-group">
        <label>Strike Price:</label>
        <input
          type="number"
          value={strikePrice}
          onChange={(e) => setStrikePrice(e.target.value)}
        />
      </div>

      <div className="input-group">
        <label>Time to Maturity (years):</label>
        <input
          type="number"
          value={timeToMaturity}
          onChange={(e) => setTimeToMaturity(e.target.value)}
        />
      </div>

      <div className="input-group">
        <label>Risk-Free Rate (decimal):</label>
        <input
          type="number"
          value={riskFreeRate}
          onChange={(e) => setRiskFreeRate(e.target.value)}
        />
      </div>

      <div className="input-group">
        <label>Volatility (decimal):</label>
        <input
          type="number"
          value={volatility}
          onChange={(e) => setVolatility(e.target.value)}
        />
      </div>

      <div className="input-group">
        <label>Option Type:</label>
        <select
          value={optionType}
          onChange={(e) => setOptionType(e.target.value)}
        >
          <option value="call">Call</option>
          <option value="put">Put</option>
        </select>
      </div>

      <button onClick={calculateOption}>Calculate Option Price</button>

      {optionPrice !== null && (
        <div className="result">
          <h2>Option Price: {optionPrice.toFixed(2)}</h2>
        </div>
      )}
    </div>
  );
}

export default App;
