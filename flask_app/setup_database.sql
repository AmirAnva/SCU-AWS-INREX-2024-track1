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
    ('test_user1', 'hashed_password1', 'test1@example.com', -33.968100, 18.582020), -- Cape Town, South Africa
    ('test_user2', 'hashed_password2', 'test2@example.com', 40.712776, -74.005974), -- New York City, USA
    ('test_user3', 'hashed_password3', 'test3@example.com', 48.856613, 2.352222),  -- Paris, France
    ('test_user4', 'hashed_password4', 'test4@example.com', 35.689487, 139.691711), -- Tokyo, Japan
    ('test_user5', 'hashed_password5', 'test5@example.com', -23.550520, -46.633308), -- São Paulo, Brazil
    ('test_user6', 'hashed_password6', 'test6@example.com', 55.755825, 37.617298), -- Moscow, Russia
    ('test_user7', 'hashed_password7', 'test7@example.com', -37.813629, 144.963058), -- Melbourne, Australia
    ('test_user8', 'hashed_password8', 'test8@example.com', 51.507222, -0.127500), -- London, England
    ('test_user9', 'hashed_password9', 'test9@example.com', 34.052235, -118.243683), -- Los Angeles, USA
    ('test_user10', 'hashed_password10', 'test10@example.com', 28.613939, 77.209023), -- New Delhi, India
    ('test_user11', 'hashed_password11', 'test11@example.com', 31.230391, 121.473701), -- Shanghai, China
    ('test_user12', 'hashed_password12', 'test12@example.com', -1.292066, 36.821945), -- Nairobi, Kenya
    ('test_user13', 'hashed_password13', 'test13@example.com', -34.603722, -58.381592), -- Buenos Aires, Argentina
    ('test_user14', 'hashed_password14', 'test14@example.com', 37.774929, -122.419418), -- San Francisco, USA
    ('test_user15', 'hashed_password15', 'test15@example.com', 59.329323, 18.068581); -- Stockholm, Sweden
