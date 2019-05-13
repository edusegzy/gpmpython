
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/divide_form')
def divide_form():
    return render_template('divide_form.jinja2')

@app.route('/divide_result', methods=['POST'])
def divide_result():
    number = float(request.form['number'])
    divide_by = float(request.form['divide_by'])
    return render_template('divide_result.jinja2', result=(number*0.453592)/(divide_by*0.3048)**2)


if __name__ == '__main__':
    app.debug = True
    app.run()
