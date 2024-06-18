from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
river_data = {
    'min_level': 1.5,  # minimum water level in meters
    'max_level': 5.0,  # maximum water level in meters
    'current_level': 3.2  # current water level in meters
}

@app.route('/api/river-level', methods=['GET'])
def get_river_level():
    return jsonify(river_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
