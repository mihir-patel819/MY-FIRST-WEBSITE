from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello Mihir!</h1>
    <h2>Welcome to My DevOps Project</h2>
    <p>Application Status: Running</p>
    <p>Version: 1.0</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
