from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 Codespace is working! Python is running."

if __name__ == "__main__":
    # host='0.0.0.0' is REQUIRED for Codespaces to forward the port
    app.run(host="0.0.0.0", port=5000)