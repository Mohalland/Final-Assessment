# Deployment Pipeline

## Source Control
The project is managed using Git and can be hosted in a GitHub repository.

## CI/CD Pipeline
The project includes a GitHub Actions CI/CD pipeline (`.github/workflows/ci-cd.yml`) that:
- Runs tests on every push and pull request to the main branch
- Builds and pushes a Docker image to GitHub Container Registry on successful pushes to main
- Triggers deployment on new releases (optional, as Render handles auto-deployment on pushes to main)

### CI/CD Jobs
1. **Test**: Installs dependencies and runs pytest on the test suite
2. **Build and Push**: Builds the Docker image and pushes it to GHCR (optional for Render)
3. **Deploy**: Currently set up for Railway; can be adapted for Render or disabled since Render auto-deploys

## Deployment Target
The application is deployed to Render.com, a cloud hosting provider that supports Docker-based web services.

## Deployment Steps for Render
1. Create a GitHub repository and push the project source code.
2. Sign up/login to [Render.com](https://render.com/).
3. Click "New +" and select "Web Service".
4. Connect your GitHub account and select the repository.
5. Configure the service:
   - **Name**: task-manager-web-app (or your choice)
   - **Environment**: Docker
   - **Region**: Choose closest to your users (e.g., Oregon)
   - **Branch**: main
   - **Root Directory**: (leave blank, or specify if needed)
   - **Dockerfile Path**: Dockerfile (in root)
   - **Docker Command**: (leave blank, uses CMD from Dockerfile)
6. Set environment variables:
   - **DATABASE_URL**: Set to your Render MySQL database connection string, e.g., `mysql+pymysql://user:pass@host/dbname`
7. For the database, create a separate MySQL service on Render:
   - Go to Render dashboard, "New +" > "Database" > "MySQL"
   - Note the connection string and update DATABASE_URL accordingly
8. Deploy the web service.
9. Once deployed, the app will be available at the generated Render URL.

## Environment Variables for Render
- `DATABASE_URL`: Set to your Render MySQL database connection string

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
