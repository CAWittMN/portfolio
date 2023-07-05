from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField("Name")
    email = EmailField("Email")
    message = TextAreaField("Message")