import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, List, Union
import math
import random
import time
from cmath import sqrt

class ComplexEquationSolver:
    """Complex root solver for univariate N-degree polynomial equations"""
    
    def __init__(self, coefficients: List[float]):
        """
        Initialize the equation solver
        
        Args:
            coefficients: List of coefficients from highest to lowest degree
                         Example: [1, 0, -2, 1] represents x^3 - 2x + 1 = 0
        """
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
    
    def f(self, x: Union[float, complex]) -> Union[float, complex]:
        """Calculate function value f(x) - supports complex numbers"""
        if isinstance(x, (int, float)):
            x = complex(x, 0)
        
        result = complex(0, 0)
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (self.degree - i))
        return result
    
    def df(self, x: Union[float, complex]) -> Union[float, complex]:
        """Calculate derivative value f'(x) - supports complex numbers"""
        if isinstance(x, (int, float)):
            x = complex(x, 0)
        
        result = complex(0, 0)
        for i, coef in enumerate(self.coefficients[:-1]):  # Last term derivative is 0
            power = self.degree - i - 1
            if power >= 0:
                result += coef * (self.degree - i) * (x ** power)
        return result
    
    def f_k_derivative(self, x: complex, k: int) -> complex:
        """
        Calculate k-th derivative value f^(k)(x)
        
        Args:
            x: Independent variable (complex)
            k: Derivative order
            
        Returns:
            k-th derivative value
        """
        if k == 0:
            return self.f(x)
        elif k == 1:
            return self.df(x)
        
        # Calculate k-th derivative coefficients
        coeffs_k = []
        for i in range(self.degree - k + 1):
            if i + k <= self.degree:
                # Calculate combination C(n,k) * k!
                factorial = 1
                for j in range(i + k, i, -1):
                    factorial *= j
                coeffs_k.append(self.coefficients[i] * factorial)
        
        # Use Horner's method to calculate k-th derivative value
        result = complex(0, 0)
        if coeffs_k:
            result = coeffs_k[0]
            for i in range(1, len(coeffs_k)):
                result = result * x + coeffs_k[i]
        
        return result
    
    def aberth_method(self, z: List[complex], max_iter: int = 50, tol: float = 1e-10) -> List[complex]:
        """
        Aberth iteration method for solving all roots of polynomial equations
        
        Args:
            z: Initial root estimates (complex list)
            max_iter: Maximum number of iterations
            tol: Convergence tolerance
            
        Returns:
            Converged root list
        """
        N = len(z)
        z = z.copy()
        
        for k in range(max_iter):
            w = [complex(0, 0)] * N
            
            for i in range(N):
                # Calculate f(z[i]) / f'(z[i])
                f_val = self.f(z[i])
                df_val = self.df(z[i])
                
                if abs(df_val) < 1e-12:  # Avoid division by zero
                    continue
                
                c = f_val / df_val
                
                # Calculate sum term 1/(z[i] - z[j])
                s = complex(0, 0)
                for j in range(N):
                    if j != i:
                        diff = z[i] - z[j]
                        if abs(diff) > 1e-12:
                            s += complex(1, 0) / diff
                
                # Update w[i]
                w[i] = complex(1, 0) / (c - s)
            
            # Update root estimates
            converged = True
            for i in range(N):
                z_new = z[i] - w[i]
                if abs(z_new - z[i]) > tol:
                    converged = False
                z[i] = z_new
            
            if converged:
                break
        
        return z
    
    def newton_refinement(self, z: List[complex], max_iter: int = 20, tol: float = 1e-12) -> List[complex]:
        """
        Use Newton's method to refine roots
        
        Args:
            z: Initial root estimates
            max_iter: Maximum number of iterations
            tol: Convergence tolerance
            
        Returns:
            Refined root list
        """
        refined_roots = []
        
        for root in z:
            x = root
            for _ in range(max_iter):
                f_val = self.f(x)
                df_val = self.df(x)
                
                if abs(df_val) < 1e-12:
                    break
                
                x_new = x - f_val / df_val
                
                if abs(x_new - x) < tol:
                    x = x_new
                    break
                
                x = x_new
            
            refined_roots.append(x)
        
        return refined_roots
    
    def solve_all_roots(self, range_val: float = 10.0, aberth_iter: int = 100, newton_iter: int = 30) -> List[complex]:
        """
        Use Aberth+Newton method to solve all roots
        
        Args:
            range_val: Range for initial root estimates
            aberth_iter: Number of Aberth iterations
            newton_iter: Number of Newton iterations
            
        Returns:
            All roots (complex)
        """
        # Set random seed
        random.seed(int(time.time()))
        
        all_roots = []
        
        # Try multiple runs with different initial conditions to ensure we find all roots
        for run in range(5):  # Run 5 times with different initial conditions
            # Generate initial root estimates with different strategies
            z = []
            if run == 0:
                # Strategy 1: Random points in a large range
                for i in range(self.degree):
                    r1 = random.uniform(-range_val, range_val)
                    r2 = random.uniform(-range_val, range_val)
                    z.append(complex(r1, r2))
            elif run == 1:
                # Strategy 2: Points on a circle
                radius = range_val * 0.5
                for i in range(self.degree):
                    angle = 2 * math.pi * i / self.degree
                    r1 = radius * math.cos(angle)
                    r2 = radius * math.sin(angle)
                    z.append(complex(r1, r2))
            elif run == 2:
                # Strategy 3: Points in a smaller range
                for i in range(self.degree):
                    r1 = random.uniform(-range_val * 0.3, range_val * 0.3)
                    r2 = random.uniform(-range_val * 0.3, range_val * 0.3)
                    z.append(complex(r1, r2))
            elif run == 3:
                # Strategy 4: Points along real axis
                for i in range(self.degree):
                    r1 = random.uniform(-range_val, range_val)
                    r2 = random.uniform(-0.1, 0.1)
                    z.append(complex(r1, r2))
            else:
                # Strategy 5: Points with larger imaginary parts
                for i in range(self.degree):
                    r1 = random.uniform(-range_val * 0.5, range_val * 0.5)
                    r2 = random.uniform(-range_val * 0.5, range_val * 0.5)
                    z.append(complex(r1, r2))
            
            # Aberth iteration
            z = self.aberth_method(z, aberth_iter)
            
            # Newton refinement
            z = self.newton_refinement(z, newton_iter)
            
            # Add new roots to the collection
            for root in z:
                is_duplicate = False
                for existing_root in all_roots:
                    if abs(root - existing_root) < 1e-6:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    all_roots.append(root)
        
        # Additional search for roots near the origin
        if len(all_roots) < self.degree:
            # Try some specific starting points
            test_points = [
                complex(0, 0), complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1),
                complex(1, 1), complex(-1, 1), complex(1, -1), complex(-1, -1)
            ]
            
            for start_point in test_points:
                # Use Newton's method from this starting point
                x = start_point
                for _ in range(50):
                    f_val = self.f(x)
                    df_val = self.df(x)
                    
                    if abs(df_val) < 1e-12:
                        break
                    
                    x_new = x - f_val / df_val
                    
                    if abs(x_new - x) < 1e-12:
                        x = x_new
                        break
                    
                    x = x_new
                
                # Check if this is a new root
                is_duplicate = False
                for existing_root in all_roots:
                    if abs(x - existing_root) < 1e-6:
                        is_duplicate = True
                        break
                if not is_duplicate and abs(self.f(x)) < 1e-6:
                    all_roots.append(x)
        
        return all_roots
    
    def plot_complex_roots(self, roots: List[complex], x_range: Tuple[float, float] = None):
        """
        Plot complex roots distribution in the complex plane
        
        Args:
            roots: Root list
            x_range: x-axis range (if None, will auto-adjust)
        """
        if not roots:
            print("No roots to plot")
            return
        
        # Auto-adjust range to include all roots
        if x_range is None:
            real_parts = [root.real for root in roots]
            imag_parts = [root.imag for root in roots]
            
            min_real, max_real = min(real_parts), max(real_parts)
            min_imag, max_imag = min(imag_parts), max(imag_parts)
            
            # Add some padding
            padding = max(max_real - min_real, max_imag - min_imag) * 0.3
            if padding == 0:
                padding = 1.0
            
            x_range = (min_real - padding, max_real + padding)
            y_range = (min_imag - padding, max_imag + padding)
        else:
            y_range = x_range
        
        # Set style for better appearance
        plt.style.use('default')
        
        # Plot function graph (real part)
        x = np.linspace(x_range[0], x_range[1], 1000)
        y_real = [self.f(complex(xi, 0)).real for xi in x]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
        
        # Subplot 1: Function graph
        ax1.plot(x, y_real, color='#2E86AB', linewidth=2.5)
        ax1.axhline(y=0, color='#333333', linestyle='-', alpha=0.5, linewidth=1)
        ax1.axvline(x=0, color='#333333', linestyle='-', alpha=0.5, linewidth=1)
        
        # Mark real roots
        real_roots = [root for root in roots if abs(root.imag) < 1e-10]
        for i, root in enumerate(real_roots):
            ax1.plot(root.real, 0, 'o', color='#D62828', markersize=12, 
                    markeredgecolor='white', markeredgewidth=2)
        
        ax1.set_xlabel('x', fontsize=12, fontweight='bold')
        ax1.set_ylabel('f(x)', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3, linestyle='--')
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        
        # Subplot 2: Root distribution in complex plane
        real_parts = [root.real for root in roots]
        imag_parts = [root.imag for root in roots]
        
        # Use different colors and sizes for real and complex roots
        colors = ['#D62828' if abs(root.imag) < 1e-10 else '#2E86AB' for root in roots]
        sizes = [200 if abs(root.imag) < 1e-10 else 150 for root in roots]
        edge_colors = ['white' if abs(root.imag) < 1e-10 else '#1B4965' for root in roots]
        
        scatter = ax2.scatter(real_parts, imag_parts, c=colors, s=sizes, alpha=0.8, 
                             edgecolors=edge_colors, linewidth=2)
        
        ax2.axhline(y=0, color='#333333', linestyle='-', alpha=0.5, linewidth=1)
        ax2.axvline(x=0, color='#333333', linestyle='-', alpha=0.5, linewidth=1)
        
        # Smart annotation placement to avoid overlaps
        def get_annotation_offset(i, total, root):
            """Calculate smart offset for annotation to avoid overlaps"""
            # Base offset
            base_offset = 15
            
            # Different quadrants get different base positions
            if root.real >= 0 and root.imag >= 0:  # Q1
                base_x, base_y = base_offset, base_offset
            elif root.real < 0 and root.imag >= 0:  # Q2
                base_x, base_y = -base_offset, base_offset
            elif root.real < 0 and root.imag < 0:  # Q3
                base_x, base_y = -base_offset, -base_offset
            else:  # Q4
                base_x, base_y = base_offset, -base_offset
            
            # Add some variation based on index to spread out labels
            angle = 2 * math.pi * i / total
            variation = 5
            base_x += variation * math.cos(angle)
            base_y += variation * math.sin(angle)
            
            return base_x, base_y
        
        # Mark roots with values using smart placement
        for i, root in enumerate(roots):
            offset_x, offset_y = get_annotation_offset(i, len(roots), root)
            
            if abs(root.imag) < 1e-10:
                # Real root
                label = f'x = {root.real:.6f}'
                ax2.annotate(label, (root.real, root.imag), 
                            xytext=(offset_x, offset_y), textcoords='offset points', 
                            fontsize=10, fontweight='bold', color='#D62828',
                            bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                    edgecolor='#D62828', alpha=0.9),
                            arrowprops=dict(arrowstyle='->', color='#D62828', alpha=0.7))
            else:
                # Complex root
                if root.imag > 0:
                    label = f'x = {root.real:.6f} + {root.imag:.6f}i'
                else:
                    label = f'x = {root.real:.6f} - {abs(root.imag):.6f}i'
                
                ax2.annotate(label, (root.real, root.imag), 
                            xytext=(offset_x, offset_y), textcoords='offset points', 
                            fontsize=10, fontweight='bold', color='#2E86AB',
                            bbox=dict(boxstyle="round,pad=0.2", facecolor='white', 
                                    edgecolor='#2E86AB', alpha=0.9),
                            arrowprops=dict(arrowstyle='->', color='#2E86AB', alpha=0.7))
        
        ax2.set_xlabel('Real Part', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Imaginary Part', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3, linestyle='--')
        ax2.axis('equal')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        
        # Set axis limits with extra padding for labels
        ax2.set_xlim(x_range)
        ax2.set_ylim(y_range)
        
        plt.tight_layout()
        plt.show()
    
    def _get_equation_string(self) -> str:
        """Get string representation of the equation"""
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            
            power = self.degree - i
            if power == 0:
                term = f"{coef}"
            elif power == 1:
                term = f"{coef}x" if coef != 1 else "x"
            else:
                term = f"{coef}x^{power}" if coef != 1 else f"x^{power}"
            
            if i > 0 and coef > 0:
                term = "+ " + term
            
            terms.append(term)
        
        return " ".join(terms) if terms else "0"

class EquationSolver:
    """Univariate N-degree equation numerical solver (original version, kept for compatibility)"""
    
    def __init__(self, coefficients: List[float]):
        """
        Initialize the equation solver
        
        Args:
            coefficients: List of coefficients from highest to lowest degree
                         Example: [1, 0, -2, 1] represents x^3 - 2x + 1 = 0
        """
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
    
    def f(self, x: float) -> float:
        """Calculate function value f(x)"""
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (self.degree - i))
        return result
    
    def df(self, x: float) -> float:
        """Calculate derivative value f'(x)"""
        result = 0
        for i, coef in enumerate(self.coefficients[:-1]):  # Last term derivative is 0
            power = self.degree - i - 1
            if power >= 0:
                result += coef * (self.degree - i) * (x ** power)
        return result
    
    def bisection_method(self, a: float, b: float, tol: float = 1e-6, max_iter: int = 100) -> Tuple[float, int, bool]:
        """
        Bisection method for solving equations
        
        Args:
            a, b: Interval endpoints
            tol: Precision requirement
            max_iter: Maximum number of iterations
            
        Returns:
            (solution, iteration count, convergence status)
        """
        if self.f(a) * self.f(b) > 0:
            return None, 0, False
        
        for i in range(max_iter):
            c = (a + b) / 2
            if abs(self.f(c)) < tol or abs(b - a) < tol:
                return c, i + 1, True
            
            if self.f(a) * self.f(c) < 0:
                b = c
            else:
                a = c
        
        return (a + b) / 2, max_iter, False
    
    def newton_method(self, x0: float, tol: float = 1e-6, max_iter: int = 100) -> Tuple[float, int, bool]:
        """
        Newton's method for solving equations
        
        Args:
            x0: Initial value
            tol: Precision requirement
            max_iter: Maximum number of iterations
            
        Returns:
            (solution, iteration count, convergence status)
        """
        x = x0
        
        for i in range(max_iter):
            fx = self.f(x)
            if abs(fx) < tol:
                return x, i + 1, True
            
            dfx = self.df(x)
            if abs(dfx) < 1e-10:  # Avoid division by zero
                return x, i + 1, False
            
            x_new = x - fx / dfx
            if abs(x_new - x) < tol:
                return x_new, i + 1, True
            
            x = x_new
        
        return x, max_iter, False
    
    def secant_method(self, x0: float, x1: float, tol: float = 1e-6, max_iter: int = 100) -> Tuple[float, int, bool]:
        """
        Secant method for solving equations
        
        Args:
            x0, x1: Two initial values
            tol: Precision requirement
            max_iter: Maximum number of iterations
            
        Returns:
            (solution, iteration count, convergence status)
        """
        for i in range(max_iter):
            fx0 = self.f(x0)
            fx1 = self.f(x1)
            
            if abs(fx1) < tol:
                return x1, i + 1, True
            
            if abs(fx1 - fx0) < 1e-10:  # Avoid division by zero
                return x1, i + 1, False
            
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            
            if abs(x2 - x1) < tol:
                return x2, i + 1, True
            
            x0, x1 = x1, x2
        
        return x1, max_iter, False
    
    def find_all_roots(self, x_range: Tuple[float, float], step: float = 0.1, tol: float = 1e-6) -> List[float]:
        """
        Find all roots in the specified range
        
        Args:
            x_range: Search range (min_x, max_x)
            step: Search step size
            tol: Precision requirement
            
        Returns:
            All found roots
        """
        roots = []
        min_x, max_x = x_range
        
        # Use bisection method for search
        x = min_x
        while x < max_x:
            if abs(self.f(x)) < tol:
                # Check if this root has already been found
                if not any(abs(x - root) < tol for root in roots):
                    roots.append(x)
            elif self.f(x) * self.f(x + step) < 0:
                root, _, converged = self.bisection_method(x, x + step, tol)
                if converged and not any(abs(root - r) < tol for r in roots):
                    roots.append(root)
            x += step
        
        return sorted(roots)
    
    def plot_function(self, x_range: Tuple[float, float], roots: List[float] = None):
        """
        Plot function graph
        
        Args:
            x_range: x-axis range
            roots: Roots to mark
        """
        x = np.linspace(x_range[0], x_range[1], 1000)
        y = [self.f(xi) for xi in x]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', label=f'f(x) = {self._get_equation_string()}')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        if roots:
            for root in roots:
                plt.plot(root, 0, 'ro', markersize=8, label=f'Root: x = {root:.6f}')
        
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Function Graph')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def _get_equation_string(self) -> str:
        """Get string representation of the equation"""
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            
            power = self.degree - i
            if power == 0:
                term = f"{coef}"
            elif power == 1:
                term = f"{coef}x" if coef != 1 else "x"
            else:
                term = f"{coef}x^{power}" if coef != 1 else f"x^{power}"
            
            if i > 0 and coef > 0:
                term = "+ " + term
            
            terms.append(term)
        
        return " ".join(terms) if terms else "0"

