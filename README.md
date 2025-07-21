# Polynomial Root Finder

A powerful, interactive web application for solving polynomial equations with complex root support using advanced numerical methods.

![Polynomial Root Finder](https://github.com/EaminC/polynomial-root-finder/raw/main/screenshot.png)

## 🌟 Features

### 🧮 **Advanced Solver**

- **Complex Root Support**: Find both real and complex roots
- **Aberth + Newton Method**: High-precision numerical algorithm
- **Arbitrary Degree**: Support for polynomials up to degree 50
- **Multiple Root Detection**: Handles repeated roots efficiently

### 🎨 **Interactive Interface**

- **Visual Input**: Dynamic coefficient input based on polynomial degree
- **Real-time Preview**: Live equation display as you type
- **Quick Examples**: Pre-defined polynomials for instant testing
- **Random Generation**: Generate random integer coefficients (-10 to 10)
- **One-click Clear**: Reset all coefficients instantly

### 🌙 **Theme Support**

- **Light/Dark Mode**: Toggle between themes with persistent preference
- **Responsive Design**: Works perfectly on desktop and mobile
- **Modern UI**: Beautiful gradients and smooth animations

### ⚙️ **Customizable Parameters**

- **Newton-Raphson Tolerance**: Control iteration precision
- **Complex Distance Tolerance**: Adjust root uniqueness criteria
- **Aberth Iteration Count**: Fine-tune convergence
- **Initial Value Range**: Optimize search space
- **Output Precision**: Set display accuracy

### 📊 **Visualization**

- **Function Graph**: Real-time plotting of polynomial function
- **Complex Plane**: Root distribution visualization
- **Interactive Plots**: Zoom, pan, and hover for details
- **Root Classification**: Clear distinction between real and complex roots

## 🚀 Quick Start

### Prerequisites

```bash
pip install flask plotly numpy
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/EaminC/polynomial-root-finder.git
cd polynomial-root-finder
```

2. Run the application:

```bash
python app.py
```

3. Open your browser and navigate to:

```
http://localhost:5001
```

## 📖 Usage

### Basic Usage

1. **Enter Polynomial Degree**: Type any degree from 1 to 50
2. **Input Coefficients**: Fill in the coefficient fields that appear
3. **Click "Find All Roots"**: Get instant results with visualizations

### Advanced Features

- **Randomize All**: Generate random integer coefficients
- **Clear All**: Reset all inputs quickly
- **Quick Examples**: Try pre-defined polynomials
- **Settings**: Adjust algorithm parameters for optimal results

### Example Polynomials

- **x³ - 2x + 1 = 0**: Three real roots
- **x² - 4 = 0**: Two real roots (±2)
- **x³ + 1 = 0**: One real and two complex roots
- **x⁴ - 5x² + 4 = 0**: Four real roots
- **x⁵ - 1 = 0**: Five complex roots (fifth roots of unity)
- **x⁸ - 1 = 0**: Eight complex roots (eighth roots of unity)

## 🔧 Algorithm Details

### Aberth Method

The Aberth method is an iterative algorithm for finding all roots of a polynomial simultaneously. It's particularly effective for polynomials with complex roots.

### Newton Refinement

After the Aberth method provides initial estimates, Newton's method refines each root to high precision.

### Parameter Tuning

- **err6**: Newton-Raphson iteration tolerance (default: 1e-6)
- **err**: Complex distance tolerance (default: 5e-2)
- **aberth**: Aberth iteration count (default: 1200)
- **range**: Initial value range (default: 150)

## 🎯 Use Cases

### Education

- **Mathematics Classes**: Visualize polynomial behavior
- **Numerical Analysis**: Demonstrate root-finding algorithms
- **Complex Analysis**: Explore complex root patterns

### Research

- **Algorithm Testing**: Validate numerical methods
- **Polynomial Analysis**: Study root distributions
- **Performance Benchmarking**: Test solver efficiency

### Development

- **Mathematical Libraries**: Reference implementation
- **Educational Tools**: Interactive learning platform
- **Scientific Computing**: Quick polynomial analysis

## 🛠️ Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Plotly.js
- **Mathematics**: NumPy
- **Styling**: Custom CSS with gradients and animations

## 📱 Browser Support

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Algorithm**: Based on Aberth's method for polynomial root finding
- **UI Inspiration**: Modern web design principles
- **Mathematical Foundation**: Classical numerical analysis techniques

## 📞 Contact

- **Author**: EaminC
- **GitHub**: [@EaminC](https://github.com/EaminC)
- **Project**: [Polynomial Root Finder](https://github.com/EaminC/polynomial-root-finder)

---

⭐ **Star this repository if you find it useful!**
# polynomial-root-finder
