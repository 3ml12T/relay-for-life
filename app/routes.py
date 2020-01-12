from flask import render_template
from app import app
from sqlalchemy import desc
from app.models import Event, Message, User
from app.forms import RegistrationForm, LoginForm 


@app.route('/')
@app.route('/home')
def events():
    events = Event.query.order_by(desc(Event.timestamp)).all()
    messages = Message.query.join(User).add_columns(User.id, User.username, Message.text, Message.timestamp).order_by(desc(Message.timestamp)).all()
    return render_template('home.html', events=events, messages=messages)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