def main():
    """Main function"""
    print("=== Univariate N-degree Equation Numerical Solver (Enhanced Version) ===")
    print()
    
    print("Enter equation coefficients from highest to lowest degree")
    print("Example: x^3 - 2x + 1 = 0, enter: 1 0 -2 1")
    print("Example: x^2 - 4 = 0, enter: 1 0 -4")
    print("Example: x^3 + 1 = 0, enter: 1 0 0 1")
    print()
    
    try:
        coeff_str = input("Enter coefficients: ").strip()
        coefficients = [float(x) for x in coeff_str.split()]
        
        if not coefficients:
            print("No coefficients entered, using default: x^3 - 2x + 1 = 0")
            coefficients = [1, 0, -2, 1]
    except ValueError:
        print("Invalid input, using default: x^3 - 2x + 1 = 0")
        coefficients = [1, 0, -2, 1]
    
    # Create solver
    solver = ComplexEquationSolver(coefficients)
    print(f"\nEquation: {solver._get_equation_string()} = 0")
    print(f"Degree: {solver.degree}")
    
    # Use Aberth+Newton method to solve all roots
    print("\nSolving all roots using Aberth+Newton method...")
    roots = solver.solve_all_roots()
    
    if roots:
        print(f"Found {len(roots)} roots:")
        for i, root in enumerate(roots, 1):
            if abs(root.imag) < 1e-10:
                print(f"Root {i}: x = {root.real:.8f} (real root)")
            else:
                print(f"Root {i}: x = {root.real:.8f} + {root.imag:.8f}i (complex root)")
            print(f"Verification: f({root:.8f}) = {solver.f(root):.2e}")
    else:
        print("No roots found")
    
    # Plot complex root distribution
    print("\nPlotting root distribution...")
    solver.plot_complex_roots(roots)
    
    print("\nProgram finished")

if __name__ == "__main__":
    main()
