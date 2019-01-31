from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField, DecimalField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    picture = StringField('Add picture', validators=[])
    submit = SubmitField('Submit')

class StvoriIzletForm(FlaskForm):
    name = StringField('Ime izleta', validators=[DataRequired()])
    description = TextAreaField('Opis Izleta', validators=[Length(min=0, max=140)])
    location = StringField('Lokacija', validators=[DataRequired()])
    transport = StringField('Prijevoz', validators=[DataRequired()])
    begin = DateField('Pocetak', format='%Y-%m-%d', validators=[DataRequired()])
    end = DateField('Kraj', format='%Y-%m-%d', validators=[DataRequired()])
    picture = StringField('Ucitaj sliku')
    cost = DecimalField('Cijena', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    submit = SubmitField('Submit')

class JoinIzlet(FlaskForm):
    izlet_id = HiddenField()
    submit = SubmitField('Submit')

class EditIzlet(FlaskForm):
    name = StringField('Ime izleta', validators=[DataRequired()])
    description = TextAreaField('Opis Izleta', validators=[Length(min=0, max=140)])
    location = StringField('Lokacija', validators=[DataRequired()])
    transport = StringField('Prijevoz', validators=[DataRequired()])
    begin = DateField('Pocetak', format='%Y-%m-%d', validators=[DataRequired()])
    end = DateField('Kraj', format='%Y-%m-%d', validators=[DataRequired()])
    picture = StringField('Ucitaj sliku')
    cost = DecimalField('Cijena', places=2, rounding=None, use_locale=False, number_format=None, validators=[DataRequired()])
    izlet_id = HiddenField()
    submit = SubmitField('Submit')