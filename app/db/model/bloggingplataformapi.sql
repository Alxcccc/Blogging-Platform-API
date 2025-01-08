CREATE DATABASE IF NOT EXISTS project CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE project;
CREATE TABLE IF NOT EXISTS posts (
    postID INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    content VARCHAR(250),
    category VARCHAR(50),
    tags VARCHAR(250),
    createdAt DATETIME,
    updateAt DATETIME
);

