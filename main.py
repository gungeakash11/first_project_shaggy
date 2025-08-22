from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

def calculate_bmi(weight, height):
    """Calculate BMI and return BMI value and category"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
        color = "#3498db"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "#27ae60"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "#f39c12"
    else:
        category = "Obese"
        color = "#e74c3c"
    
    return round(bmi, 1), category, color

@app.route('/')
def landing():
    """Landing page"""
    return render_template('landing.html')

@app.route('/calculator')
def calculator():
    """Calculator page"""
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Process BMI calculation"""
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        if weight <= 0 or height <= 0:
            return render_template('calculator.html', error="Please enter valid positive numbers")
        
        bmi, category, color = calculate_bmi(weight, height)
        
        # Store results in session
        session['bmi'] = bmi
        session['category'] = category
        session['color'] = color
        session['weight'] = weight
        session['height'] = height
        
        return redirect(url_for('result'))
    
    except ValueError:
        return render_template('calculator.html', error="Please enter valid numbers")

@app.route('/result')
def result():
    """Result page"""
    if 'bmi' not in session:
        return redirect(url_for('calculator'))
    
    return render_template('result.html', 
                         bmi=session['bmi'],
                         category=session['category'],
                         color=session['color'],
                         weight=session['weight'],
                         height=session['height'])

if __name__ == '__main__':
    app.run(debug=True)