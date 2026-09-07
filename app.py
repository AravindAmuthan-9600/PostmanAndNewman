from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Aravind",
        "role": "DevOps Engineer"
    },
    {
        "id": 2,
        "name": "Kumar",
        "role": "Developer"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "User Management API is running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is healthy"
    }), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "role" not in data:
        return jsonify({
            "error": "name and role are required"
        }), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "role": data["role"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next(
        (user for user in users if user["id"] == user_id),
        None
    )

    if user is None:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify(user), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
