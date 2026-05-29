from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from forms import TaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-tasks'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    # Filtering
    filter_status = request.args.get('filter')
    query = Task.query
    if filter_status == 'active':
        query = query.filter_by(done=False)
    elif filter_status == 'done':
        query = query.filter_by(done=True)

    tasks = query.order_by(Task.created_at.desc()).all()

    return render_template('index.html', form=form, tasks=tasks, current_filter=filter_status)

@app.route('/done/<int:id>', methods=['POST'])
def mark_done(id):
    task = Task.query.get_or_404(id)
    task.done = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
