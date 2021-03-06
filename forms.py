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
    radios = RadioField('Luokka', default=1, choices=[(1, 'Myydään'), (2, 'Ostetaan'),('3', 'Vaihdetaan'), ('4', 'Lahjoitetaan')])
    cat = SelectField('Osasto', choices=[])
    image = FileField('Lisää kuva', validators=[FileAllowed(['jpg']),DataRequired()])
    submit = SubmitField('Lähetä')

class new_categoryForm(FlaskForm):
    cat = StringField('osasto', validators=[DataRequired()])
    submit = SubmitField('Lisää')

class search_Form(FlaskForm):
    cat = SelectField('Osastosta', choices=[])
    radios = RadioField('Luokka', default='1', choices=[('1', 'Myydään'), ('2', 'Ostetaan'),('3', 'Vaihdetaan'), ('4', 'Lahjoitetaan')])
    submit = SubmitField('Haku')
    item = StringField('Hae otsikosta')
    ad = StringField('Hae ilmoitustekstistä')
    submit = SubmitField('Haku')

class new_mesageForm(FlaskForm):
    message = TextAreaField('Ilmoitus teksti', validators=[DataRequired(), Length(min=2, max=3000)])
    submit = SubmitField('Lähetä')

	