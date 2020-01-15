from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class ProgrammingForm(FlaskForm):
    programField = StringField(u'Enter your program here...')
    submit = SubmitField(u'Submit')