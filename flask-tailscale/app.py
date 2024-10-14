from flask import Flask, jsonify, render_template
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML UI

@app.route('/start-tailscale', methods=['POST'])
def start_tailscale():
    try:
        # Start Tailscale process
        result = subprocess.Popen(['tailscale', 'up'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = result.communicate()
        if stderr:
            return jsonify({"error": stderr}), 500
        return jsonify({"message": "Tailscale started! Complete authentication in the browser.", "output": stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
