from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my home page and welcome page"

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/pass/<int:score>')
def Pass(score):
    return "Person has passed and scored " + str(score)

@app.route('/fail/<int:score>')
def Fail(score):
    return "Person has failed and scored " + str(score)

@app.route('/result/<int:score>')
def results(score):
    result = "Pass" if score >= 50 else "Fail"
    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)
