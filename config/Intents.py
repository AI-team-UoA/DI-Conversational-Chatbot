simple_intents = {
    'hello': [
        'Hello',
        'Can I ask a question?'
    ],
    'goodbye': [
        'Goodbye',
        'Ok. Thanks',
        'Bye',
        'Thank you'
    ],
    'university_location': [
        'Where is the location of university?',
        'Where is located the university?',
        'Where is the department located?'
    ],
    'general_courses_info': [
        'Where can I find more information about the courses?',
        'More information about the courses I can find?'
    ],
    'university_official_site': [
        'What is the site of the department?',
        'What is the department website?',
        'What is the university department s website?'
    ],
    'usp_pps': [
        'What is the curriculum?'
    ],
    'questions_help': [
        'What questions can I ask?',
        'help?'
    ],
    'followup_questions' :[
        'more questions?',
        'more?',
        'Can you please give me more info about the questions on courses?'
    ],
    'courses_type': [
        'What are the types of courses?',
        'In what types are the courses divided?'
    ],
    'compulsory_courses': [
        'Which courses are compulsory?'
    ],
    'track_compulsory_courses': [
        'Which courses are track compulsory?'
    ],
    'elective_specialization_courses':[
        'Which courses are elective specialization?'
    ],
    'project_courses': [
        'Which courses are Project?'
    ],
    'optional_laboratory_courses': [
        'Which courses are optional laboratory?'
    ],
    'general_education': [
        'Which courses are general education?'
    ],
    'thesis_internship': [
        'Do we need to carry out an internship or a thesis to get a degree?'
    ],
    'total_ects': [
        'How many ECTS do I need in total to get a degree?'
    ],
    'total_courses': [
        'How many courses do I need in total to get a degree?'
    ],
    'schedules': [
        'Where can I find the course schedule or the exam schedule?',
        'Where can I find the timetable of this semester?',
        'Where can I find the exam schedule of this semester?'
    ],
    'secretary_info': [
        'How can I reach the secretariat?',
        'How can I reach the secretary office?'
    ],
    'average_grade': [
        'What is my average grade?',
        'What is my grade point average (GPA)?'
    ],
    'are_required_courses': [
        'Which courses are required courses and in which ones?',
        'Which courses are required courses?'
    ],
    'have_recommended_courses': [
        'Which courses have recommended courses and which are they?',
        'Which courses have recommended courses?'
    ],
    'are_recommended_courses': [
        'Which courses are recommended courses, and in which ones?',
        'Which courses are recommended courses?'
    ],
    'total_teachers': [
        'Who are the teachers?'
    ],
}

simple_intents_with_entity_number = {
    'recent_announcements_days': [
        'Are there any recent announcements the last $number days?',
        'Is there any recent announcement the last $number days?'
    ],
    'courses_code_semester': [
        'What are the courses with their codes that are taught in the $number semester?',
        'What are the courses codes for the $number semester?',
    ],
    'courses_semester': [
        'What are the courses that are taught in the $number semester?',
        'What courses are offered in the $number semester?'
    ],
    'have_required_courses': [
        'Which courses from the $number semester have required courses and which are they?',
        'Which courses from the $number semester have required courses?'
    ],
    'ects_semester': [
        'What are the ects of the courses in the $number semester?'
    ],
    'teachers_semester': [
        'What are the courses of the $number semester and who are the teachers?',
        'Who are the teachers and the courses on $number semester?',
    ]
}

follow_up_intents_course = {
    'ects_course': [
        'How many ects does $course_name have?'
    ],
    'grade_course': [
        'What is my grade on $course_name?',
        'What are my grades on $course_name?'
    ],
    'staff_course': [
        'Who is the teacher on $course_name?'
    ]
}

follow_up_intents_course1 = {
    'isRequired_course': [
        'Is the $course_name a required course?',
        'Is the $course_name a required course? If so, in which courses?'
    ],
    'hasRequired_course': [
        'Does the $course_name have required courses?',
        'Does the $course_name have required courses?Does it have required courses?'
    ]
}

follow_up_intents_course2 = {
    'isRecommended_course': [
        'Is the $course_name a recommended course?',
        'Is the $course_name a recommended course? If so, in which courses?'
    ],
    'hasRecommended_course': [
        'Does the $course_name have recommended courses?',
        'Does the $course_name have recommended courses? If so, which one?'
    ]
}

follow_up_intents_course3 = {
    'type_course': [
        'Is the $course_name an obligatory course?',
        'Is the $course_name a compulsory course?',
        'Is the $course_name an elective specialization course?',
        'Is the $course_name a track compulsory course?',
        'Is the $course_name a general education course?',
        'Is the $course_name a Project course?',
        'Is the $course_name an optional laboratory course?',
        'What type of course is the $course_name?',

    ],
    'announcements_course': [
        'Does $course_name have any recent announcements?',
        'Does $course_name have any recent announcements and when they were released?'
    ]
}

follow_up_intents_course4 = {
    'semester_course': [
        'In what semester is $course_name offered?'
    ],
    'code_course': [
        'What is the course code for $course_name?'
    ]
}

follow_up_intents_course5 = {
    'website_course': [
        'What is the $course_name website?',
        'Does the $course_name have a website?'
    ],
    'eclass_course': [
        'What is the e-class link of $course_name?'
    ]
}

follow_up_intents_course6 = {
    'theoryHours_course': [
        'How many theory hours does $course_name have?'
    ],
    'seminarHours_course': [
        'How many seminar hours does $course_name have?'
    ]
}

follow_up_intents_course7 = {
    'laboratoryHours_course': [
        'How many laboratory hours does $course_name have?'
    ],
    'totalTeachingHours_course': [
        'How many teaching hours does $course_name have?',
        'How many total teaching hours does $course_name have?'
    ]
}

follow_up_intents_teacher = {
    'contact_teacher': [
        'What are the contact details of $teacher_name?',
        'What are $teacher_name contact details?'
    ],
    'subject_teacher': [
        'What courses are $teacher_name teaching?',
        'What courses is $teacher_name teaching?'
    ],
    'office_teacher':[
        'Which is the number of $teacher_name office?'
    ],
    'website_teacher':[
        'Do $teacher_name have personal website? If yes, which one?',
        'Does $teacher_name have personal website? If yes, which one?'
    ]
}