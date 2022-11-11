from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

class RequestPing(FlaskForm):
    rigions = SelectField('Regions', choices=[(1, 'NA'),(2, 'LAN'),(3, 'EUW'),(4, 'EUNE'),(5,"BR"),(6,"OCE"),(7,"RU")], validators=[DataRequired()])
    submit = SubmitField('Submit')