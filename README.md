# Univariate N-degree Equation Numerical Solver (Enhanced Version)

This is a Python implementation of a univariate N-degree equation numerical solver that supports multiple numerical methods to find equation roots, including **Aberth iteration method** and **complex root** support.

## Features

- **Multiple numerical methods**: Supports bisection method, Newton's method, secant method
- **Aberth iteration method**: Specifically designed for solving all roots of polynomial equations
- **Complex root support**: Can find and handle complex roots
- **Automatic root finding**: Automatically finds all roots in a specified range
- **Visualization**: Plots function graphs and root distribution in the complex plane
- **User-friendly**: Provides interactive interface and preset examples
- **High precision**: Supports customizable precision requirements

## Core Algorithm

### Aberth Iteration + Newton Refinement

This is the core algorithm of the program, combining the advantages of two methods:

1. **Aberth iteration**: Simultaneously updates all root estimates, avoiding convergence to the same root
2. **Newton refinement**: High-precision refinement for each root

**Algorithm steps:**

```python
# 1. Randomly generate initial root estimates
z = [complex(random.uniform(-range, range), random.uniform(-range, range)) for _ in range(degree)]

# 2. Aberth iteration
for k in range(max_iter):
    for i in range(N):
        # Calculate f(z[i]) / f'(z[i])
        c = f(z[i]) / df(z[i])

        # Calculate sum term 1/(z[i] - z[j])
        s = sum(1/(z[i] - z[j]) for j in range(N) if j != i)

        # Update w[i]
        w[i] = 1 / (c - s)

    # Update root estimates
    z[i] = z[i] - w[i]

# 3. Newton refinement
for root in z:
    for _ in range(newton_iter):
        root = root - f(root) / df(root)
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run the program

```bash
python main.py
```

### Program options

The program provides the following options:

1. **x³ - 2x + 1 = 0** - Cubic equation example
2. **x² - 4 = 0** - Quadratic equation example
3. **x⁴ - 5x² + 4 = 0** - Quartic equation example
4. **x³ + 1 = 0** - Equation with complex roots example
5. **Custom equation** - Enter your own equation coefficients

### Custom equation input format

For equation: aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ = 0

Enter coefficients: `aₙ aₙ₋₁ ... a₁ a₀`

**Examples:**

- x³ - 2x + 1 = 0 → Enter: `1 0 -2 1`
- x² - 4 = 0 → Enter: `1 0 -4`
- x⁴ - 5x² + 4 = 0 → Enter: `1 0 -5 0 4`
- x³ + 1 = 0 → Enter: `1 0 0 1`

## Numerical Methods

### 1. Aberth Iteration Method (Aberth Method)

- **Principle**: Simultaneously updates all root estimates, avoiding convergence to the same root
- **Advantages**: Can find all roots, including complex roots
- **Disadvantages**: Higher computational complexity
- **Applicable**: All root solving for polynomial equations

### 2. Newton's Method (Newton's Method)

- **Principle**: Uses the tangent line at a point to approximate the root
- **Advantages**: Fast convergence (quadratic convergence)
- **Disadvantages**: Requires derivative calculation, sensitive to initial values
- **Applicable**: Smooth functions with initial values close to roots

### 3. Bisection Method (Bisection Method)

- **Principle**: Uses the property that continuous functions have opposite signs at interval endpoints
- **Advantages**: Stable convergence, independent of initial values
- **Disadvantages**: Slow convergence
- **Applicable**: Scenarios requiring stable convergence

### 4. Secant Method (Secant Method)

- **Principle**: Uses secant lines instead of tangent lines to avoid derivative calculation
- **Advantages**: No derivative calculation needed, relatively fast convergence
- **Disadvantages**: Requires two initial values
- **Applicable**: Cases where derivative calculation is difficult

## Program Output

The program will output:

1. Basic information about the equation
2. All found roots (including complex roots) and their verification
3. Dual graph display:
   - Function graph (real part) and real root positions
   - Root distribution in the complex plane

## Example Output

```
=== Univariate N-degree Equation Numerical Solver (Enhanced Version) ===

Equation: x^3 + 1 = 0
Degree: 3

Solving all roots using Aberth+Newton method...
Found 3 roots:
Root 1: x = -1.00000000 (real root)
Verification: f(-1.00000000) = 0.00e+00
Root 2: x = 0.50000000 + 0.86602540i (complex root)
Verification: f(0.50000000 + 0.86602540i) = 1.11e-16
Root 3: x = 0.50000000 - 0.86602540i (complex root)
Verification: f(0.50000000 - 0.86602540i) = 1.11e-16
```

## Complex Root Handling

The program can:

- Automatically identify real roots and complex roots
- Visualize root distribution in the complex plane
- Handle conjugate complex root pairs
- Verify the correctness of complex roots

## Notes

1. Ensure the input coefficients are correct, from highest to lowest degree
2. Aberth iteration is sensitive to initial values, the program uses random initialization
3. Complex roots will be displayed in the form a + bi
4. Graph display requires graphical interface support
5. The program automatically removes duplicate roots

## Technical Implementation

- **Language**: Python 3.7+
- **Main libraries**: NumPy (numerical computation), Matplotlib (plotting)
- **Design pattern**: Object-oriented design with good encapsulation
- **Error handling**: Includes division by zero checks, convergence judgments, etc.
- **Complex number support**: Uses Python's built-in complex type

## Extensible Features

Features that can be easily extended:

- Add more numerical methods (e.g., Steffensen method, Muller method)
- Support for multiple root detection and handling
- Add equation system solving
- Support for symbolic computation
- Add more visualization options
- Support for high-precision computation (using mpmath library)
# polynomial-root-finder
