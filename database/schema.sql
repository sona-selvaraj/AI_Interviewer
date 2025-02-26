 
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE user_interviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    response_text TEXT NOT NULL,
    chroma_id TEXT NOT NULL
);
