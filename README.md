# Black-scholes-calculator-
# Black-Scholes Option Pricing Calculator

A Python implementation of the Black-Scholes model for European options.

## Features
- Calculates call/put prices
- Uses NumPy and SciPy for fast computation

## Usage
```python
from black_scholes import black_scholes
call_price = black_scholes(100, 105, 1, 0.05, 0.2, 'call')
pip install numpy scipy
