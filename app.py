from flask import Flask, render_template, request, jsonify
import numpy as np
import plotly.graph_objects as go
import plotly.utils
import json
import random
import time
import math
from typing import List, Tuple, Union

app = Flask(__name__)

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
    
    def aberth_method(self, z: List[complex], max_iter: int = 50, tol: float = 1e-10) -> List[complex]:
        """Aberth iteration method for solving all roots of polynomial equations"""
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
        """Use Newton's method to refine roots"""
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
        """Use Aberth+Newton method to solve all roots"""
        return self.solve_all_roots_custom(range_val, aberth_iter, newton_iter, 1e-6, 1e-6)
    
    def solve_all_roots_custom(self, range_val: float = 10.0, aberth_iter: int = 100, newton_iter: int = 30, 
                              err6: float = 1e-6, err: float = 1e-6, zero_threshold: float = 1e-10) -> List[complex]:
        """Use Aberth+Newton method to solve all roots with custom parameters"""
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
            
            # Add new roots to the collection (check for duplicates)
            for root in z:
                is_duplicate = False
                for existing_root in all_roots:
                    if abs(root - existing_root) < err:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    all_roots.append(root)
        
        # Additional search for roots near the origin if we haven't found enough roots
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
                    
                    if abs(df_val) < err6:
                        break
                    
                    x_new = x - f_val / df_val
                    
                    if abs(x_new - x) < err6:
                        x = x_new
                        break
                    
                    x = x_new
                
                # Check if this is a new root
                is_duplicate = False
                for existing_root in all_roots:
                    if abs(x - existing_root) < err:
                        is_duplicate = True
                        break
                if not is_duplicate and abs(self.f(x)) < err6:
                    all_roots.append(x)
        
        # Now process the roots to detect multiplicity
        return self._process_roots_with_multiplicity(all_roots, err, zero_threshold)
    
    def _process_roots_with_multiplicity(self, roots: List[complex], tolerance: float, zero_threshold: float = 1e-8) -> List[complex]:
        """Process roots to detect and handle multiplicity - return n roots (including multiplicities)"""
        if not roots:
            return []
        
        # Clean roots: set real/imaginary parts to 0 if they're close to 0
        cleaned_roots = []
        for root in roots:
            real_part = root.real if abs(root.real) > zero_threshold else 0.0
            imag_part = root.imag if abs(root.imag) > zero_threshold else 0.0
            cleaned_roots.append(complex(real_part, imag_part))
        
        # Sort roots by real part (ascending), then by imaginary part (ascending)
        cleaned_roots.sort(key=lambda x: (x.real, x.imag))
        
        # Group roots by proximity and calculate multiplicity
        processed_roots = []
        i = 0
        
        while i < len(cleaned_roots):
            current_root = cleaned_roots[i]
            multiplicity = 1
            
            # Count how many roots are close to the current root
            j = i + 1
            while j < len(cleaned_roots) and abs(cleaned_roots[j] - current_root) < tolerance:
                multiplicity += 1
                j += 1
            
            # Add the root with its multiplicity (repeat the root based on multiplicity)
            for _ in range(multiplicity):
                processed_roots.append(current_root)
            
            i = j
        
        # Ensure we have exactly n roots (where n is the degree of the polynomial)
        # If we have fewer roots, add the most common root to reach n roots
        while len(processed_roots) < self.degree:
            if processed_roots:
                # Add the most common root (first one after sorting)
                processed_roots.append(processed_roots[0])
            else:
                # If no roots found, add zeros
                processed_roots.append(complex(0, 0))
        
        # If we have more than n roots, take the first n
        if len(processed_roots) > self.degree:
            processed_roots = processed_roots[:self.degree]
        
        return processed_roots
    
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

