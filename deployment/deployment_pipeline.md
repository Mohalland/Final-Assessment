# Deployment Pipeline

## Source Control
The project is managed using Git and can be hosted in a GitHub repository.

## CI/CD Pipeline
The project includes a GitHub Actions CI/CD pipeline (`.github/workflows/ci-cd.yml`) that:
- Runs tests on every push and pull request to the main branch
- Builds and pushes a Docker image to GitHub Container Registry on successful pushes to main
- Triggers deployment on new releases

### CI/CD Jobs
1. **Test**: Installs dependencies and runs pytest on the test suite
2. **Build and Push**: Builds the Docker image and pushes it to GHCR
3. **Deploy**: Triggers deployment (currently set up for Railway as an example)

## Deployment Target
The application is designed to be deployed to a cloud hosting provider such as Render, Railway, PythonAnywhere, Heroku-compatible hosting, or a virtual private server.

## Deployment Steps
1. Create a GitHub repository.
2. Upload or push the project source code to the repository.
3. The CI/CD pipeline will automatically run tests and build the Docker image.
4. For deployment, configure your cloud platform to pull from GitHub Container Registry or integrate with the deploy job.
5. Set the start command to:
   ```bash
   docker compose up --build
   ```
6. Deploy the application.
7. Open the generated public URL and test the CRUD functions.

## Local Test Commands
```bash
cd source_code
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Or with Docker:
```bash
docker compose up --build
```

## Public URL Evidence
After deployment, record the cloud URL here:

Application URL: _______________________________

Repository URL: _______________________________
