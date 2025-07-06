from flask import Flask, request, jsonify

app = Flask(__name__)

campaigns = []

@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    return jsonify(campaigns)

@app.route('/campaigns', methods=['POST'])
def add_campaign():
    data = request.get_json()
    campaign = {
        "id": len(campaigns) + 1,
        "name": data.get("name"),
        "date": data.get("date")
    }
    campaigns.append(campaign)
    return jsonify({"message": "Campaign added", "campaign": campaign}), 201

if __name__ == '__main__':
    app.run(host ="0.0.0.0", port=5001)
  
