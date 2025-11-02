from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    strength = "Weak"
    color_class = "text-red-600"
    if score >= 5:
        strength = "Strong"
        color_class = "text-green-600"
    elif score >= 3:
        strength = "Medium"
        color_class = "text-yellow-600"
    
    return {
        "strength": strength,
        "color_class": color_class,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "min_length": length >= 8
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form.get('password')
        result = check_password_strength(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)