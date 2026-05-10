import os
import sys
import tempfile

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source_code'))
sys.path.insert(0, PROJECT_ROOT)

import app as task_app


def test_homepage_loads():
    task_app.app.config['TESTING'] = True
    task_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with task_app.app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Task Records' in response.data


def test_api_create_and_list_task():
    task_app.app.config['TESTING'] = True
    task_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with task_app.app.app_context():
        task_app.db.drop_all()
        task_app.db.create_all()
    with task_app.app.test_client() as client:
        create_response = client.post('/api/tasks', json={
            'title': 'Prepare assessment submission',
            'description': 'Package final documents and source code.',
            'status': 'In Progress',
            'due_date': '2026-05-15'
        })
        assert create_response.status_code == 201
        list_response = client.get('/api/tasks')
        assert list_response.status_code == 200
        assert list_response.get_json()[0]['title'] == 'Prepare assessment submission'
