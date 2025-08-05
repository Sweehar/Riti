
from flask import Flask, render_template, request, jsonify,url_for,redirect

app = Flask(__name__)

numbers = []


@app.route('/')
def hi():
    return redirect(url_for('home'))
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = request.form.get('number')
        if number and number.isdigit():
            numbers.append(int(number))
    return render_template('home.html', numbers=numbers)

@app.route('/data', methods=['GET'])
def data():
    return jsonify({'value': numbers})

if __name__ == '__main__':
    app.run(debug=True)

