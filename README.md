# Task API

A simple in-memory CRUD API for managing tasks, built with FastAPI as part of a backend development internship assignment.

## What this is

This API lets you create, read, update, and delete tasks. Data is stored in memory only — it resets every time the server restarts. There's no database yet; that's a deliberate first step before adding persistence.

## How to run

1. Clone this repo and `cd` into it
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `.\venv\Scripts\Activate.ps1`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install fastapi uvicorn`
5. Start the server: `uvicorn main:app --reload`
6. Visit `http://localhost:8000/docs` for interactive Swagger UI

## Endpoints

| Method | Endpoint         | Meaning                          |
|--------|------------------|-----------------------------------|
| GET    | `/`              | API info                          |
| GET    | `/health`        | Health check                      |
| GET    | `/tasks`         | List all tasks                    |
| GET    | `/tasks/{id}`    | Get a single task                 |
| POST   | `/tasks`         | Create a new task                 |
| PUT    | `/tasks/{id}`    | Update a task's title and/or done status |
| DELETE | `/tasks/{id}`    | Delete a task                     |

## Example request

```
curl -i http://localhost:8000/tasks
```
## Swagger UI

![Swagger UI showing all endpoints](swagger-screenshot.png)

## Notes

- Built stage by stage, with a commit after each stage — see commit history for progress from "hello server" to full CRUD.
- Status codes follow REST conventions: `201` for created, `200` for success, `204` for deleted with no content, `400` for bad input, `404` for not found.
## Running Postgres (Docker)

This project now uses Postgres instead of SQLite. Start it with:

This runs Postgres 16 in a container named `taskdb`, with a named volume (`taskdata`) so data survives container restarts.
