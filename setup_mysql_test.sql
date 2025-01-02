-- Check and create the testing database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check and create the testing user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;