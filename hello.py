from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello():
    return 'Hello, Ahsan'

@app.route('/user/<name>')
def user(name):
    stuff='I am <strong>PHP Developer</strong>'
    #return '<h1>Hello {}</h1>'.format(name)
    return render_template("index.html" , name=name,stuff=stuff)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
#internal server error 
@app.errorhandler(500)
def server_not_found(e):
    return render_template("500.html"),500
