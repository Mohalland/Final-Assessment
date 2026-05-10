# Task Manager Web Application

## Project Summary
This is a functional CRUD web application designed for a final web application development assessment. The application allows users to list, add, update, and delete task records in a MySQL database.

## Technologies Used
- Python Flask web framework
- MySQL database
- Flask-SQLAlchemy ORM
- PyMySQL database driver
- HTML, CSS, and Jinja templates
- Git/GitHub for source control
- Gunicorn for cloud deployment

## Features
- List task records
- Add new task records
- Edit existing task records
- Delete task records
- REST-style JSON API endpoints for consumption
- Cloud-ready deployment files

## API Endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks` | Return all task records |
| POST | `/api/tasks` | Create a new task |
| GET | `/api/tasks/<id>` | Return one task |
| PUT | `/api/tasks/<id>` | Update one task |
| DELETE | `/api/tasks/<id>` | Delete one task |

## Run Locally
```bash
cd source_code
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL='mysql+pymysql://user:password@host/dbname'
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

### Local MySQL setup
If you run locally, you must provide a working MySQL instance and set `DATABASE_URL` before starting the app. The application will raise an error if `DATABASE_URL` is not defined.

## Run with Docker Compose
From the project root:
```bash
docker compose up --build
```

The web app will be available at `http://127.0.0.1:5000`. Docker Compose starts a MySQL container and the `web` service connects to it via:

`mysql+pymysql://taskuser:taskpass@db/tasks`

The Compose MySQL service is configured with:
- database: `tasks`
- user: `taskuser`
- password: `taskpass`
- root password: `rootpass`

To stop and remove containers:
```bash
docker compose down
```

## Run Tests
```bash
pip install -r source_code/requirements.txt
pytest testing
```

## Deployment
Use the deployment guide in `deployment/deployment_pipeline.md`.
