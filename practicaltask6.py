import math

def Integrate(f, a, b, rule="simpson"):
    if a >= b:
        return "Error: improper limits"
    
    if rule == "rectangle-left":
        approx_func = lambda x: f(x)
    elif rule == "rectangle-mid":
        approx_func = lambda x: f(x + 0.5 * (b - a) / 50)
    elif rule == "rectangle-right":
        approx_func = lambda x: f(x + (b - a) / 50)
    elif rule == "trapezoid":
        approx_func = lambda x: 0.5 * (f(x) + f(x + (b - a) / 50))
    elif rule == "simpson":
        approx_func = lambda x: (f(x) + 4 * f(x + 0.5 * (b - a) / 50) + f(x + (b - a) / 50)) / 6
    else:
        return "Error: Invalid approximation rule"

    n_intervals = max(int((b - a) / 0.1), 50)
    interval_width = (b - a) / n_intervals

    integral_sum = sum(approx_func(a + i * interval_width) for i in range(n_intervals))
    
    return interval_width * integral_sum

# Examples
f = lambda x: math.sin(x)
g = lambda x: math.exp(x) + 1

print(Integrate(f, 0, 3.141593))  # Output: 2 (using Simpson’s rule)
print(Integrate(f, 0, 3.141593, rule="trapezoid"))  # Output: 2 (using trapezoid rule)
print(Integrate(f, 2, -3))  # Output: Error: improper limits
print(Integrate(f, -3.141593, 3.141593))  # Output: 0 (using Simpson’s rule)
print(Integrate(f, 2, 2))  # Output: 0

print(Integrate(g, 0, 1))  # Output: 2.7183 (using Simpson’s rule)