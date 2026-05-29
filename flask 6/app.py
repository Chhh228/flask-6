from flask import Flask, render_template, redirect, url_for, session
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'  # Обязательно для WTForms

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Сохраняем данные в session
        session['participant'] = {
            'name': form.name.data,
            'email': form.email.data,
            'age': form.age.data,
            'track': dict(form.track.choices).get(form.track.data), # Сохраняем красивое название направления
            'experience': form.experience.data
        }
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    participant = session.get('participant')
    if not participant:
        return redirect(url_for('register'))
    return render_template('success.html', participant=participant)

if __name__ == '__main__':
    app.run(debug=True)
