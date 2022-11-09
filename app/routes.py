from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import RequestPing

@app.route('/')
def index():
    form = RequestPing()

    return render_template('base.html', form = form)

