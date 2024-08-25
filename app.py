import os
from flask import Flask, request, jsonify

app = Flask(_name_)

USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase = max((char for char in alphabets if char.islower()), default=None)
        
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
