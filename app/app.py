# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class users(db.Model):
    name = db.Column(db.String(20), nullable = False, primary_key= True)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer, default='N/A')
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'users: ' + self.name 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        post_name = request.form['name']
        post_email = request.form['email']
        post_phone = request.form['phone']
        post_age = request.form['age']
        new_post = users(name= post_name, email= post_email, phone=post_phone, age = post_age)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/form')
    else:
        all_posts = users.query.all()
        return render_template("form.html",users = all_posts) 

@app.route('/form/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    post = users.query.get_or_404(name)
    db.session.delete(post)
    db.session.commit()
    return redirect('/form')

@app.route('/form/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    
    post = users.query.get_or_404(name)
    if request.method == 'POST':
        post.name = request.form['name']
        post.email = request.form['email']
        post.phone = request.form['phone']
        post.age = request.form['age']
        db.session.commit()
        return redirect('/form')
    else:
        return render_template('update.html', post=post)
if __name__ == '__main__':
    app.run(host = '0.0.0.0') 
