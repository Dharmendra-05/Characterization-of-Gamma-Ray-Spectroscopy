import numpy as np

# Sample Data (Based on Eu-152 peaks)
# Channel Numbers from the detector
x = np.array([100, 200, 300, 1000], dtype=float)
# Actual Energy values (keV)
y = np.array([121.7, 244.6, 344.2, 1408.0], dtype=float)

# Fit a quadratic (degree 2) polynomial: y = c*x^2 + b*x + a
coeffs = np.polyfit(x, y, 2)

# coeffs returns [c, b, a] (highest power first)
c, b, a = coeffs

print("Calibration Parameters:")
print(f"a (Offset) = {a}")
print(f"b (Linear) = {b}")
print(f"c (Quadratic) = {c}")