from flask import Flask , render_template , make_response , request , session , redirect
from . import core
from app import app

app.config['SECRET_KEY'] = "f116d0a5491cbe27e7bb07016b694eb4f6a1976e9f9c55621b9c5418567ac02c"

@app.route('/')
def index():
    return render_template('adminlk.html')

app.run(debug=True)