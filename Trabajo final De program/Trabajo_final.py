from flask import Flask, render_template
from database_db import get_universe_characters

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Trabajo_fin.html')

@app.route('/universo/<int:number>')
def universo(number):
    characters = get_universe_characters(number)
    return render_template(
        'universo.html',
        universe_number=number,
        characters=characters
    )


@app.route('/universo_11')
def universo_11():
    return render_template('universo_11.html')

@app.route('/universo_2')
def universo_2():
    return render_template('universo_2.html')

@app.route('/universo_3')
def universo_3():
    return render_template('universo_3.html')

@app.route('/universo_4')
def universo_4():
    return render_template('universo_4.html')

@app.route('/universo_6')
def universo_6():
    return render_template('universo_6.html')

@app.route('/universo_7')
def universo_7():
    return render_template('universo_7.html')

@app.route('/universo_9')
def universo_9():
    return render_template('universo_9.html')

@app.route('/universo_10')
def universo_10():
    return render_template('universo_10.html')

if __name__ == '__main__':
    app.run(debug=True)
