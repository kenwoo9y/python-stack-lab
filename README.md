# python-stack-lab

A lab for exploring and experimenting with a Python backend development stack, including FastAPI, SQLAlchemy, uv, Ruff, ty, Pytest, PostgreSQL, Docker, and GitHub Actions.

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=for-the-badge&logo=SQLAlchemy&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64.svg?style=for-the-badge&logo=Ruff&logoColor=black)
![ty](https://img.shields.io/badge/ty-46EBE1.svg?style=for-the-badge&logo=ty&logoColor=black)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

### Programming Languages
- [Python](https://www.python.org/) v3.11 - Development language

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) v0.110 - High-performance Python web framework
- [Uvicorn](https://www.uvicorn.org/) v0.29 - ASGI server for running the FastAPI app
- [SQLAlchemy](https://www.sqlalchemy.org/) v2.0 - SQL toolkit and ORM, used in async mode
- [asyncpg](https://magicstack.github.io/asyncpg/) v0.29 - Async PostgreSQL driver for the application
- [psycopg2](https://www.psycopg.org/) v2.9 - Sync PostgreSQL driver used for database setup/migration scripts

### Database
- [PostgreSQL](https://www.postgresql.org/) v16 - Primary relational database

### Development Environment
- [uv](https://docs.astral.sh/uv/) - Python package manager
- [Docker](https://www.docker.com/) with Compose v3.9 - Containerization platform for building and managing applications

### Testing & Quality Assurance
- [pytest](https://docs.pytest.org/) v8.4 - Python testing framework
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/) v0.23 - Support for testing async FastAPI/SQLAlchemy code
- [pytest-cov](https://pytest-cov.readthedocs.io/) v6.0 - Code coverage plugin
- [httpx](https://www.python-httpx.org/) v0.27 - HTTP client used for testing FastAPI endpoints
- [aiosqlite](https://github.com/omnilib/aiosqlite) v0.20 - Async SQLite driver used for isolated test databases
- [Ruff](https://docs.astral.sh/ruff/) v0.7 - Fast Python linter and formatter
- [ty](https://docs.astral.sh/ty/) v0.0.80 - Fast Python type checker

### CI/CD
- GitHub Actions - Continuous Integration and Deployment

## Setup
### Initial Setup
1. Clone this repository:
    ```
    $ git clone https://github.com/kenwoo9y/python-stack-lab.git
    $ cd python-stack-lab
    ```

2. Create environment file:
    ```
    $ cp .env.example .env
    ```
    Edit `.env` file to match your environment if needed.

3. Build the required Docker images:
    ```
    $ make build-local
    ```

4. Start the containers:
    ```
    $ make up
    ```

5. Apply database migrations:
    ```
    $ make migrate
    ```

6. Verify the API is running by accessing http://localhost:8000/docs.

## Usage
### API Documentation
- Swagger UI: http://localhost:8000/docs

### Container Management
- Check container status:
    ```
    $ make ps
    ```
- View container logs:
    ```
    $ make logs
    ```
- Stop containers:
    ```
    $ make down
    ```

## Development
### Running Tests
- Run tests:
    ```
    $ make test
    ```
- Run tests with coverage:
    ```
    $ make test-coverage
    ```
### Code Quality Checks
- Lint check:
    ```
    $ make lint-check
    ```
- Apply lint fixes:
    ```
    $ make lint-fix
    ```
- Check code formatting:
    ```
    $ make format-check
    ```
- Apply code formatting:
    ```
    $ make format-fix
    ```
- Run type check:
    ```
    $ make type-check
    ```

## Database
### Configuring the Database
1. Edit `.env` file:

```
DB_HOST=postgresql-db
DB_PORT=5432
DB_NAME=todo
DB_USER=<your_username>
DB_PASSWORD=<your_password>
```

2. Rebuild and restart the application:
```
$ make build-local
$ make up
$ make migrate
```

### Database Access
- Access PostgreSQL database:
    ```
    $ make psql
    ```
