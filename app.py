from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# instantiate database object
db = SQLAlchemy(app)

# pass .Model to db object in the class user. This will map them model to the database table
# db types given as attributes to columns


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route('/')
def home():
    return '<h1> Welcome to the users app. </h1> <br> <h2> Use the following routes: </h2> <br> <ul> <li>To add new users:  localhost:5000/<name>/<location><br>(replace the variables name and location with the information you want to add without using the angle brackets) </li><li> To delete users:  localhost:5000/delete/<location></li><li> To see single user: localhost:5000/<name></li><li> To see list of users:  localhost:5000/users </li> </ul>'

# create new object using the url below (change the variables in the url and add new ones in the url itself to create)


@app.route('/<name>/<location>')
def index(name, location):
    user = User(name=name, location=location)
    # insert new user with this
    db.session.add(user)
    # save new user with this
    db.session.commit()
    # html ack
    return '<h1> Added new user!</h1>'

# get a single user


@app.route('/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()

    return f'<h1>User { user.name } is located at { user.location }.</h1>'

# get multiple users


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template("users.html", users=users)

# delete a user using location  (can use name or id instead, just change the variable in the url, pass it to the function and to the filter)


@app.route('/delete/<location>')
def delete_user(location):
    user = User.query.filter_by(location=location).first()
    db.session.delete(user)
    db.session.commit()
    return '<h1>User deleted!</h1>'
