import json

fullpath_filename = 'courses_crawler/courses_crawler/spiders/data.json'
database_courses_path = '../db/populate_courses_data.sql'
database_required_courses_path = '../db/populate_required_courses_data.sql'

def post_process_course(course):
    clean_data_course = {}
    nullable_fields = [
        'theory_class_hours',
        'seminar_class_hours',
        'laboratory_class_hours'
    ]
    for k in course:
        if course[k]:
            if k in nullable_fields and course[k] == '-':
                clean_data_course[k] = 'NULL'
            else:
                clean_data_course[k] = course[k].strip()
    return clean_data_course

def generate_sql_courses_inserts(data):
    sql_string = ""
    primary_keys_inserted = {}
    current_primary_key = 1
    for row in data:
        primary_keys_inserted[row['name']] = current_primary_key
        sql_string += """
INSERT INTO courses
(code, name, ects, semester, eclass_link, teacher_id, type, link, theory_class_hours, seminar_class_hours, laboratory_class_hours)
VALUES (
'{code}', '{name}', {ects}, {semester}, {eclass_link}, {teacher_id},
'{type}', '{link}', {theory_class_hours}, {seminar_class_hours},{laboratory_class_hours}
);
        """.format(
            code=row['code'], name=row['name'], ects=row['ects'],
            semester=row['semester'][0:1],
            eclass_link="'" + row['eclass_link'] + "'" if 'eclass_link' in row.keys() else 'NULL',
            teacher_id='NULL', type=row['type'], link=row['link'],
            theory_class_hours=row['theory_class_hours'], 
            seminar_class_hours=row['seminar_class_hours'], 
            laboratory_class_hours=row['laboratory_class_hours']
        )
        current_primary_key += 1
    return (sql_string, primary_keys_inserted)

def generate_sql_required_courses_inserts(data, primary_keys):
    sql_string = ""
    for row in data:
        if 'required' in row:
            sql_string += """
INSERT INTO required_courses (course_id, course_required_id, requirement_status)
VALUES ({course_id}, {course_required_id}, 'required');
            """.format(
                course_id=primary_keys[row['name']],
                course_required_id=primary_keys[row['required']]
            )
        if 'recommended' in row:
            sql_string += """
INSERT INTO required_courses (course_id, course_required_id, requirement_status)
VALUES ({course_id}, {course_recommended_id}, 'recommended');
            """.format(
                course_id=primary_keys[row['name']],
                course_recommended_id=primary_keys[row['recommended']]
            )
    return sql_string

if __name__ == "__main__":
    with open(fullpath_filename) as data_file:
        data = json.load(data_file)
        clean_data = []
        for course in data:
            clean_data.append(post_process_course(course))

        (sql_inserts_courses, primary_keys_inserted) = generate_sql_courses_inserts(clean_data)
        # Generate Required courses insert
        sql_inserts_required_courses = \
        generate_sql_required_courses_inserts(clean_data, primary_keys_inserted)

    with open(database_courses_path, mode='w') as output_file:
        output_file.write(sql_inserts_courses)

    with open(database_required_courses_path, mode='w') as output_file:
        output_file.write(sql_inserts_required_courses)