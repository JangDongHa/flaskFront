from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def getLogin():
    return render_template('login.html');

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)