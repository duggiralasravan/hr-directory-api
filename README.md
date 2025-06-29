[![CI](https://github.com/yourusername/hr-directory-api/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/hr-directory-api/actions)

# HR Directory API

A simple FastAPI microservice to search employees with dynamic column configuration per organization.

## Features
- Filter by status, location, company, department, and position
- Dynamic columns per organization
- Simple in-memory rate limiting
- Containerized with Docker
- OpenAPI compliant
- Unit tested

## Running

```bash
# Local
uvicorn app.main:app --reload

# Docker
docker build -t hr-api .
docker run -p 8000:8000 hr-api
```


## Seeding the DB

```bash
python seed.py
```
