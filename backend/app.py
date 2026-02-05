from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Mal_Tracker backend running successfully 🚀"

@app.route("/health")
def health():
    return {"status": "ok", "service": "Mal_Tracker"}

if __name__ == "__main__":
    app.run(debug=True)
