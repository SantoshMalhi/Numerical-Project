# Secant Method Implementation in Python

## Overview

This project demonstrates the implementation of the Secant Method in Python for finding the roots of a real-valued function. The Secant Method is a numerical technique that approximates the derivative of a function using finite differences and iteratively refines the estimate of the root.


## Introduction

The Secant Method is an iterative root-finding algorithm that is particularly useful when the derivative of the function is difficult to calculate. Unlike the Newton-Raphson method, which requires the derivative, the Secant Method uses two initial approximations to construct a secant line and find the root.

## Getting Started

### Prerequisites

Make sure you have Python installed. Additionally, you'll need the following Python libraries:
- NumPy
- Matplotlib

You can install these libraries using pip:

```sh
pip install numpy matplotlib
```

### Installation

Clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/secant-method-python.git
cd secant-method-python
```

## Usage

### Running the Code

You can run the implementation script directly:

```sh
python secant_method.py
```

## Code Explanation

### Function Definitions

- **secant_method(f, x0, x1, tol, max_iter)**: This function implements the Secant Method to find the root of the function `f`.
  - `f`: The function for which we are finding the root.
  - `x0`, `x1`: Initial guesses for the root.
  - `tol`: Tolerance level for stopping criterion.
  - `max_iter`: Maximum number of iterations.

### Example Function

An example function `f(x) = x^3 - 6x^2 + 11x - 6` is used to demonstrate the method. You can replace this with any other function as needed.

### Iteration and Convergence

The method iteratively updates the estimates of the root until the difference between successive approximations is less than the specified tolerance.

## Example

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

x0 = 2.0
x1 = 3.5
tol = 1e-6
max_iter = 100

root, iterations = secant_method(f, x0, x1, tol, max_iter)
if root is not None:
    print(f"Root found: {root} in {iterations} iterations")
```

## Plotting the Results

The script also includes a section for plotting the function and the root using Matplotlib.

```python
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
```

## Conclusion

The Secant Method is an effective numerical technique for root finding, especially when the derivative of the function is not readily available. This implementation in Python demonstrates its practical application with a simple example and visual representation.


## Acknowledgements

- The project uses Python's NumPy and Matplotlib libraries.
- Inspired by numerical methods coursework and practical assignments.
