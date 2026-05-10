from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise RuntimeError(
        'DATABASE_URL environment variable must be set to a MySQL connection string, '
        'for example: mysql+pymysql://taskuser:taskpass@db/tasks when running in Docker Compose'
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(30), nullable=False, default='Pending')
    due_date = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date,
            'created_at': self.created_at.isoformat()
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    status = request.form.get('status', 'Pending').strip()
    due_date = request.form.get('due_date', '').strip()

    if not title:
        return redirect(url_for('index'))

    task = Task(title=title, description=description, status=status, due_date=due_date)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title', task.title).strip()
        task.description = request.form.get('description', task.description).strip()
        task.status = request.form.get('status', task.status).strip()
        task.due_date = request.form.get('due_date', task.due_date).strip()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# API endpoints for external consumption
@app.route('/api/tasks', methods=['GET'])
def api_list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def api_create_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get('title', '')).strip()
    if not title:
        return jsonify({'error': 'title is required'}), 400
    task = Task(
        title=title,
        description=str(data.get('description', '')).strip(),
        status=str(data.get('status', 'Pending')).strip(),
        due_date=str(data.get('due_date', '')).strip()
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json(silent=True) or {}
    if 'title' in data and str(data['title']).strip():
        task.title = str(data['title']).strip()
    if 'description' in data:
        task.description = str(data['description']).strip()
    if 'status' in data:
        task.status = str(data['status']).strip()
    if 'due_date' in data:
        task.due_date = str(data['due_date']).strip()
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
