CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    telephone INT,
    email VARCHAR(255) UNIQUE,
    gender enum('M','F') NOT NULL,
    title enum(
        'assistant professor',
        'associate professor',
        'professor',
        'laboratory teaching staff'
    ) NOT NULL,
    office VARCHAR(255),
    personal_website VARCHAR(255)
) ENGINE=InnoDB CHARACTER SET=utf8;