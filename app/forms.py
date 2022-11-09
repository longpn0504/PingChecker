from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

class RequestPing(FlaskForm):
    rigions = SelectField('Regions', choices=[(1, 'NA'),(2, 'Asia'),(3, 'EU'),(4, 'SA')], validators=[DataRequired()])
    submit = SubmitField('Submit')