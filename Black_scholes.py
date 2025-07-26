import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    # Price calculation
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    # Greeks calculations
    delta = norm.cdf(d1) if option_type == 'call' else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T) * 0.01  # 1% vol change
    theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - 
             r * K * np.exp(-r*T) * norm.cdf(d2)) / 365  # Daily decay
    
    return {
        'price': price,
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta
    }

if __name__ == "__main__":
    result = black_scholes(100, 105, 1, 0.05, 0.2, 'call')
    print("=== Option Metrics ===")
    print(f"Price: ${result['price']:.2f}")
    print(f"Delta: {result['delta']:.4f}")
    print(f"Gamma: {result['gamma']:.6f}")
    print(f"Vega: {result['vega']:.4f} (per 1% vol change)")
    print(f"Theta: {result['theta']:.4f} (daily time decay)")