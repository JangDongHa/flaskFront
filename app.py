from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def getLogin():
    return render_template('login.html')

@app.route('/user')
def getUser():
    return render_template('user.html')

@app.route('/register')
def getRegister():
    return render_template('register.html')

@app.route('/search')
def getSearch():
    return render_template('search.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
