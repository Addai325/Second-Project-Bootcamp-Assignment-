#Name: Ransford Addai
#Training ID: 32524
#Week Two(2) Python Programming Project


from flask import Flask, render_template_string, request

app = Flask(__name__)

# Predefined exchange rates
exchange_rates = {
    'USD': 0.0014,
    'EUR': 0.0013,
    'GBP': 0.0011,
}

# HTML template containing the web page structure and styles
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS styles for the user interface -->
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        h1 {
            text-align: center;
        }
        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.2);
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        p {
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
    <title>Currency Converter</title>
</head>
<body>
    <h1>Currency Converter</h1>
    <form method="POST">
        <!-- Input field for NGN amount -->
        <label for="ngn_amount">Enter NGN Amount:</label>
        <input type="number" name="ngn_amount" id="ngn_amount" required>
        <!-- Dropdown for selecting target currency -->
        <label for="target_currency">Select Target Currency:</label>
        <select name="target_currency" id="target_currency">
            <option value="USD">USD</option>
            <option value="EUR">EUR</option>
            <option value="GBP">GBP</option>
        </select>
        <!-- Submit button -->
        <button type="submit">Convert</button>
    </form>
    <!-- Display converted amount if available -->
    {% if converted_amount is not none %}
        <p>Converted Amount: {{ converted_amount }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ngn_amount = float(request.form['ngn_amount'])
        target_currency = request.form['target_currency']
        converted_amount = ngn_amount * exchange_rates[target_currency]
        return render_template_string(html_template, converted_amount=converted_amount)

    # Render the HTML template with no converted amount initially
    return render_template_string(html_template, converted_amount=None)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
