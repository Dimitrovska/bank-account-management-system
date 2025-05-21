from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Loan calculator API running. Use /calculate-interest with parameters principal, loan_type, years."


INTEREST_RATES = {
    "mortgage": 4.5,     # Ипотечен кредит
    "consumer": 8.0,     # Потребителски кредит
    "car": 6.5,          # Автокредит
    "credit_card": 15.0  # Кредитна карта
}

def calculate_interest(principal, rate, years):
    # проста лихва = P * R * T / 100
    return (principal * rate * years) / 100


#@app.route(...) е декоратор в Flask, който казва на приложението:
"""„Тази функция ще отговаря на HTTP заявки, идващи на пътя /calculate-interest."""

@app.route('/calculate-interest', methods=['GET'])
def interest():
    principal = float(request.args.get('principal', 0))
    loan_type = request.args.get('loan_type', '').lower()
    years = float(request.args.get('years', 0))

    print(f"principal={principal}, loan_type={loan_type}, years={years}")

    if loan_type not in INTEREST_RATES:
        return jsonify({"error": "Invalid loan type"}), 400

    rate = INTEREST_RATES[loan_type]
    interest_value = calculate_interest(principal, rate, years)

    return jsonify({
        "principal": principal,
        "loan_type": loan_type,
        "years": years,
        "rate": rate,
        "interest": interest_value
    })

if __name__ == '__main__':
    app.run(debug=True)

# Тестваме в бразуер дали работи
#http://127.0.0.1:5000/calculate-interest?principal=10000&loan_type=mortgage&years=5
#http://127.0.0.1:5000/calculate-interest?principal=150000&loan_type=consumer&years=24
