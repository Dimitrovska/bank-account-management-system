from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # празна парола
        database="your_database_name"
    )
    return conn

@app.route('/calculate-interest', methods=['GET'])
def calculate_interest():
    principal = float(request.args.get('principal', 0))
    loan_type = request.args.get('loan_type', '').lower()
    years = float(request.args.get('years', 0))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Взимаме лихвения процент от базата за конкретния loan_type
    cursor.execute("SELECT interest_rate FROM loan_types WHERE loan_name = %s", (loan_type,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if not result:
        return jsonify({"error": "Invalid loan type"}), 400

    rate = result['interest_rate']
    interest_value = (principal * rate * years) / 100

    return jsonify({
        "principal": principal,
        "loan_type": loan_type,
        "years": years,
        "rate": rate,
        "interest": interest_value
    })

if __name__ == '__main__':
    app.run(debug=True)

