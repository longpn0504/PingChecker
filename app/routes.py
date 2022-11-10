from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import RequestPing


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = RequestPing()
    if form.validate_on_submit():
        region = form.rigions.data
        print(region)
        
    return render_template('base.html', form = form)

