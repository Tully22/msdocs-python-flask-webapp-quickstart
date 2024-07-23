from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
#importing validators and ValidationError from wtforms gives access to Flask-WTF's built-in validators

class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name."),validators.Length(min=2, max=30)])
  email = TextField("Email",  [validators.Required("Please enter your email address."),validators.Length(min=3, max=35)])
  subject = TextField("Subject",  [validators.Required("Please enter a subject."),validators.Length(min=3, max=25)])
  message = TextAreaField("Message",  [validators.Required("Please enter a message."),validators.Length(min=5, max=150)])
  submit = SubmitField("Send")