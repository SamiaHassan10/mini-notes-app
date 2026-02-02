# mini-notes-app — Docker run instructions

This repository contains a small notes app with two services:

- `backend/` — Flask backend (ports: 5000)
- `frontend/` — Static frontend served in a container (ports: 8080)
- `docker-compose.yml` — Compose file that builds and runs both services

Prerequisites
- Docker (Docker Desktop or engine) installed and running.
- Docker Compose (either the `docker-compose` standalone or the `docker compose` plugin).

Quick start (recommended)
From the project root, run:

```bash
# Using docker-compose (v1)
docker-compose up --build

# Or using Docker Compose plugin (v2)
docker compose up --build
```

Run in background (detached):

```bash
docker-compose up -d --build
```

Stop and remove containers:

```bash
docker-compose down
```

Rebuild or run a single service

```bash
# Rebuild only the backend
docker-compose build backend
docker-compose up -d backend

# Rebuild only the frontend
docker-compose build frontend
docker-compose up -d frontend
```

View logs

```bash
docker-compose logs -f
docker-compose logs -f backend
```

Accessing the app
- Frontend: http://localhost:8080
- Backend API: http://localhost:5000

Notes & troubleshooting
- If ports 8080 or 5000 are already in use, stop the process using them or change the host port mapping in `docker-compose.yml`.
- On Windows, you can run the above commands in PowerShell or a WSL2 shell. Ensure Docker Desktop is running and WSL integration is enabled if using WSL.
- If you get permission or daemon errors, verify the Docker service is running (`docker ps` should list containers or return an empty list without errors).
- Use `docker-compose ps` or `docker ps` to inspect running containers.

Useful commands

```bash
# Show running containers
docker ps

# Show all containers (including stopped)
docker ps -a

# Remove stopped containers
docker container prune
```

CI / tests ✅

- A GitHub Actions workflow is included at `.github/workflows/ci.yml`. It builds the Compose stack, runs a smoke test and linting, and tears down the services.

Run tests and lint locally:

```bash
# Install dev dependencies (recommended inside a virtualenv)
python -m pip install -r backend/requirements-dev.txt

# Run tests
python -m pytest -q

# Run linter
python -m flake8 backend
```

If you want, I can also add a short `dev` script or `Makefile` to simplify these commands.
