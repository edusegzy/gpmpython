
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
    methane_num = float(request.form['methane'])
    ethane_num = float(request.form['ethane'])
    propane_num = float(request.form['propane'])
    ibutane_num = float(request.form['iButane'])
    
    return render_template('divide_result.jinja2', result=(methane_num*1)+ (ethane_num*1) + (propane_num*1)+ (ibutane_num*1)


if __name__ == '__main__':
    app.debug = True
    app.run()
