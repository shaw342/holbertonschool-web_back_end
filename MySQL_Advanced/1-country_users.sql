-- Create the 'users' table if it does not already exist
-- 'id' column: auto-incrementing primary key
-- 'email' column: unique and non-null string
-- 'name' column: string
--  country comlum: enum 

CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
);