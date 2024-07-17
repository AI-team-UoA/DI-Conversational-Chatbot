CREATE TABLE IF NOT EXISTS required_courses (
    course_id INT NOT NULL,
    course_required_id INT NOT NULL,
    requirement_status ENUM('required', 'recommended'), 
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (course_required_id) REFERENCES courses(id)
);