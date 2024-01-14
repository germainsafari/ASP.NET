import numpy as np
from scipy import integrate

def Integrate(f, a, b, rule="simpson"):
    if a > b:
        raise ValueError("Improper limits")

    # Determine the number of intervals
    n = max(50, int((b - a) / 0.1))

    # Create an array of values at which to evaluate the function
    x = np.linspace(a, b, n+1)

    # Evaluate the function at the points in the x array
    y = f(x)

    # Approximate the integral using the specified rule
    if rule == "rectangle-left":
        return np.sum(y[:-1]) * (b - a) / n
    elif rule == "rectangle-mid":
        midpoints = (x[:-1] + x[1:]) / 2
        return np.sum(f(midpoints)) * (b - a) / n
    elif rule == "rectangle-right":
        return np.sum(y[1:]) * (b - a) / n
    elif rule == "trapezoid":
        return (np.sum(y) - 0.5 * (y[0] + y[-1])) * (b - a) / n
    elif rule == "simpson":
        return integrate.simps(y, x)
    else:
        raise ValueError("Unknown rule")

# Test the function with the examples provided
from math import sin, exp
print(Integrate(sin, 0, 3.141593))
print(Integrate(sin, 0, 3.141593, rule="trapezoid"))
print(Integrate(lambda x: exp(x) + 1, 0, 1))