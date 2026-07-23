# Task_Management API with FastAPI, PostgreSQL & Docker

A RESTful Task Management API built with **FastAPI** that demonstrates CRUD operations using **PostgreSQL** as the persistence layer. The entire application is containerized with **Docker** and orchestrated using **Docker Compose**.

This project demonstrates how to migrate a RESTful CRUD API from SQLite to PostgreSQL while preserving the same API endpoints and application architecture. The backend is containerized using Docker and orchestrated with Docker Compose.

---

## Features

- Create a task
- Retrieve all tasks
- Retrieve a task by ID
- Update a task
- Delete a task
- Persistent PostgreSQL database
- Dockerized FastAPI application
- Multi-container setup using Docker Compose
- Environment variables managed through `.env`

---

## Tech Stack

- FastAPI
- PostgreSQL 17
- psycopg2
- Docker
- Docker Compose
- Python 3.13

---

## Project Structure

```
task-api/
│── app.py
│── crud.py
│── database.py
│── models.py
│── init.sql
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .env.example
│── README.md
```

---

## Architecture

```
                Client
                   │
                   ▼
              FastAPI Routes
                   │
                   ▼
            CRUD Repository
                   │
                   ▼
          PostgreSQL Database
             (Docker Container)
                   │
                   ▼
             Docker Volume
```

The API layer remains unchanged while only the persistence layer has been switched from SQLite to PostgreSQL.

---

## Persistence Layer

The previous SQLite implementation has been replaced with PostgreSQL.

Only the database implementation changed.

- API routes remain the same.
- Request bodies remain the same.
- Response formats remain the same.
- CRUD operations now execute PostgreSQL SQL queries.

This demonstrates separation between the API layer and the persistence layer.

---

## Database Initialization

When PostgreSQL starts for the first time, `init.sql` automatically creates the `tasks` table.

```sql
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

Sample tasks are also inserted during the initial database creation.

---

## Environment Variables

Create a `.env` file.

```
DATABASE_URL=postgresql://postgres:password@postgres:5432/taskdb
```

The `.env` file is ignored by Git.

An `.env.example` file is included for reference.

---

## Running the Project with Docker

### Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd task-api
```

### Start the application

```bash
docker compose up --build
```

The command automatically:

- Builds the FastAPI image
- Pulls the PostgreSQL image
- Creates the Docker network
- Creates a persistent Docker volume
- Starts both containers

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

Interactive ReDoc

```
http://localhost:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

## PostgreSQL Persistence

This project stores data inside a PostgreSQL Docker container.

The database files are stored inside a Docker Volume.

Because of the volume:

- Data survives application restarts.
- Data survives container restarts.
- The database is recreated only if the volume is removed.

---

## Verify Persistence

1. Start the application.

```bash
docker compose up
```

2. Create new tasks.

3. Stop the containers.

```bash
docker compose down
```

4. Start the application again.

```bash
docker compose up
```

5. Retrieve tasks.

The previously created tasks will still exist, demonstrating persistent storage.

---

## Pull the Docker Image

Pull the image from Docker Hub:

```bash
docker pull nasrinanwar931/task-api-api
```

Run the container:

```bash
docker run -d \
--name task-api \
-p 8000:8000 \
-v postgres_data:/var/lib/postgresql/data \
<YOUR_DOCKERHUB_USERNAME>/task-api:latest
```


<img width="592" height="115" alt="image" src="https://github.com/user-attachments/assets/f3fe30b7-a24d-46c4-8938-fe9c2b2bec17" />

---

## Learning Outcomes

- FastAPI CRUD API development
- PostgreSQL integration
- SQL queries with psycopg2
- Docker containerization
- Docker Compose
- Docker Volumes
- Environment variable management
- Database initialization with SQL scripts
- Separation of API and persistence layers

---

## Future Improvements

- Authentication & Authorization
- Pagination
- Search and filtering
- File uploads
- Task thumbnails
- PostgreSQL indexing
- Unit and integration testing
- CI/CD pipeline
- Deployment on cloud platforms

---

## Author

**Nasrin Anwar**

B.Sc. in Information Technology  
Jahangirnagar University

Backend Developer | Machine Learning Enthusiast | AI Developer
