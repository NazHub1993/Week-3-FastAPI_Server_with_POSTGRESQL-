CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    done BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks(title, done)
VALUES
    ('Learn FastAPI', FALSE),
    ('Learn SQL', FALSE);