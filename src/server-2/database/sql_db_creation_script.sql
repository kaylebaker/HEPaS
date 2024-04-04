-- Create Courses table
CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code VARCHAR(3),
    course_title VARCHAR(255),
    year_created SMALLINT,
    year_cancelled SMALLINT,
    coordinator_name VARCHAR(255),
    coordinator_email VARCHAR(255),
    coordinator_mobile VARCHAR(10)
);

-- Insert 20 Course records
INSERT INTO Courses (course_code, course_title, year_created, year_cancelled, coordinator_name, coordinator_email, coordinator_mobile)
VALUES
    ('B65', 'Bachelor of Computer Science', 2020, NULL, 'John Smith', 'john.smith@example.com', '0412345678'),
    ('M75', 'Master of Engineering', 2018, NULL, 'Emily Johnson', 'emily.johnson@example.com', '0423456789'),
    ('B82', 'Bachelor of Mathematics', 2019, NULL, 'Michael Brown', 'michael.brown@example.com', '0434567890'),
    ('D94', 'Doctor of Physics', 2021, NULL, 'Sarah Davis', 'sarah.davis@example.com', '0445678901'),
    ('B47', 'Bachelor of Biology', 2017, NULL, 'David Wilson', 'david.wilson@example.com', '0456789012'),
    ('M31', 'Master of Chemistry', 2022, NULL, 'Jessica Martinez', 'jessica.martinez@example.com', '0467890123'),
    ('B58', 'Bachelor of Software Engineering', 2019, NULL, 'Mark Taylor', 'mark.taylor@example.com', '0478901234'),
    ('M12', 'Master of Literature', 2016, NULL, 'Jennifer Garcia', 'jennifer.garcia@example.com', '0489012345'),
    ('B24', 'Bachelor of Business Analytics', 2020, NULL, 'Matthew Rodriguez', 'matthew.rodriguez@example.com', '0490123456'),
    ('D39', 'Doctor of Astrophysics', 2018, NULL, 'Amanda Lopez', 'amanda.lopez@example.com', '0401234567'),
    ('B78', 'Bachelor of Environmental Science', 2021, NULL, 'Robert Hernandez', 'robert.hernandez@example.com', '0413579246'),
    ('M83', 'Master of Organic Chemistry', 2017, NULL, 'Laura Gonzalez', 'laura.gonzalez@example.com', '0424681357'),
    ('B42', 'Bachelor of Artificial Intelligence', 2019, NULL, 'Daniel Perez', 'daniel.perez@example.com', '0435792468'),
    ('M57', 'Master of English Literature', 2016, NULL, 'Melissa Sanchez', 'melissa.sanchez@example.com', '0446813579'),
    ('B19', 'Bachelor of Data Science', 2020, NULL, 'Jason Martinez', 'jason.martinez@example.com', '0457924680'),
    ('M26', 'Master of Theoretical Physics', 2018, NULL, 'Maria Young', 'maria.young@example.com', '046035791'),
    ('B10', 'Bachelor of Biotechnology', 2021, NULL, 'Kevin Scott', 'kevin.scott@example.com', '0479146802'),
    ('M32', 'Master of Physical Chemistry', 2017, NULL, 'Jessica Harris', 'jessica.harris@example.com', '0480257913'),
    ('B44', 'Bachelor of Computer Engineering', 2019, NULL, 'Mark Clark', 'mark.clark@example.com', '0491368024'),
    ('M56', 'Master of World Literature', 2016, NULL, 'Lauren King', 'lauren.king@example.com', '0402479135');


-- Create Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id VARCHAR(8) PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(10),
    course_code VARCHAR(255),
    units_attempted SMALLINT,
    units_completed SMALLINT,
    course_status VARCHAR(255),
    FOREIGN KEY (course_code) REFERENCES Courses(course_code)
);

