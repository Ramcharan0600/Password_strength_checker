Password Strength Checker

A Real-Time, Interactive Password Validator Built with Flask

1. Project Overview

This is a modern web-based password strength checker that evaluates password security as you type. It uses Flask (Python) for the backend and Tailwind CSS + Vanilla JavaScript for a smooth, responsive frontend.

Key Features

Live validation – no form submission needed

Interactive checkboxes for each password rule

Color-coded strength meter:

Weak → Red

Medium → Yellow

Strong → Green

No page reloads – instant feedback

Clean, mobile-friendly UI

2. Project Structure

Password_strength_checker/
│
├── app.py                  # Flask server + password logic
├── templates/
│   └── index.html          # Frontend UI (HTML + Tailwind + JS)
├── README.md               # This document
└── (Optional) LICENSE      # MIT License file


3. How It Works

Password Rules (Checked in Real Time)

Rule

Requirement

Points

Uppercase Letter

At least one A-Z

+1

Lowercase Letter

At least one a-z

+1

Number

At least one 0-9

+1

Special Character

!@#$%^&*(),.?":{}<>

+1

Minimum Length

≥ 8 characters

+1

Bonus

≥ 12 characters

+1

Final Score → Determines Strength Level

Strength Levels

Score Range

Strength

Color

5–6

Strong

Green

3–4

Medium

Yellow

0–2

Weak

Red

4. Setup & Run Instructions

Step 1: Clone the Repository

git clone [https://github.com/Ramcharan0600/Password_strength_checker.git](https://github.com/Ramcharan0600/Password_strength_checker.git)
cd Password_strength_checker


Step 2: Create Templates Folder

mkdir -p templates


Step 3: Install Dependencies

pip install flask


Step 4: Save Files

Save app.py in the root

Save index.html inside templates/

Step 5: Run the App

python app.py


Step 6: Open in Browser
Go to: http://127.0.0.1:5000

5. File Contents

app.py (Flask Backend)

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
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1
        
    strength = "Weak"
    color_class = "text-red-600"
    if score >= 5:
        strength, color_class = "Strong", "text-green-600"
    elif score >= 3:
        strength, color_class = "Medium", "text-yellow-600"
        
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


templates/index.html (Frontend)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Strength Checker</title>
    <script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h1 class="text-2xl font-bold text-center text-gray-800 mb-6">Password Strength Checker</h1>
        
        <div class="space-y-4">
            <input 
                type="text" 
                id="password" 
                name="password" 
                placeholder="Enter your password" 
                required
                class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                oninput="checkPassword()"
            >
            
            <div id="criteria" class="space-y-2 text-sm text-gray-600">
                <div class="flex items-center">
                    <input type="checkbox" id="upper" disabled class="mr-2">
                    <label for="upper">Contains uppercase letter</label>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="lower" disabled class="mr-2">
                    <label for="lower">Contains lowercase letter</label>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="digit" disabled class="mr-2">
                    <label for="digit">Contains number</label>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="special" disabled class="mr-2">
                    <label for="special">Contains special character</label>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="length" disabled class="mr-2">
                    <label for="length">Minimum 8 characters</label>
                </div>
            </div>
            
            <div id="strength" class="mt-4 text-center">
                <p class="text-lg font-semibold text-gray-600">
                    Password Strength: None
                </p>
            </div>
        </div>
    </div>

    <script>
        function checkPassword() {
            const password = document.getElementById('password').value;
            
            const upper = /[A-Z]/.test(password);
            const lower = /[a-z]/.test(password);
            const digit = /\d/.test(password);
            const special = /[!@#$%^&*(),.?":{}|<>]/.test(password);
            const length = password.length >= 8;

            document.getElementById('upper').checked = upper;
            document.getElementById('lower').checked = lower;
            document.getElementById('digit').checked = digit;
            document.getElementById('special').checked = special;
            document.getElementById('length').checked = length;

            let score = (upper + lower + digit + special + length + (password.length >= 12 ? 1 : 0));
            
            const strengthText = score >= 5 ? 'Strong' : score >= 3 ? 'Medium' : 'Weak';
            const strengthColor = score >= 5 ? 'text-green-600' : score >= 3 ? 'text-yellow-600' : 'text-red-600';

            document.getElementById('strength').innerHTML = 
                `<p class="text-lg font-semibold ${strengthColor}">Password Strength: ${strengthText}</p>`;
        }
    </script>
</body>
</html>


6. Technology Stack

Layer

Technology

Backend

Python, Flask

Frontend

HTML, Tailwind CSS, JavaScript

Hosting

Local (127.0.0.1:5000)

Dependencies

flask only

7. Contributing

Fork the repository

Create a branch: git checkout -b feature/name

Commit: git commit -m "Add feature"

Push: git push origin feature/name

Open a Pull Request

8. License

MIT License – Free to use, modify, and distribute.

9. Author

Ramcharan0600

GitHub: https://github.com/Ramcharan0600

Project Complete. Ready to Deploy or Share.

“Strong passwords start with smart tools.”