def create_plots(coefficients, roots):
    """Create interactive plots using Plotly"""
    solver = ComplexEquationSolver(coefficients)
    
    # Auto-adjust range to include all roots
    if roots:
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
        x_range = (-3, 3)
        y_range = (-3, 3)
    
    # Create function plot (real part)
    x = np.linspace(x_range[0], x_range[1], 1000)
    y_real = [solver.f(complex(xi, 0)).real for xi in x]
    
    # Function plot
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=x, y=y_real,
        mode='lines',
        name='f(x)',
        line=dict(color='#2E86AB', width=3)
    ))
    
    # Add zero line
    fig1.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig1.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    # Mark real roots
    real_roots = [root for root in roots if abs(root.imag) < 1e-10]
    if real_roots:
        fig1.add_trace(go.Scatter(
            x=[root.real for root in real_roots],
            y=[0] * len(real_roots),
            mode='markers',
            name='Real Roots',
            marker=dict(color='#D62828', size=12, line=dict(color='white', width=2))
        ))
    
    fig1.update_layout(
        title="Function Graph (Real Part)",
        xaxis_title="x",
        yaxis_title="f(x)",
        showlegend=False,
        plot_bgcolor='white',
        width=600,
        height=400
    )
    
    # Complex plane plot
    fig2 = go.Figure()
    
    # Add coordinate axes
    fig2.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig2.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    if roots:
        # Separate real and complex roots
        real_roots = [root for root in roots if abs(root.imag) < 1e-10]
        complex_roots = [root for root in roots if abs(root.imag) >= 1e-10]
        
        # Plot real roots
        if real_roots:
            fig2.add_trace(go.Scatter(
                x=[root.real for root in real_roots],
                y=[root.imag for root in real_roots],
                mode='markers+text',
                name='Real Roots',
                text=[f'x = {root.real:.6f}' for root in real_roots],
                textposition="top center",
                marker=dict(color='#D62828', size=15, line=dict(color='white', width=2)),
                textfont=dict(color='#D62828', size=10)
            ))
        
        # Plot complex roots
        if complex_roots:
            complex_labels = []
            for root in complex_roots:
                if root.imag > 0:
                    label = f'x = {root.real:.6f} + {root.imag:.6f}i'
                else:
                    label = f'x = {root.real:.6f} - {abs(root.imag):.6f}i'
                complex_labels.append(label)
            
            fig2.add_trace(go.Scatter(
                x=[root.real for root in complex_roots],
                y=[root.imag for root in complex_roots],
                mode='markers+text',
                name='Complex Roots',
                text=complex_labels,
                textposition="top center",
                marker=dict(color='#2E86AB', size=12, line=dict(color='#1B4965', width=2)),
                textfont=dict(color='#2E86AB', size=10)
            ))
    
    fig2.update_layout(
        title="Root Distribution in Complex Plane",
        xaxis_title="Real Part",
        yaxis_title="Imaginary Part",
        showlegend=False,
        plot_bgcolor='white',
        width=600,
        height=400
    )
    
    # Set equal aspect ratio
    fig2.update_xaxes(range=x_range)
    fig2.update_yaxes(range=y_range)
    
    return fig1, fig2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        coefficients_str = data.get('coefficients', '')
        params = data.get('params', {})
        
        # Parse coefficients
        coefficients = [float(x.strip()) for x in coefficients_str.split() if x.strip()]
        
        if not coefficients:
            return jsonify({'error': 'No coefficients provided'})
        
        # Get algorithm parameters (with defaults)
        err6 = float(params.get('err6', 1e-6))
        err = float(params.get('err', 5e-2))
        aberth_iter = int(params.get('aberth', 1200))
        chongshumax = int(params.get('chongshumax', 30000))
        print_precision = int(params.get('printprecision', 9))
        range_val = float(params.get('range', 150))
        zero_threshold = float(params.get('zero_threshold', 1e-8))
        
        # Create solver and find roots with custom parameters
        solver = ComplexEquationSolver(coefficients)
        roots = solver.solve_all_roots_custom(
            range_val=range_val,
            aberth_iter=aberth_iter,
            newton_iter=50,
            err6=err6,
            err=err,
            zero_threshold=zero_threshold
        )
        
        # Prepare results
        results = []
        for i, root in enumerate(roots, 1):
            if abs(root.imag) < 1e-10:
                root_type = 'real'
                value = f"{root.real:.8f}"
            else:
                root_type = 'complex'
                if root.imag > 0:
                    value = f"{root.real:.8f} + {root.imag:.8f}i"
                else:
                    value = f"{root.real:.8f} - {abs(root.imag):.8f}i"
            
            verification = solver.f(root)
            results.append({
                'index': i,
                'type': root_type,
                'value': value,
                'verification': f"{verification.real:.2e} + {verification.imag:.2e}i"
            })
        
        # Create plots
        fig1, fig2 = create_plots(coefficients, roots)
        
        return jsonify({
            'success': True,
            'equation': solver._get_equation_string(),
            'degree': solver.degree,
            'roots': results,
            'plot1': json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder),
            'plot2': json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 