# Project Guidelines

## Scope
- This repository is a workshop scaffold for building the OctoFit Tracker app with:
  - Backend: Django + Django REST Framework + MongoDB (Djongo)
  - Frontend: React
- Follow detailed implementation guidance in:
  - [.github/instructions/octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
  - [.github/instructions/octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
  - [.github/instructions/octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)

## Terminal and Environment Rules
- Do not change directories while running terminal commands.
- Run commands from repo root by passing explicit paths (for example, using `--prefix` or full workspace-relative paths).
- Use only these service ports:
  - 8000 (public): Django backend
  - 3000 (public): React frontend
  - 27017 (private): MongoDB

## Project Structure
- Target application layout:
  - `octofit-tracker/backend/`
  - `octofit-tracker/frontend/`

## Build and Setup Commands
- Create Python virtual environment:
  - `python3 -m venv octofit-tracker/backend/venv`
- Install backend dependencies:
  - `source octofit-tracker/backend/venv/bin/activate`
  - `pip install -r octofit-tracker/backend/requirements.txt`
- Verify MongoDB process when needed:
  - `ps aux | grep mongod`

## Data and API Conventions
- Use Django ORM for data structure and data operations. Do not use direct MongoDB scripts for app data modeling.
- In backend serializers, convert `ObjectId` fields to strings.
- For API checks during development, use `curl` endpoint tests.

## Documentation
- Product context and goals: [docs/octofit_story.md](docs/octofit_story.md)
- Top-level exercise context: [README.md](README.md)
