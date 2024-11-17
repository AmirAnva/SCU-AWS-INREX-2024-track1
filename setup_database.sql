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
    ('test_user1', 'hashed_password1', 'chrislo5311@gmail.com', -33.968100, 18.582020), -- Cape Town, South Africa
    ('test_user2', 'hashed_password2', 'chrislo5311@gmail.com', 40.712776, -74.005974), -- New York City, USA
    ('test_user3', 'hashed_password3', 'chrislo5311@gmail.com', 48.856613, 2.352222),  -- Paris, France
    ('test_user4', 'hashed_password4', 'chrislo5311@gmail.com', 35.689487, 139.691711), -- Tokyo, Japan
    ('test_user5', 'hashed_password5', 'chrislo5311@gmail.com', -23.550520, -46.633308), -- São Paulo, Brazil
    ('test_user6', 'hashed_password6', 'chrislo5311@gmail.com', 55.755825, 37.617298), -- Moscow, Russia
    ('test_user7', 'hashed_password7', 'chrislo5311@gmail.com', -37.813629, 144.963058), -- Melbourne, Australia
    ('test_user8', 'hashed_password8', 'chrislo5311@gmail.com', 51.507222, -0.127500), -- London, England
    ('test_user9', 'hashed_password9', 'chrislo5311@gmail.com', 34.052235, -118.243683), -- Los Angeles, USA
    ('test_user10', 'hashed_password10', 'chrislo5311@gmail.com', 28.613939, 77.209023), -- New Delhi, India
    ('test_user11', 'hashed_password11', 'chrislo5311@gmail.com', 31.230391, 121.473701), -- Shanghai, China
    ('test_user12', 'hashed_password12', 'chrislo5311@gmail.com', -1.292066, 36.821945), -- Nairobi, Kenya
    ('test_user13', 'hashed_password13', 'chrislo5311@gmail.com', -34.603722, -58.381592), -- Buenos Aires, Argentina
    ('test_user14', 'hashed_password14', 'chrislo5311@gmail.com', 37.774929, -122.419418), -- San Francisco, USA
    ('test_user15', 'hashed_password15', 'chrislo5311@gmail.com', 59.329323, 18.068581), -- Stockholm, Sweden
    ('test_user16', 'hashed_password16', 'chrislo5311@gmail.com', 47.614134, -122.326947),
    ('test_user17', 'hashed_password17', 'chrislo5311@gmail.com', 47.612483, -122.331927),
    ('test_user18', 'hashed_password18', 'chrislo5311@gmail.com', 47.609874, -122.337694),
    ('test_user19', 'hashed_password19', 'chrislo5311@gmail.com', 47.611924, -122.330234),
    ('test_user20', 'hashed_password20', 'chrislo5311@gmail.com', 47.608134, -122.334756),
    ('test_user21', 'hashed_password21', 'chrislo5311@gmail.com', 47.610972, -122.328367),
    ('test_user22', 'hashed_password22', 'chrislo5311@gmail.com', 47.612135, -122.327456),
    ('test_user23', 'hashed_password23', 'chrislo5311@gmail.com', 47.610459, -122.336987),
    ('test_user24', 'hashed_password24', 'chrislo5311@gmail.com', 47.609982, -122.329456),
    ('test_user25', 'hashed_password25', 'chrislo5311@gmail.com', 47.611743, -122.328457),
    ('test_user26', 'hashed_password26', 'chrislo5311@gmail.com', 47.610673, -122.334295),
    ('test_user27', 'hashed_password27', 'chrislo5311@gmail.com', 47.609212, -122.327845),
    ('test_user28', 'hashed_password28', 'chrislo5311@gmail.com', 47.611583, -122.335867),
    ('test_user29', 'hashed_password29', 'chrislo5311@gmail.com', 47.607489, -122.328349),
    ('test_user30', 'hashed_password30', 'chrislo5311@gmail.com', 47.613245, -122.326845),
    ('test_user31', 'hashed_password31', 'chrislo5311@gmail.com', 47.607594, -122.329124),
    ('test_user32', 'hashed_password32', 'chrislo5311@gmail.com', 47.608473, -122.337364),
    ('test_user33', 'hashed_password33', 'chrislo5311@gmail.com', 47.608952, -122.330582),
    ('test_user34', 'hashed_password34', 'chrislo5311@gmail.com', 47.610984, -122.325983),
    ('test_user35', 'hashed_password35', 'chrislo5311@gmail.com', 47.609932, -122.330784),
    ('test_user36', 'hashed_password36', 'chrislo5311@gmail.com', 47.612184, -122.333567),
    ('test_user37', 'hashed_password37', 'chrislo5311@gmail.com', 47.609891, -122.336245),
    ('test_user38', 'hashed_password38', 'chrislo5311@gmail.com', 47.611289, -122.338927),
    ('test_user39', 'hashed_password39', 'chrislo5311@gmail.com', 47.610567, -122.335862),
    ('test_user40', 'hashed_password40', 'chrislo5311@gmail.com', 47.612349, -122.331749),
    ('test_user41', 'hashed_password41', 'chrislo5311@gmail.com', 47.609722, -122.333056),
    ('test_user42', 'hashed_password42', 'chrislo5311@gmail.com', 47.613951, -122.329283),
    ('test_user43', 'hashed_password43', 'chrislo5311@gmail.com', 47.614892, -122.332789),
    ('test_user44', 'hashed_password44', 'chrislo5311@gmail.com', 47.614134, -122.326947),
    ('test_user45', 'hashed_password45', 'chrislo5311@gmail.com', 47.610673, -122.334295);

CREATE TABLE email_messages (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each email message
    subject VARCHAR(255) NOT NULL,     -- Subject of the email
    body TEXT NOT NULL                 -- Body of the email
);

INSERT INTO email_messages (subject, body)
VALUES
    ('Warnings!', 'Car accident in front! Pleas find alternatives way!'),
    ('Be careful!', 'Heavy rainy blocking sites!');
