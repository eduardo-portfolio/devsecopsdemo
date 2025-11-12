from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Python WebAPP "

if __name__ == "__main__":
    # Faz a app escutar em todas as interfaces na porta 5000
    app.run(host='0.0.0.0', port=5000)
