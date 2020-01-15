from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class ProgrammingForm(FlaskForm):
    programField = TextAreaField(u'Enter your program here...', default="public static String StudentAnswer () {\n\t\n}")
    submit = SubmitField(u'Submit')