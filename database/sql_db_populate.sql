-- Insert records into Students table
INSERT INTO Students (student_id, fname, lname, email, mobile, course_code, units_attempted, units_completed, course_status) VALUES
('S001', 'John', 'Doe', 'john.doe@example.com', '123-456-7890', 'C001', 4, 3, 'Active'),
('S002', 'Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'C002', 5, 5, 'Active'),
('S003', 'Michael', 'Johnson', 'michael.johnson@example.com', '456-789-0123', 'C001', 6, 4, 'Active'),
('S004', 'Emily', 'Brown', 'emily.brown@example.com', '789-012-3456', 'C003', 7, 7, 'Active'),
('S005', 'David', 'Martinez', 'david.martinez@example.com', '234-567-8901', 'C002', 8, 6, 'Active'),
('S006', 'Sophia', 'Garcia', 'sophia.garcia@example.com', '890-123-4567', 'C004', 9, 9, 'Active'),
('S007', 'James', 'Lopez', 'james.lopez@example.com', '345-678-9012', 'C003', 10, 8, 'Active'),
('S008', 'Olivia', 'Hernandez', 'olivia.hernandez@example.com', '012-345-6789', 'C001', 11, 10, 'Active'),
('S009', 'William', 'Smith', 'william.smith@example.com', '901-234-5678', 'C002', 12, 11, 'Active'),
('S010', 'Amelia', 'Jones', 'amelia.jones@example.com', '567-890-1234', 'C004', 13, 12, 'Active');

-- Insert records into Courses table
INSERT INTO Courses (course_code, course_title, year_created, year_cancelled, coordinator_name, coordinator_email, coordinator_mobile) VALUES
('C001', 'Computer Science', 2010, NULL, 'Dr. Smith', 'dr.smith@example.com', '123-456-7890'),
('C002', 'Engineering', 2012, NULL, 'Dr. Johnson', 'dr.johnson@example.com', '987-654-3210'),
('C003', 'Mathematics', 2015, NULL, 'Dr. Brown', 'dr.brown@example.com', '789-012-3456'),
('C004', 'Business Administration', 2018, NULL, 'Dr. Garcia', 'dr.garcia@example.com', '890-123-4567'),
('C005', 'Physics', 2020, NULL, 'Dr. Martinez', 'dr.martinez@example.com', '234-567-8901'),
('C006', 'Chemistry', 2013, NULL, 'Dr. Lopez', 'dr.lopez@example.com', '345-678-9012'),
('C007', 'Biology', 2011, NULL, 'Dr. Hernandez', 'dr.hernandez@example.com', '012-345-6789'),
('C008', 'History', 2014, NULL, 'Dr. Williams', 'dr.williams@example.com', '901-234-5678'),
('C009', 'English Literature', 2016, NULL, 'Dr. Brown', 'dr.brown@example.com', '789-012-3456'),
('C010', 'Economics', 2019, NULL, 'Dr. Johnson', 'dr.johnson@example.com', '987-654-3210');

-- Insert records into StudentUnits table
INSERT INTO StudentUnits (student_id, unit_code, unit_title, unit_score, unit_grade, year_attempted, semester_attempted, note) VALUES
('S001', 'U001', 'Introduction to Programming', 85, 'B', 2022, 1, 'Good performance'),
('S002', 'U002', 'Database Management', 92, 'A', 2023, 2, 'Excellent work'),
('S003', 'U003', 'Web Development', 78, 'C', 2021, 1, 'Needs improvement'),
('S004', 'U004', 'Software Engineering', 88, 'B+', 2020, 2, 'Solid performance'),
('S005', 'U005', 'Data Structures', 95, 'A+', 2019, 1, 'Top performer'),
('S006', 'U006', 'Machine Learning', 80, 'B-', 2022, 2, 'Satisfactory'),
('S007', 'U007', 'Algorithms', 87, 'B+', 2023, 1, 'Good progress'),
('S008', 'U008', 'Computer Networks', 93, 'A', 2021, 2, 'Outstanding performance'),
('S009', 'U009', 'Operating Systems', 79, 'C+', 2020, 1, 'Average work'),
('S010', 'U010', 'Cybersecurity', 85, 'B', 2019, 2, 'Steady progress');