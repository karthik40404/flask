from flask import Flask, render_template ,request,redirect,url_for
app = Flask(__name__)
import sqlite3
data =[]
@app.route('/')
def f1():
    return 'welcome'

@app.route('/f2')
def f2():
    return 'welcome all'

@app.route('/ind', methods=['POST', 'GET'])
def fun4():
    con = sqlite3.connect('database.db') 
    try:
        con.execute("create table user(name text, age int)")
    except:
        pass   
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if name and age:
            data.append({"name": name, "age": age})
        con.execute("INSERT INTO user(age,name) VALUES (?, ?)", (int(age), name))
        con.commit()
        con.close()      
        return redirect(url_for('fun4'))
    else:
        con.close()
        return render_template('index1.html',data=data)

@app.route('/p')
def f4():
    return render_template('index.html')


app.run()