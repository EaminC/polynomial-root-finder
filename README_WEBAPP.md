# 🌐 Polynomial Root Finder Web Application

A beautiful, interactive web application for solving polynomial equations with complex root support. Built with Flask, Plotly, and modern web technologies.

## ✨ Features

### 🎯 **Core Functionality**

- **Advanced Algorithm**: Aberth iteration + Newton refinement
- **Complex Root Support**: Find all real and complex roots
- **High Precision**: 8-digit accuracy with verification
- **Multiple Strategies**: 5 different initialization methods
- **Arbitrary Degree Support**: Handle polynomials from degree 1 to 50

### 🎨 **Beautiful Interface**

- **Modern Design**: Gradient backgrounds, smooth animations
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects, loading animations
- **Professional UI**: Clean cards, icons, and typography

### 📊 **Visualization**

- **Real-time Plotting**: Interactive charts with Plotly
- **Dual Views**: Function graph + Complex plane
- **Smart Scaling**: Auto-adjusts to show all roots
- **Color Coding**: Red for real roots, blue for complex

### 🚀 **User Experience**

- **Quick Examples**: One-click preset equations
- **Instant Results**: Real-time calculation and display
- **Error Handling**: Clear error messages and validation
- **Keyboard Support**: Enter key to solve

## 🛠️ Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Web Application

```bash
# Option 1: Use the launcher script (recommended)
python run_webapp.py

# Option 2: Run directly with Flask
python app.py
```

### 3. Access the Application

Open your browser and go to: **http://localhost:5000**

## 🎮 How to Use

### 📝 **Input Format**

Enter coefficients from highest to lowest degree:

- `1 0 -2 1` → x³ - 2x + 1 = 0
- `1 0 -4` → x² - 4 = 0
- `1 0 0 1` → x³ + 1 = 0

### 🎯 **Quick Examples**

Click any example to auto-fill the input:

- **x³ - 2x + 1 = 0** (3 real roots)
- **x² - 4 = 0** (2 real roots)
- **x³ + 1 = 0** (1 real + 2 complex roots)
- **x⁴ - 5x² + 4 = 0** (4 real roots)

### 📊 **Results Display**

- **Equation Info**: Degree and root count
- **Root Cards**: Individual cards for each root
- **Verification**: f(root) values to confirm accuracy
- **Interactive Plots**: Zoom, pan, and hover for details

## 🏗️ Architecture

### **Backend (Flask)**

```
app.py
├── ComplexEquationSolver class
│   ├── Aberth iteration method
│   ├── Newton refinement
│   └── Multiple search strategies
├── Plotly visualization
└── RESTful API endpoints
```

### **Frontend (HTML/CSS/JavaScript)**

```
templates/index.html
├── Modern responsive design
├── Interactive UI components
├── Plotly.js integration
└── AJAX communication
```

### **Key Technologies**

- **Flask**: Web framework
- **Plotly**: Interactive plotting
- **NumPy**: Numerical computations
- **Font Awesome**: Icons
- **CSS Grid/Flexbox**: Layout

## 🎨 Design Features

### **Color Scheme**

- **Primary**: Purple gradient (#667eea → #764ba2)
- **Real Roots**: Red (#dc3545)
- **Complex Roots**: Blue (#2E86AB)
- **Background**: White with subtle shadows

### **Interactive Elements**

- **Hover Effects**: Cards lift and glow
- **Loading Animation**: Spinning icon during calculation
- **Smooth Transitions**: All animations are CSS-based
- **Responsive Grid**: Adapts to screen size

### **Typography**

- **Font**: Segoe UI (modern, readable)
- **Hierarchy**: Clear heading structure
- **Monospace**: For numerical values
- **Icons**: Font Awesome for visual cues

## 🔧 Customization

### **Adding New Examples**

Edit `templates/index.html`:

```html
<div class="example-item" onclick="setExample('1 0 -3 2')">
  <div class="equation">x³ - 3x + 2 = 0</div>
  <div class="coefficients">1 0 -3 2</div>
</div>
```

### **Modifying Colors**

Edit CSS variables in the style section:

```css
:root {
  --primary-color: #667eea;
  --secondary-color: #764ba2;
  --real-root-color: #dc3545;
  --complex-root-color: #2e86ab;
}
```

### **Adding New Plot Types**

Extend the `create_plots()` function in `app.py`:

```python
def create_plots(coefficients, roots):
    # Existing plots...

    # Add new plot type
    fig3 = go.Figure()
    # ... plot configuration
    return fig1, fig2, fig3
```

## 🚀 Performance

### **Optimizations**

- **Efficient Algorithms**: O(n²) Aberth iteration
- **Smart Initialization**: Multiple strategies for better convergence
- **Lazy Loading**: Plots render only when needed
- **Minimal Dependencies**: Lightweight web stack

### **Scalability**

- **Stateless Design**: No server-side state
- **RESTful API**: Clean separation of concerns
- **CDN Resources**: External libraries loaded from CDN
- **Mobile Optimized**: Responsive design for all devices

## 🐛 Troubleshooting

### **Common Issues**

1. **Port Already in Use**

   ```bash
   # Change port in app.py
   app.run(port=5001)
   ```

2. **Plotly Not Loading**

   - Check internet connection (CDN required)
   - Try different browser
   - Check browser console for errors

3. **Slow Performance**
   - Reduce polynomial degree
   - Check system resources
   - Close other applications

### **Debug Mode**

```bash
# Enable debug mode
export FLASK_ENV=development
python app.py
```

## 📱 Mobile Support

The web app is fully responsive and works on:

- **iOS Safari**: iPhone and iPad
- **Android Chrome**: All Android devices
- **Desktop Browsers**: Chrome, Firefox, Safari, Edge

## 🔮 Future Enhancements

### **Planned Features**

- [ ] **Symbolic Input**: LaTeX equation input
- [ ] **Root History**: Save and compare results
- [ ] **Export Options**: PNG, PDF, CSV export
- [ ] **Advanced Plots**: 3D visualization
- [ ] **User Accounts**: Save favorite equations

### **Technical Improvements**

- [ ] **WebAssembly**: Faster computation
- [ ] **Service Worker**: Offline support
- [ ] **Progressive Web App**: Install as native app
- [ ] **Real-time Collaboration**: Share results

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

**Enjoy solving polynomial equations with style! 🎉**
