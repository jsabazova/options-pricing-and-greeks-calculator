# options-pricing-and-greeks-calculator
# My notes on everything I learnt this weekend 16 Sep 2024 

### **1. What is an Option?**

An **option** is a financial contract that gives the buyer the **right**, but not the obligation, to buy or sell an underlying asset (like a stock) at a specific price, on or before a specific date. There are two main types of options:
- **Call Option:** The right to buy the asset.
- **Put Option:** The right to sell the asset.

#### Example:
Let’s say you buy a **call option** on Apple stock. You pay $5 for the option (called the **premium**). This option gives you the right to buy 1 share of Apple for $100 (this is called the **strike price**) at any time over the next month. If Apple’s stock price goes up to $120, you can still buy it for $100 using the option, making a $20 profit (minus the $5 you paid for the option).

If the stock doesn’t go above $100, you won’t use the option (you let it expire), and your only loss is the $5 you paid for the option.

### **2. What is Options Pricing?**

Options are valuable because they give you the flexibility to capitalize on future price movements of a stock. But how much should an option be worth? That’s where **options pricing** models come in. They estimate the **fair value** of an option based on several factors:
- **Current stock price** (How much is the stock worth today?)
- **Strike price** (The price at which the option lets you buy/sell the stock)
- **Time to expiration** (How long before the option expires)
- **Volatility** (How much the stock price is expected to fluctuate)
- **Risk-free interest rate** (The interest rate on a risk-free investment, like a government bond)

The **Black-Scholes Model** is one of the most popular models for pricing options, especially **European options** (which can only be exercised at expiration, unlike American options which can be exercised anytime).

---

### **3. The Black-Scholes Model: What It Does**

The **Black-Scholes Model** is a mathematical formula used to estimate the price of a European call or put option. It was developed by Fischer Black and Myron Scholes in 1973 and was revolutionary because it provided a closed-form solution (a formula) to calculate the theoretical price of an option.

In simple terms, the Black-Scholes model tells you:
- What should the option cost based on today’s market conditions?
- How sensitive is the option price to different factors (like time, stock price, or volatility)?

---

### **4. The Main Idea Behind the Black-Scholes Model**

The Black-Scholes model is based on several assumptions:
1. **No arbitrage:** There’s no way to make a risk-free profit from trading options.
2. **Efficient markets:** Stock prices move randomly but follow a predictable pattern over time.
3. **Stock prices follow a "log-normal distribution"**: This means stock prices can rise or fall over time, but they won’t drop below zero.
4. **Constant volatility and interest rates**: The volatility of the stock and the interest rates are assumed to be constant over the life of the option.
5. **No dividends:** The model assumes that the stock doesn’t pay any dividends during the life of the option.

The Black-Scholes model calculates the **option price** by considering how much risk is involved and how much time is left until the option expires. It uses statistical methods from probability theory (like the normal distribution) to account for the randomness of stock price movements.

---

### **5. The Formula Itself**

The Black-Scholes formula for a **call option** is:

\[
C = S_0 N(d_1) - X e^{-rT} N(d_2)
\]

Let’s break down what each term means:
- \( C \): The price of the call option.
- \( S_0 \): The current price of the underlying stock (e.g., Apple stock today).
- \( X \): The strike price (the price at which you have the right to buy the stock).
- \( T \): The time until the option expires (expressed as a fraction of a year, like 0.25 years for three months).
- \( r \): The risk-free interest rate (usually the rate on government bonds).
- \( \sigma \): The volatility of the stock price (how much the stock price is expected to fluctuate).
- \( N(d_1) \) and \( N(d_2) \): These are the values from the **cumulative normal distribution** (the bell curve that shows probabilities). Essentially, they tell you the likelihood of the stock price moving in your favor.

### **6. Breaking Down \( d_1 \) and \( d_2 \)**

The terms \( d_1 \) and \( d_2 \) are calculated as:

\[
d_1 = \frac{\ln(S_0 / X) + (r + 0.5 \sigma^2) T}{\sigma \sqrt{T}}
\]
\[
d_2 = d_1 - \sigma \sqrt{T}
\]

- \( d_1 \) and \( d_2 \) represent "z-scores" or how many standard deviations a particular outcome (like the stock reaching a certain price) is away from the average. They factor in the relationship between the current stock price, strike price, interest rates, time, and volatility.
- \( N(d_1) \) is the probability that the option will expire **in the money** (meaning the stock price will be above the strike price, making the call option valuable).
- \( N(d_2) \) is related to the probability that the **option will be exercised** after accounting for the time value of money.

### **7. Interpretation of the Formula**

- The term \( S_0 N(d_1) \) represents the **expected gain** from owning the stock.
- The term \( X e^{-rT} N(d_2) \) represents the **present value** of the strike price you’ll have to pay when you exercise the option.

The difference between these two terms gives the fair value of the call option.

### **8. The Black-Scholes Formula for Put Options**

There’s also a version of the Black-Scholes formula for **put options** (which give the right to sell the stock). The formula is:

\[
P = X e^{-rT} N(-d_2) - S_0 N(-d_1)
\]

This is very similar to the call option formula but reflects the value of being able to sell the stock at the strike price rather than buy it.

---

### **9. What are "Greeks" in Options Pricing?**

The **Greeks** are sensitivities that measure how much an option’s price will change with respect to different factors:
- **Delta (Δ):** How much the option price changes when the stock price changes.
- **Gamma (Γ):** How much Delta changes when the stock price changes.
- **Theta (Θ):** How much the option price changes as time passes (the effect of time decay).
- **Vega (V):** How much the option price changes when volatility changes.
- **Rho (ρ):** How much the option price changes when interest rates change.

These are important because they help traders understand how their option positions will react to changes in market conditions.

---

### **10. Why is the Black-Scholes Model Important?**

- **Simplicity:** The Black-Scholes formula provides a relatively simple way to estimate the fair value of an option.
- **Market Efficiency:** Many financial markets use the Black-Scholes model as a benchmark for pricing options. Even though it has limitations (like assuming constant volatility), it’s still widely used.
- **Risk Management:** The model and its extensions are used by traders and financial institutions to manage risk, hedge positions, and develop trading strategies.

<img width="718" alt="Screenshot 2024-09-15 at 11 27 58 pm" src="https://github.com/user-attachments/assets/5a080a3a-a70b-4331-8c6d-6d096647f9ec">
