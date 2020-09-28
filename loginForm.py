from flask_wtf import FlaskForm
from wtforms import SubmitField,BooleanField,IntegerField,StringField,TextAreaField,PasswordField
from wtforms.validators import DataRequired
from flask_wtf import Form

class LoginForm(Form):
    login = StringField('login',validators=[DataRequired()]);
    senha = PasswordField('senha',validators=[DataRequired()]);
    entrar = SubmitField('Entrar');