from flask import Flask, request, jsonify

app = Flask(__name__)

registrations = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    registration = {
        "user": data.get("user"),
        "campaign_id": data.get("campaign_id")
    }
    registrations.append(registration)
    return jsonify({"message": "User registered for campaign", "registration": registration}), 201

@app.route('/registrations', methods=['GET'])
def get_registrations():
    return jsonify(registrations)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
  
