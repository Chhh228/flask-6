from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[
        DataRequired(message='Введите имя'),
        Length(min=2, max=50, message='От 2 до 50 символов')
    ])
    email = EmailField('Email', validators=[
        DataRequired(message='Введите email'),
        Email(message='Некорректный формат email')
    ])
    age = IntegerField('Возраст', validators=[
        DataRequired(message='Введите возраст'),
        NumberRange(min=18, max=99, message='Возраст должен быть от 18 до 99 лет')
    ])
    track = SelectField('Направление', choices=[
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('data', 'Data Science'),
        ('devops', 'DevOps')
    ])
    experience = IntegerField('Опыт (лет)', validators=[
        DataRequired(message='Введите опыт работы'),
        NumberRange(min=0, max=50, message='Опыт должен быть от 0 до 50 лет')
    ])
    agree = BooleanField('Принимаю условия участия', validators=[
        DataRequired(message='Необходимо принять условия')
    ])
    submit = SubmitField('Зарегистрироваться')
