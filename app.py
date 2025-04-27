from flask import Flask, request, jsonify
from red_team import red_team_attack
from blue_team import blue_team_defend

app = Flask(__name__)

@app.route('/red_attack', methods=['POST'])
@app.route('/red_attack', methods=['POST'])
def red_attack():
    data = request.get_json()
    system_info = data.get('system_info', '')
    print(f"Received Red Team Data: {system_info}")  # Gelen veriyi kontrol et
    result = red_team_attack(system_info)
    print(f"Red Team Response: {result}")  # Red Team'in yanıtını kontrol et
    return jsonify({"red_team_result": result})

@app.route('/blue_defend', methods=['POST'])
def blue_defend():
    data = request.get_json()
    vulnerabilities = data.get('vulnerabilities', '')
    print(f"Received Blue Team Data: {vulnerabilities}")  # Gelen veriyi kontrol et
    result = blue_team_defend(vulnerabilities)
    print(f"Blue Team Response: {result}")  # Blue Team'in yanıtını kontrol et
    return jsonify({"blue_team_result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

