
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>CCA2 Student App</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 80px;">
            <h1>Welcome to CCA 2 CI/CD Project!</h1>
            <p>Student Information Application</p>
            <p>Deployed using Docker, Jenkins and Kubernetes.</p>
        </body>
    </html>
    """

@app.route("/student")
def student():
    return jsonify({
        "name": "Student",
        "course": "CSE",
        "subject": "Cloud Computing and DevOps",
        "version": "v1"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
