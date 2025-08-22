# BMI Calculator Flask App

A modern, responsive BMI calculator web application built with Flask backend and HTML/CSS/JavaScript frontend.

## Features

- **Landing Page**: Welcome page with BMI information and categories
- **Calculator Page**: Interactive form with metric/imperial unit conversion
- **Result Page**: Detailed BMI results with health recommendations
- **Responsive Design**: Works on all devices
- **Modern UI**: Gradient backgrounds, smooth animations, and glass-morphism effects

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation & Setup

### 1. Create Project Directory
```bash
mkdir bmi-calculator-app
cd bmi-calculator-app
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Create Project Structure
Create the following folders and files:

```
bmi-calculator-app/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    ├── base.html
    ├── landing.html
    ├── calculator.html
    └── result.html
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create Files
Copy the provided code into respective files:

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `templates/base.html` - Base template with common styles
- `templates/landing.html` - Welcome/landing page
- `templates/calculator.html` - BMI calculator form
- `templates/result.html` - Results display page

### 6. Run the Application
```bash
python app.py
```

The application will start and you'll see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### 7. Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. **Landing Page**: Start at the home page to learn about BMI
2. **Calculator**: Click "Calculate Your BMI" to enter your measurements
3. **Units**: Toggle between Metric (kg, m) and Imperial (lbs, ft) units
4. **Results**: View your BMI score, category, and health recommendations

## File Structure Explanation

- **`app.py`**: Main Flask application with routes and BMI calculation logic
- **`templates/base.html`**: Base template with common HTML structure and CSS
- **`templates/landing.html`**: Home page with BMI information and categories
- **`templates/calculator.html`**: Calculator form with unit conversion
- **`templates/result.html`**: Results page with recommendations

## BMI Categories

- **Underweight**: BMI < 18.5
- **Normal Weight**: BMI 18.5 - 24.9
- **Overweight**: BMI 25 - 29.9
- **Obese**: BMI ≥ 30

## Customization

### Changing Colors
Edit the CSS variables in `base.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adding Features
- Add user authentication
- Store calculation history
- Export results as PDF
- Add more health metrics

## Troubleshooting

### Port Already in Use
If port 5000 is busy, change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Module Not Found
Make sure your virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Template Not Found
Ensure the `templates` folder is in the same directory as `app.py`.

## Development Mode

The app runs in debug mode by default, which means:
- Automatic reloading when code changes
- Detailed error messages
- Not suitable for production

For production deployment, set `debug=False` in `app.py`.

## Security Note

Change the secret key in `app.py` before deploying:
```python
app.secret_key = 'your-random-secret-key-here'
```

## Browser Support

- Chrome/Edge 80+
- Firefox 75+
- Safari 13+
- Mobile browsers (iOS Safari, Chrome Mobile)

Enjoy your BMI calculator app!