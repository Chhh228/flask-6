from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Заголовок задачи', validators=[
        DataRequired(message='Обязательное поле'),
        Length(min=3, max=150, message='Длина от 3 до 150 символов')
    ])
    description = TextAreaField('Описание', validators=[
        DataRequired(message='Обязательное поле'),
        Length(min=5, message='Минимум 5 символов')
    ])
    priority = SelectField('Приоритет', choices=[
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ])
    submit = SubmitField('Добавить задачу')
