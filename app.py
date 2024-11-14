from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_prices

app = Flask(__name__)
CORS(app)

@app.route('/get-prices', methods=['POST'])
def get_prices_route():
    data = request.get_json()
    product_name = data.get("product_name")
    if not product_name:
        return jsonify({"error": "Product name required"}), 400

    result = get_prices(product_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
