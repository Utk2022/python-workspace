from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Set your API key from ExchangeRate-API
API_KEY = "9f2caf0e2a57e5e7d3b8a214"  # Replace with your actual API key from ExchangeRate-API

# API URL for ExchangeRate-API (or another service of your choice)
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

@app.route('/', methods=['GET', 'POST'])
def index():
    exchange_rates = None
    conversion_result = None

    if request.method == 'POST':
        # Get the currency and amount input by the user
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        # Get exchange rates from the API
        response = requests.get(API_URL)
        data = response.json()

        if data['result'] == 'success':
            from_rate = data['conversion_rates'].get(from_currency)
            to_rate = data['conversion_rates'].get(to_currency)

            if from_rate and to_rate:
                # Convert from "from_currency" to USD, then from USD to "to_currency"
                usd_amount = amount / from_rate
                conversion_result = round(usd_amount * to_rate, 2)
            else:
                conversion_result = "Invalid currency selected"
        else:
            conversion_result = "Failed to fetch exchange rates"

    return render_template('index.html', exchange_rates=exchange_rates, conversion_result=conversion_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
