from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = 'b\xcc1\xc1\xd3\xccA\xfa\xe3X\xde\x08\x06\xdc\xde\xdf\x80'

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

