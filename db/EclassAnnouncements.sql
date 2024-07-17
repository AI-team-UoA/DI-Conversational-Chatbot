CREATE TABLE IF NOT EXISTS eclass_announcements (
    announcement_id INT AUTO_INCREMENT PRIMARY KEY,
    announcement_text VARCHAR(500),
    announcement_date DATETIME,
    course_id INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    UNIQUE (announcement_text, announcement_date, course_id)
);