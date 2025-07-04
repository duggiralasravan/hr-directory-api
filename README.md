[![CI](https://github.com/duggiralasravan/hr-directory-api/actions/workflows/ci.yml/badge.svg)](https://github.com/duggiralasravan/hr-directory-api/actions)

# HR Directory API

A simple FastAPI microservice to search employees with dynamic column configuration per organization.

## Features
- Filter by status, location, company, department, and position
- Dynamic columns per organization
- Simple in-memory rate limiting
- Containerized with Docker
- OpenAPI compliant
- Unit tested

## Project Structure
```shell
hr_directory/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── db.py
│   ├── crud.py
│   ├── rate_limiter.py
│   └── config.py
├── tests/
│   └── test_search_api.py
├── Dockerfile
├── requirements.txt
├── README.md
└── openapi.json
```

## Running The Project Set Up
```bash
# Clone repo
git clone https://github.com/duggiralasravan/hr-directory-api
cd hr-directory-api

# Run locally
uvicorn app.main:app --reload

# OR with Docker
docker build -t hr-api .
docker run -p 8000:8000 hr-api
```

## Seeding the DB

```bash
python seed.py
```

## Running Test Cases
Option 1: Run with unittest (built-in, recommended since you're restricted to standard libraries)

```bash
python -m unittest discover -s tests
```
Option 2: Run a single test file manually

```bash
python tests/test_search_api.py
```

Option 3: Run inside Docker container
```bash
docker exec -it <container_name_or_id> python -m unittest discover -s tests
```
