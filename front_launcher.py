import subprocess
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))
FRONTEND = os.path.join(BASE, "frontend")

@app.route("/")
def home():
    return send_from_directory(FRONTEND, "index.html")

@app.route("/dashboard")
def dashboard():
    subprocess.Popen(["python", "dashboard.py"], shell=True)
    return "<h1 style='color:#38BDF8;background:#020617;height:100vh;padding:40px;'>IRANDP Command Center launched.<br>Desktop SOC is opening...</h1>"


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND, path)

if __name__ == "__main__":
    app.run(port=8080)
