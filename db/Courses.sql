CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL UNIQUE,
    ects INT NOT NULL,
    semester INT NOT NULL,
    eclass_link VARCHAR(255),
    teacher_id INT,
    second_teacher_id INT,
    -- type VARCHAR(255) NOT NULL,
    type enum(
        'Compulsory courses (YM)',
        'Elective Specialization courses (ΠΜ-E)',
        'Optional Laboratory courses (EP)',
        'General Education (ΓΠ)',
        'Track Compulsory courses (EYM)',
        'Project'
    ),
    link VARCHAR(255),
    theory_class_hours INT,
    seminar_class_hours INT,
    laboratory_class_hours INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
    FOREIGN KEY (second_teacher_id) REFERENCES teachers(id)
) ENGINE=InnoDB CHARACTER SET=utf8;