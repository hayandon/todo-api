# Task API

A simple in-memory CRUD API for managing tasks, built with FastAPI as part of a backend development internship assignment.

## What this is

This API lets you create, read, update, and delete tasks. Data is stored in memory only — it resets every time the server restarts. There's no database yet; that's a deliberate first step before adding persistence.
# Task API

A CRUD API for managing tasks, built with FastAPI and backed by a SQLite database. Originally built with in-memory storage; now persists data to disk so tasks survive a server restart.

## Why SQLite

SQLite needs no separate server, no install, and no configuration — the entire database is a single file (`tasks.db`) that Python's built-in `sqlite3` module can read and write directly. That makes it a natural next step after in-memory storage: same zero-setup simplicity, but now the data survives a restart. It's a great fit for small projects and prototypes before scaling up to something like PostgreSQL.

## Where the database lives

The database is a single file, `tasks.db`, created automatically in the project root the first time the app runs. It is not committed to Git (see `.gitignore`) — each person running the project gets their own local copy, seeded with 3 example tasks the first time.

## How to run

1. Clone this repo and `cd` into it
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `.\venv\Scripts\Activate.ps1`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install fastapi uvicorn`
5. Start the server: `uvicorn main:app --reload`
   - On first run, this automatically creates `tasks.db` and seeds it with 3 example tasks
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

## Example SQL query

Run directly against `tasks.db` using DB Browser for SQLite:

```sql
SELECT * FROM tasks WHERE done = 1;
```

This returns only completed tasks — and the API reflects the change instantly, since both read from the same database file.

## Database viewer

![DB Browser showing the tasks table](db-screenshot.png)

## Notes

- Data now persists in `tasks.db` (SQLite) instead of a Python list — restarting the server no longer wipes your tasks.
- All queries use parameterized statements (`?` placeholders) to avoid SQL injection.
- Status codes follow REST conventions: `201` created, `200` success, `204` deleted with no content, `400` bad input, `404` not found.
- Built stage by stage with a commit after each — see commit history for the full progression from in-memory storage to SQLite.
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
