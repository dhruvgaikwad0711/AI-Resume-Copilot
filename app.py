from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Resume Copilot V1 is running!"

if __name__ == "__main__":
    app.run(debug=True)