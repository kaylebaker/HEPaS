-- Create Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id VARCHAR(255) PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(255),
    course_code VARCHAR(255),
    units_attempted SMALLINT,
    units_completed SMALLINT,
    course_status VARCHAR(255)
);

-- Create Courses table
CREATE TABLE IF NOT EXISTS Courses (
    course_code VARCHAR(255) PRIMARY KEY,
    course_title VARCHAR(255),
    year_created SMALLINT,
    year_cancelled SMALLINT,
    coordinator_name VARCHAR(255),
    coordinator_email VARCHAR(255),
    coordinator_mobile VARCHAR(255)
);

-- Create StudentUnits table
CREATE TABLE IF NOT EXISTS StudentUnits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id VARCHAR(255),
    unit_code VARCHAR(255),
    unit_title VARCHAR(255),
    unit_score SMALLINT,
    unit_grade VARCHAR(255),
    year_attempted SMALLINT,
    semester_attempted SMALLINT,
    note TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    UNIQUE (student_id, unit_code)
);