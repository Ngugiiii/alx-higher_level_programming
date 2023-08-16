-- Change to the hbtn_0c_0 database
USE hbtn_0c_0;

-- Convert the first_table's name field to UTF8mb4 collation
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the whole database to UTF8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
