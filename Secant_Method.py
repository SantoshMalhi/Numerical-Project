import matplotlib.pyplot as plt
import numpy as np

def secant_method(f, x0, x1, tol, max_iter):
    iter_count = 0
    while iter_count < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x1 - f_x0) < tol:
            print("Denominator is too small, method fails.") 
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x2 - x1) < tol:
            return x2, iter_count

        x0, x1 = x1, x2
        iter_count += 1

    print("Method did not converge.")
    return None

# Example function
def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Example: (x-1)(x-2)(x-3)

# Initial guesses
x0 = 2.0
x1 = 3.5

# Parameters
tol = 1e-6
max_iter = 100

# Finding root
root, iterations = secant_method(f, x0, x1, tol, max_iter)
if root is not None:
    print(f"Root found: {root} in {iterations} iterations")

# Plotting the function and root
x = np.linspace(0, 4, 400)
y = f(x)

plt.plot(x, y, label='f(x) = x^3 - 6x^2 + 11x - 6')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(root, color='red', linestyle='--', label=f'Root at x={root:.4f}')
plt.scatter([x0, x1], [f(x0), f(x1)], color='blue', zorder=5)
plt.legend()
plt.title('Secant Method for Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
