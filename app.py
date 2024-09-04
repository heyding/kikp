from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_folder='dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top-players', methods=['POST'])
def top_players():
    min_expected_points = int(request.form['min_expected_points'])
    max_market_value = float(request.form['max_market_value'])
    positions = request.form.getlist('positions')

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
                if expected_points >= min_expected_points and marktwert <= max_market_value and position in positions:
                    ratio = expected_points / marktwert * 10000
                    player["Preis_Leistungs_Verhältnis"] = round(ratio, 2)
                    players_with_ratio.append(player)
            except ValueError:
                continue

    players_with_ratio.sort(key=lambda x: x["Preis_Leistungs_Verhältnis"], reverse=True)
    top_players = players_with_ratio[:100]

    return jsonify(top_players)

if __name__ == '__main__':
    app.run(debug=True)