-- Insert 50 Student records
INSERT INTO Students (student_id, fname, lname, email, mobile, course_code, units_attempted, units_completed, course_status)
VALUES
    ('12345678', 'John', 'Doe', 'john.doe@example.com', '0412345678', 'B65', 4, 4, 'Active'),
    ('23456789', 'Jane', 'Smith', 'jane.smith@example.com', '0423456789', 'M75', 3, 2, 'Inactive'),
    ('34567890', 'Michael', 'Johnson', 'michael.johnson@example.com', '0434567890', 'B82', 5, 5, 'Active'),
    ('45678901', 'Emily', 'Brown', 'emily.brown@example.com', '0445678901', 'D94', 2, 1, 'Inactive'),
    ('56789012', 'David', 'Anderson', 'david.anderson@example.com', '0456789012', 'B47', 3, 3, 'Active'),
    ('67890123', 'Sarah', 'Martinez', 'sarah.martinez@example.com', '0467890123', 'M31', 4, 4, 'Active'),
    ('78901234', 'Christopher', 'Taylor', 'christopher.taylor@example.com', '0478901234', 'B58', 3, 2, 'Inactive'),
    ('89012345', 'Jennifer', 'Garcia', 'jennifer.garcia@example.com', '0489012345', 'M12', 4, 3, 'Active'),
    ('90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com', '0490123456', 'B24', 5, 5, 'Active'),
    ('01234567', 'Amanda', 'Lopez', 'amanda.lopez@example.com', '0401234567', 'D39', 3, 2, 'Inactive'),
    ('13579246', 'Robert', 'Hernandez', 'robert.hernandez@example.com', '0413579246', 'B78', 4, 4, 'Active'),
    ('24681357', 'Laura', 'Gonzalez', 'laura.gonzalez@example.com', '0424681357', 'M83', 3, 2, 'Inactive'),
    ('35792468', 'Daniel', 'Perez', 'daniel.perez@example.com', '0435792468', 'B42', 5, 4, 'Active'),
    ('46813579', 'Melissa', 'Sanchez', 'melissa.sanchez@example.com', '0446813579', 'M57', 2, 1, 'Inactive'),
    ('57924680', 'Jason', 'Martinez', 'jason.martinez@example.com', '0457924680', 'B19', 4, 4, 'Active'),
    ('68035791', 'Maria', 'Young', 'maria.young@example.com', '046035791', 'M26', 3, 2, 'Inactive'),
    ('79146802', 'Kevin', 'Scott', 'kevin.scott@example.com', '0479146802', 'B10', 5, 5, 'Active'),
    ('80257913', 'Jessica', 'Harris', 'jessica.harris@example.com', '0480257913', 'M32', 3, 2, 'Inactive'),
    ('91368024', 'Mark', 'Clark', 'mark.clark@example.com', '0491368024', 'B44', 4, 3, 'Active'),
    ('02479135', 'Lauren', 'King', 'lauren.king@example.com', '0402479135', 'M56', 3, 2, 'Inactive'),
    ('13579135', 'Laura', 'King', 'laura.king@example.com', '0401357913', 'B44', 4, 3, 'Active'),
    ('24680246', 'Steven', 'Lee', 'steven.lee@example.com', '0424680246', 'M26', 3, 2, 'Inactive'),
    ('46802468', 'Rachel', 'Wright', 'rachel.wright@example.com', '0446802468', 'B65', 4, 3, 'Active'),
    ('68024680', 'Justin', 'Lopez', 'justin.lopez@example.com', '0468024680', 'M75', 3, 2, 'Inactive'),
    ('80246802', 'Christina', 'Green', 'christina.green@example.com', '0480246802', 'B82', 5, 4, 'Active'),
    ('02468024', 'Brandon', 'Adams', 'brandon.adams@example.com', '0402468024', 'D94', 2, 1, 'Inactive'),
    ('24687246', 'Megan', 'Baker', 'megan.baker@example.com', '0424680246', 'B47', 3, 3, 'Active'),
    ('46852468', 'Eric', 'Rivera', 'eric.rivera@example.com', '0446802468', 'M31', 4, 4, 'Active'),
    ('68124680', 'Amy', 'Allen', 'amy.allen@example.com', '0468024680', 'B58', 3, 2, 'Inactive');


-- Create StudentUnits table
CREATE TABLE IF NOT EXISTS StudentUnits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id VARCHAR(8),
    unit_code VARCHAR(7) CHECK (
		LENGTH(unit_code) = 7 AND 
        SUBSTR(unit_code, 1, 3) BETWEEN 'AAA' AND 'ZZZ' AND 
        SUBSTR(unit_code, 4) BETWEEN '0000' AND '9999'
	),
    unit_title VARCHAR(255),
    unit_score SMALLINT,
    unit_grade VARCHAR(2) GENERATED ALWAYS AS (
        CASE
            WHEN unit_score < 50 THEN 'F'
            WHEN unit_score < 60 THEN 'P'
            WHEN unit_score < 70 THEN 'CR'
            WHEN unit_score < 80 THEN 'D'
            ELSE 'HD'
        END
    ),
    year_attempted SMALLINT,
    semester_attempted SMALLINT,
    note TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Insert StudentUnits records
