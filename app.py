from flask import Flask, render_template, request, jsonify
import json
import os
from dotenv import load_dotenv

# Laden Sie die Umgebungsvariablen aus der .env-Datei
load_dotenv()

app = Flask(__name__, static_folder='dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top-players', methods=['POST'])
def top_players():
    min_expected_points = int(request.form['min_expected_points'])
    max_market_value = float(request.form['max_market_value'])
    chosen_position = request.form['position']

    with open('data/2024_25_merged_players.json', 'r') as file:
        players_data = json.load(file)

    players_with_ratio = []
    for player in players_data:
        marktwert = player.get("Marktwert")
        expected_points = player.get("Expected_Points_Kicker")
        position = player.get("Position")
        if marktwert and expected_points:
            try:
                marktwert = float(marktwert)
                expected_points = float(expected_points)
                if expected_points >= min_expected_points and marktwert <= max_market_value and position == chosen_position:
                    ratio = expected_points / marktwert * 10000
                    player["Preis_Leistungs_Verhältnis"] = round(ratio, 2)
                    players_with_ratio.append(player)
            except ValueError:
                continue

    players_with_ratio.sort(key=lambda x: x["Preis_Leistungs_Verhältnis"], reverse=True)

    return jsonify(players_with_ratio)

if __name__ == '__main__':
    # Überprüfen Sie die Umgebungsvariable FLASK_ENV
    env = os.getenv('FLASK_ENV', 'production')
    debug = env == 'development'
    app.run(debug=debug)