-- Step 1: Create the database
CREATE DATABASE flask_app_db;

-- Step 2: Use the newly created database
USE flask_app_db;

-- Step 3: Create the 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Username, unique for each user
    password VARCHAR(255) NOT NULL,          -- Password, hashed
    email VARCHAR(100) NOT NULL UNIQUE,      -- Email, unique for each user
    latitude DECIMAL(10, 6) NOT NULL,        -- Latitude (decimal, precision 10, scale 6)
    longitude DECIMAL(10, 6) NOT NULL,       -- Longitude (decimal, precision 10, scale 6)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Step 4: Insert some sample data into the 'users' table (optional)
INSERT INTO users (username, password, email, latitude, longitude)
VALUES
    ('test_user1', 'hashed_password1', 'test1@example.com', -33.968100, 18.582020),
    ('test_user2', 'hashed_password2', 'test2@example.com', 40.712776, -74.005974);