INSERT INTO StudentUnits (student_id, unit_code, unit_title, unit_score, year_attempted, semester_attempted, note)
VALUES
    ('12345678', 'CSA0101', 'Introduction to Programming', 85, 2020, 1, NULL),
    ('12345678', 'CSA0101', 'Introduction to Programming', 90, 2020, 2, NULL),
    ('12345678', 'CSA0102', 'Data Structures', 78, 2021, 1, NULL),
    ('23456789', 'CSA0101', 'Introduction to Programming', 70, 2020, 1, NULL),
    ('23456789', 'CSA0102', 'Data Structures', 85, 2020, 2, NULL),
    ('34567890', 'MTH0101', 'Calculus I', 95, 2021, 1, NULL),
    ('34567890', 'MTH0102', 'Calculus II', 88, 2021, 2, NULL),
    ('45678901', 'PHY0101', 'Physics Fundamentals', 60, 2020, 1, NULL),
    ('45678901', 'PHY0101', 'Physics Fundamentals', 75, 2020, 2, NULL),
    ('56789012', 'BIO0101', 'Introduction to Biology', 85, 2021, 1, NULL),
    ('56789012', 'BIO0102', 'Genetics', 92, 2021, 2, NULL),
    ('67890123', 'CHM0101', 'General Chemistry', 78, 2020, 1, NULL),
    ('67890123', 'CHM0101', 'General Chemistry', 85, 2020, 2, NULL),
    ('78901234', 'ENG0101', 'English Composition', 90, 2021, 1, NULL),
    ('78901234', 'ENG0102', 'Literary Analysis', 88, 2021, 2, NULL),
    ('89012345', 'CSA0101', 'Introduction to Programming', 75, 2020, 1, NULL),
    ('89012345', 'CSA0101', 'Introduction to Programming', 82, 2020, 2, NULL),
    ('90123456', 'MTH0101', 'Calculus I', 85, 2021, 1, NULL),
    ('90123456', 'MTH0102', 'Calculus II', 78, 2021, 2, NULL),
    ('01234567', 'PHY0101', 'Physics Fundamentals', 70, 2020, 1, NULL),
    ('01234567', 'PHY0101', 'Physics Fundamentals', 65, 2020, 2, NULL),
    ('13579246', 'BIO0101', 'Introduction to Biology', 80, 2021, 1, NULL),
    ('13579246', 'BIO0102', 'Genetics', 88, 2021, 2, NULL),
    ('24681357', 'CHM0101', 'General Chemistry', 85, 2020, 1, NULL),
    ('24681357', 'CHM0101', 'General Chemistry', 92, 2020, 2, NULL),
    ('35792468', 'ENG0101', 'English Composition', 78, 2021, 1, NULL),
    ('35792468', 'ENG0102', 'Literary Analysis', 85, 2021, 2, NULL),
    ('46813579', 'CSA0101', 'Introduction to Programming', 92, 2020, 1, NULL),
    ('46813579', 'CSA0101', 'Introduction to Programming', 88, 2020, 2, NULL),
    ('57924680', 'MTH0101', 'Calculus I', 85, 2021, 1, NULL),
    ('57924680', 'MTH0102', 'Calculus II', 92, 2021, 2, NULL),
    ('68035791', 'PHY0101', 'Physics Fundamentals', 75, 2020, 1, NULL),
    ('68035791', 'PHY0101', 'Physics Fundamentals', 80, 2020, 2, NULL),
    ('79146802', 'BIO0101', 'Introduction to Biology', 88, 2021, 1, NULL),
    ('79146802', 'BIO0102', 'Genetics', 90, 2021, 2, NULL),
    ('80257913', 'CHM0101', 'General Chemistry', 82, 2020, 1, NULL),
    ('80257913', 'CHM0101', 'General Chemistry', 88, 2020, 2, NULL),
    ('91368024', 'ENG0101', 'English Composition', 85, 2021, 1, NULL),
    ('91368024', 'ENG0102', 'Literary Analysis', 92, 2021, 2, NULL),
    ('02479135', 'CSA0101', 'Introduction to Programming', 78, 2020, 1, NULL),
    ('02479135', 'CSA0101', 'Introduction to Programming', 85, 2020, 2, NULL),
    ('24680246', 'MTH0101', 'Calculus I', 92, 2021, 1, NULL),
    ('24680246', 'MTH0102', 'Calculus II', 88, 2021, 2, NULL),
    ('46802468', 'PHY0101', 'Physics Fundamentals', 75, 2020, 1, NULL),
    ('46802468', 'PHY0101', 'Physics Fundamentals', 82, 2020, 2, NULL),
    ('68024680', 'BIO0101', 'Introduction to Biology', 88, 2021, 1, NULL),
    ('68024680', 'BIO0102', 'Genetics', 85, 2021, 2, NULL),
    ('79146802', 'CSA0101', 'Introduction to Programming', 90, 2020, 1, NULL),
    ('79146802', 'CSA0101', 'Introduction to Programming', 88, 2020, 2, NULL),
    ('80257913', 'MTH0101', 'Calculus I', 85, 2021, 1, NULL),
    ('80257913', 'MTH0102', 'Calculus II', 92, 2021, 2, NULL),
    ('91368024', 'PHY0101', 'Physics Fundamentals', 75, 2020, 1, NULL),
    ('91368024', 'PHY0101', 'Physics Fundamentals', 80, 2020, 2, NULL),
    ('02479135', 'BIO0101', 'Introduction to Biology', 88, 2021, 1, NULL),
    ('02479135', 'BIO0102', 'Genetics', 90, 2021, 2, NULL),
    ('24680246', 'CHM0101', 'General Chemistry', 82, 2020, 1, NULL),
    ('24680246', 'CHM0101', 'General Chemistry', 88, 2020, 2, NULL),
    ('46802468', 'ENG0101', 'English Composition', 85, 2021, 1, NULL),
    ('46802468', 'ENG0102', 'Literary Analysis', 92, 2021, 2, NULL),
    ('68024680', 'CSA0101', 'Introduction to Programming', 78, 2020, 1, NULL),
    ('68024680', 'CSA0101', 'Introduction to Programming', 85, 2020, 2, NULL);
