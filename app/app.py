from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Cloud Platform is running",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0"
    })

@app.route("/info")
def info():
    return jsonify({
        "application": "DevOps Cloud Platform",
        "environment": "development",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
