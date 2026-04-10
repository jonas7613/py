
from flask import Flask, jsonify
app = Flask(__name__)
users = {
    1: {"name": "Jonathan", "email": "jonathan@gmail.com"},
    2: {"name": "Jonathan Samson", "email": "jonathan@gmail.com"}
}
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
if __name__ == "__main__":
    app.run(port=5007)
