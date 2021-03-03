from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def weclome_func():
    return '<html> <body> <h1> Welcome </h1> </body> </html>'

@app.route('/welcome/home')
def weclome_home_func():
    return '<html> <body> <h1> Welcome Home </h1> </body> </html>'

@app.route('/welcome/back')
def weclome_back_func():
    return '<html> <body> <h1> Welcome Back </h1> </body> </html>'