from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

CAMPAIGN_SERVICE_URL = "http://localhost:5001"
REGISTRATION_SERVICE_URL = "http://localhost:5002"

@app.route('/')
def upcoming_campaigns():
    resp = requests.get(f"{CAMPAIGN_SERVICE_URL}/campaigns")
    campaigns = resp.json()
    return render_template("upcoming.html", campaigns=campaigns)

@app.route('/register-campaign', methods=['GET', 'POST'])
def register_campaign():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        requests.post(f"{CAMPAIGN_SERVICE_URL}/campaigns", json={"name": name, "date": date})
        return redirect(url_for('upcoming_campaigns'))
    return render_template("register_campaign.html")

@app.route('/register-for-campaign', methods=['GET', 'POST'])
def register_for_campaign():
    if request.method == 'POST':
        user = request.form['user']
        campaign_id = int(request.form['campaign_id'])
        requests.post(f"{REGISTRATION_SERVICE_URL}/register", json={"user": user, "campaign_id": campaign_id})
        return redirect(url_for('upcoming_campaigns'))

    resp = requests.get(f"{CAMPAIGN_SERVICE_URL}/campaigns")
    campaigns = resp.json()
    return render_template("register_for_campaign.html", campaigns=campaigns)

if __name__ == '__main__':
    app.run(port=5000)
