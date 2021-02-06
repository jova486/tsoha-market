from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Käyttäjätunnus', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Salasana', validators=[DataRequired()])
    confirm_password = PasswordField('Vahvista salasana',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Kirjaudu')


class LoginForm(FlaskForm):
    username = StringField('Käyttäjätunnus', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Salasana', validators=[DataRequired()])
    remember = BooleanField('Muista minut')
    submit = SubmitField('Kirjaudu')

										  

class new_adForm(FlaskForm):
    item = StringField('Otsikko', validators=[DataRequired()])
    ad = TextAreaField('Ilmoitus teksti')
    radios = RadioField('Luokka', default='option1', choices=[('option1', 'Myydään'), ('option2', 'Ostetaan')])
    cat = SelectField('Osasto', choices=[])
    image = FileField('Lisää kuva', validators=[FileAllowed(['jpg'])])
    submit = SubmitField('Lataa')

class new_mesageForm(FlaskForm):
    message = TextAreaField('Ilmoitus teksti')
    submit = SubmitField('Lähetä')

	