from flask import Flask, jsonify
import requests
app = Flask(__name__)
orders = {
    1: {"order_id": 101, "user_id": 1, "amount": 250},
    2: {"order_id": 102, "user_id": 2, "amount": 300},
    3: {"order_id": 103, "user_id": 3, "amount": 1000},
    4: {"order_id": 104, "user_id": 4, "amount": 1500},
    5: {"order_id": 105, "user_id": 5, "amount": 150}
}
USER_SERVICE_URL = "http://localhost:5001/users"
@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        user_response = requests.get(f"{USER_SERVICE_URL}/{order['user_id']}")
        
        if user_response.status_code == 200:
            order["user"] = user_response.json()
        else:
            order["user"] = "User not found"
            
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404
if __name__ == "__main__":
    app.run(port=5007)

