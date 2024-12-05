from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def f1():
    return 'welcome'

@app.route('/f2')
def f2():
    return 'welcome all'

@app.route('/index')
def f3():
    return render_template('index1.html')

@app.route('/p')
def f4():
    return render_template('index.html')


app.run()