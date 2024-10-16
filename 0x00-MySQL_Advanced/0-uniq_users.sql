-- create table user with some requiremnets
CREATE TABLE IF NOT EXISTS users(
    id INT NOt NULL AUTO_INCREMENT PRIMARY KEY,
    emai VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
