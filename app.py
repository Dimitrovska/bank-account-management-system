from flask import Flask, request, jsonify
from bank import BankAccount, SavingsAccount

app = Flask(__name__)

# Банкови акаунти
account1 = BankAccount("123456789", 1000)
savings1 = SavingsAccount("987654321", 2000, interest_rate=5)

# API endpoint-и за банката (balance, deposit, withdraw, calculate_interest)
@app.route('/balance/<account_number>', methods=['GET'])
def get_balance(account_number):
    if account_number == account1.account_number:
        return jsonify({"balance": account1.get_balance()})
    elif account_number == savings1.account_number:
        return jsonify({"balance": savings1.get_balance()})
    else:
        return jsonify({"error": "Account not found"}), 404

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    acc_num = data.get("account_number")
    amount = data.get("amount")
    if acc_num == account1.account_number:
        account1.deposit(amount)
        return jsonify({"balance": account1.get_balance()})
    elif acc_num == savings1.account_number:
        savings1.deposit(amount)
        return jsonify({"balance": savings1.get_balance()})
    else:
        return jsonify({"error": "Account not found"}), 404

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    acc_num = data.get("account_number")
    amount = data.get("amount")
    if acc_num == account1.account_number:
        result = account1.withdraw(amount)
        if result == "Insufficient availability":
            return jsonify({"error": result}), 400
        return jsonify({"balance": account1.get_balance()})
    elif acc_num == savings1.account_number:
        result = savings1.withdraw(amount)
        if result == "Insufficient availability":
            return jsonify({"error": result}), 400
        return jsonify({"balance": savings1.get_balance()})
    else:
        return jsonify({"error": "Account not found"}), 404

@app.route('/calculate_interest/<account_number>', methods=['POST'])
def calculate_interest(account_number):
    if account_number == savings1.account_number:
        savings1.calculate_interest()
        return jsonify({"balance": savings1.get_balance()})
    else:
        return jsonify({"error": "Interest can only be calculated for savings accounts"}), 400

# API endpoint за изчисляване на лихва (втори начин)
@app.route('/calculate-interest', methods=['GET'])
def interest():
    principal = float(request.args.get('principal', 0))
    rate = float(request.args.get('rate', 0))
    time = float(request.args.get('time', 0))

    interest_value = (principal * rate * time) / 100

    return jsonify({
        "principal": principal,
        "rate": rate,
        "time": time,
        "interest": interest_value
    })

if __name__ == '__main__':
    app.run(debug=True)
