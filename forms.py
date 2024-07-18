from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField 

class Addprofession(FlaskForm):
    name = StringField("პროფესიის სახელი", validators=[DataRequired()])
    image_url = StringField("პროფესიის სურათის ლინკი")
    image = FileField("პროფესიის სურათი")
    text = StringField("დახასიათება")

    submit = SubmitField("Submit")

class Adduniversity(FlaskForm):
    name = StringField("უნივერსიტეტის სახელი", validators=[DataRequired()])
    image_url = StringField("უნივერსიტეტის სურათის ლინკი")
    image = FileField("უნივერსიტეტის სურათი")

    text = StringField("დახასიათება")

    submit = SubmitField("Submit")




class SignUp(FlaskForm):
    username = StringField("Username", validators= [DataRequired(), Length(min=4, max=25)])
    email = StringField("email", validators= [DataRequired()])
    password = PasswordField("password", validators= [DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm password", validators= [DataRequired(), EqualTo("password")])

    submit = SubmitField("submit")

class Login(FlaskForm):
    username = StringField("Username", validators= [DataRequired(), Length(min=4, max=25)])
    password = PasswordField("password", validators= [DataRequired(), Length(min=8)])

    submit = SubmitField("Submit")


