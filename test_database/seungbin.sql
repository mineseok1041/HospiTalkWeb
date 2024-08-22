-- SQLite
CREATE TABLE Users (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO Users (id, name, email, password)
VALUES ('test_user', '테스트 사용자', 'test@example.com', 'password123');

