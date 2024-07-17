# from auxiliaries_functions import convert_to_cap_greek, LessonsECTS, english_lessons
# from dictionaries import Lessons_ECTS, Map_English_Greek_Lessons
import mysql.connector
from config.faq import questions as faq
from config.course_questions import questions as course_entity_questions

class IntentResponse: 

  @staticmethod 
  def _select_query(query):
    mydb = mysql.connector.connect(
      host="localhost", 
      user="root", 
      password="root",
      database="DiBot"
    )
    # mydb.autocommit = True
    cursor = mydb.cursor()
    cursor.execute(query, multi=True)
    results = cursor.fetchall()
    cursor.close()
    mydb.close()
    return results

  def hello(entity):
    return "Hello, how can I help you with?"
  
  def goodbye(entity):
    return "At your disposal. Goodbye!"

  def university_location(entity):
    return "Your university is located here: " + \
    "https://www.google.com/maps/place/Department+of+Informatics+and+Telecommunications/@37.968141,23.7643221,17"


  def general_courses_info(entity):
    return "Every information that you need about the courses in this " + \
    "university can be found here: " + \
    "https://www.di.uoa.gr/studies/undergraduate/courses (in Greek)" + \
    "or here https://www.di.uoa.gr/en/studies/undergraduate/courses " + \
    "(in English)"


  def university_official_site(entity):
    return "University site: https://www.di.uoa.gr/ (in Greek) " + \
    "https://www.di.uoa.gr/en (in English)"


  def usp_pps(entity):
    return "Every information that you need to know about the " + \
    "Structure of the Undergraduate Study Program (USP) can be found " + \
    "here: https://www.di.uoa.gr/studies/undergraduate/student-guide " + \
    "(in Greek)  or here " + \
    "https://www.di.uoa.gr/en/studies/undergraduate/student-guide " + \
    "(in English)\n" + \
    "For the year 2022 - 2023 you can find it here:" + \
    "https://www.di.uoa.gr/sites/default/files/documents/ODIGOS_SPOYDWN_DIT_EKPA_2022-23.pdf" 

  def questions_help(entity):
    return faq
  
  def followup_questions(entity):
    return course_entity_questions

  def courses_type(entity):
    query = "select type from courses group by type;"
    types = IntentResponse._select_query(query)
    response = "The courses are distinguished to the following types:\n"
    for (courseType,) in types:
      response += courseType + "\n"
    return response
    
  def compulsory_courses(entity):
    query = "select name from courses where type = 'Compulsory courses (YM)';"
    compulsory_courses = IntentResponse._select_query(query)
    response = "The following courses are compulsory:\n"
    for (course,) in compulsory_courses:
      response += course + "\n"
    return response

  def track_compulsory_courses(entity):
    query = "select name from courses where type = 'Track Compulsory courses (EYM)';"
    track_compulsory_courses = IntentResponse._select_query(query)
    response = "The following courses are track compulsory:\n"
    for (course,) in track_compulsory_courses:
      response += course + "\n"
    return response

  def elective_specialization_courses(entity):
    query = "select name from courses where type = 'Elective Specialization courses (ΠΜ-E)';"
    elective_specialization_courses = IntentResponse._select_query(query)
    response = "The following courses are elective specialization:\n" 
    for (course,) in elective_specialization_courses:
      response += course + "\n"
    return response

  def project_courses(entity):
    query = "select name from courses where type = 'Project';"
    project_courses = IntentResponse._select_query(query)
    response = "The following courses are project:\n"
    for (course,) in project_courses:
      response += course + "\n"
    return response

  def optional_laboratory_courses(entity):        
    query = "select name from courses where type = 'Optional Laboratory courses (EP)';"
    optional_laboratory_courses = IntentResponse._select_query(query)
    response = "The following courses are optional laboratory:\n"
    for (course,) in optional_laboratory_courses:
      response += course + "\n"
    return response

  def general_education(entity):
    query = "select name from courses where type = 'General Education (ΓΠ)';"
    general_education = IntentResponse._select_query(query)
    response = "The following courses are general education:\n"
    for (course,) in general_education:
      response += course + "\n"
    return response

  def thesis_internship(entity):
    return "The curriculum requires you to get 16 ECTS by carrying out Thesis and/or Internship, completing them in a minimum time of one year." + \
    "The Thesis is consisted of the courses Thesis I, Thesis II and the Internship of Internship I, Internship II." + \
    "You should choose between the 4 following cases: \n Thesis I + Thesis II \n Internship I + Internship II \n Thesis I + Internship II \n " + \
    "Internship I + Thesis II\nYou can get more information here: https://www.di.uoa.gr/studies/undergraduate/student-guide"

  def total_ects(entity):
    return "You need to collect 240 ECTS to get a degree."

  def total_courses(entity):
    return "You need to pass 39-42 courses to get a degree (Thesis/Internship are included)."

  def schedules(entity):
    return "All the schedules can be found here: https://www.di.uoa.gr/en/studies/undergraduate/schedules"

  def secretary_info(entity):
    return " The secretaries for undergraduate issues and their contact information are the following:" + \
    "Bourogianni Panagiota, secret@di.uoa.gr, 210 7275173" + \
    "Kasimati Athanasia, akasim@di.uoa.gr, secretary office - basement, 210 7275338" + \
    "Loupa Kity,  loupa@di.uoa.gr,  secretary office - basement, 210 7275154"

  def average_grade(entity):
    return "Access to such sensitive data is protected for privacy reasons.\n But you can calculate it by solving the following type:\n" + \
    "sum(M(i) * B(i)) / sum(M(i))\n" + \
    "where M(i): ECTS for the specific course, B(i): grade for the specific course\n" + \
    "You can find more information here: https://www.di.uoa.gr/sites/default/files/documents/ODIGOS_SPOYDWN_DIT_EKPA_2023-24.pdf"

  def are_required_courses(entity):
    query = "select c2.name, group_concat(c.name SEPARATOR ' + ') from courses as c inner join required_courses as r on c.id=r.course_id inner join courses as c2 on c2.id=r.course_required_id where r.requirement_status = 'required' group by c2.name order by c2.semester, c2.name;"
    required_courses = IntentResponse._select_query(query)
    response = "\n"
    for (course_name,required_course_name,) in required_courses:
      response += "- " + course_name + ": " + required_course_name + "\n"
    return response

  def have_recommended_courses(entity):
    query = "select c.name, c2.name from courses as c inner join required_courses as r on c.id=r.course_id inner join courses as c2 on c2.id=r.course_required_id where r.requirement_status = 'recommended' order by c.semester, c.name;"
    recommended_courses = IntentResponse._select_query(query)
    response = "\n"
    for (course_name,recommended_course_name,) in recommended_courses:
      response += "- " + course_name + ": " + recommended_course_name + "\n"
    return response

  def are_recommended_courses(entity):
    query = "select c2.name, group_concat(c.name SEPARATOR ' + ') from courses as c inner join required_courses as r on c.id=r.course_id inner join courses as c2 on c2.id=r.course_required_id where r.requirement_status = 'recommended' group by c2.name order by c2.semester, c2.name;"
    recommended_courses = IntentResponse._select_query(query)
    response = "\n"
    for (course_name,recommended_course_name,) in recommended_courses:
      response += "- " + course_name + ": " + recommended_course_name + "\n"
    return response

  def total_teachers(entity):
    query = "select last_name, first_name, gender, title from teachers;"
    teachers = IntentResponse._select_query(query)
    response = "The staff of the university is the following:\n"
    for (last_name, first_name, gender, title,) in teachers:
      if gender == 'F':
        response += "Mrs. "
      else:
        response += "Mr. "
      response += last_name + " (" + title + ")" + "\n"
    return response

  def recent_announcements_days(entity):
    if entity == '0':
      return "The aren't any announcements."
    query = "select c.name, ea.announcement_text, ea.announcement_date from eclass_announcements as ea inner join courses as c on ea.course_id = c.id where ea.announcement_date >= DATE_SUB(NOW(), INTERVAL {} DAY);".format(int(entity))
    recent_announcements = IntentResponse._select_query(query)
    response = "The announcements the last {} days are:\n".format(entity)
    for (name,announcement,date,) in recent_announcements:
      response += name + ': ' + announcement + ' announced on ' + date + "\n"
    if not recent_announcements: 
      response = "There aren't any announcements." 
    return response

  def courses_code_semester(entity):
    if entity == '':
      return "At your question you should add the semester you are interested to."
    query = "select name, code, semester from courses where semester = '{}';".format(entity)
    codes = IntentResponse._select_query(query)
    response = "The courses and theirs codes that are taught in the {} semester are:\n".format(entity)
    for (name,code,semester,) in codes:
      response += name + ': ' + code + "\n"
    if not codes: 
      response = "The semesters are 8." 
    return response

  def courses_semester(entity):
    if entity == '':
      return "At your question you should add the semester you are interested to."
    query = "select name, semester from courses where semester = '{}';".format(entity)
    courses = IntentResponse._select_query(query)
    response = "The courses that are taught in the {} semester are:\n".format(entity)
    for (name,semester,) in courses:
      response += name + "\n"
    if not courses: 
      response = "The semesters are 8." 
    return response

  def have_required_courses(entity):
    if entity == '':
      return "At your question you should add the semester you are interested to."
    query = "select c.name, c2.name from courses as c inner join required_courses as r on c.id=r.course_id inner join courses as c2 on c2.id=r.course_required_id where r.requirement_status = 'required' and c. semester = '{}' order by c.semester, c.name;".format(entity)
    required_courses = IntentResponse._select_query(query)
    if int(entity[0]) < 5:
      return "The courses of the first two years don't have required courses."
    response = "The courses of the {} semester that have required courses and their required courses are:\n".format(entity)
    for (course_name,required_course_name,) in required_courses:
      response += "- " + course_name + ": " + required_course_name + "\n"
    if not required_courses: 
      response = "The semesters are 8." 
    return response

  def ects_semester(entity):
    if entity == '':
      return "At your question you should add the semester you are interested to."
    query = "select name, ects from courses where semester = '{}';".format(entity)
    courses_ects = IntentResponse._select_query(query)
    response = "The courses of the {} semester with their ECTS are the following:\n".format(entity)
    for (name,ects,) in courses_ects:
      response += name + ": " + str(ects) + "\n"
    if not courses_ects:
      response = "The semesters are 8." 
    return response 

  def teachers_semester(entity):
    if entity == '':
      return "At your question you should add the semester you are interested to."
    query = "select c.name,t.first_name, t.last_name, t.gender, t.title, t2.first_name, t2.last_name,t2.gender, t2.title from courses as c  inner join teachers as t on c.teacher_id=t.id left join teachers as t2 on c.second_teacher_id=t2.id where c.semester= '{}';".format(entity)
    courses_teachers = IntentResponse._select_query(query)
    response = "I can help you only with the teachers that are members of our department.\n The teachers and their courses on the {} semester are:\n".format(entity)
    for (course, first_name, last_name, gender, title, first_name_2, last_name_2, gender_2, title_2,) in courses_teachers:
      if title == 'laboratory teaching staff':
        if gender == 'F':
          title_teacher = "Mrs"
        else:
          title_teacher = "Mr"
      else:
        title_teacher = "The " + title
      response += title_teacher + " " + first_name + " " + last_name + " "
      if last_name_2:
        response += "and "
        if title_2 == 'laboratory teaching staff':
          if gender_2 == 'F':
            title_teacher = "mrs"
          else:
            title_teacher = "mr"
        else:
          title_teacher = "the " + title_2
        response += title_teacher + " " + first_name_2 + " " + last_name_2 + " teach "
      else:
        response += "teaches "
      response += course + "\n"
    if not courses_teachers: 
      response = "The semesters are 8." 
    return response    

  def ects_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, ects from courses where name = '{}';".format(entity)
    course_ects = IntentResponse._select_query(query)
    for (name,ects,) in course_ects:
      response = "The ECTS of the course " + name + " are " + str(ects)
    if not course_ects:
      response = "The course is not taught in the department." 
    return response

  def grade_course(entity):
    return "Access to such sensitive data is protected for privacy reasons.\n" + \
    "For questions about your grades you can check the website: https://my-studies.uoa.gr/Secr3w/connect.aspx"

  def staff_course(entity):
    # import ipdb; ipdb.set_trace()
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select c.name,t.first_name, t.last_name, t.gender, t.title, t2.first_name, t2.last_name,t2.gender, t2.title from courses as c  inner join teachers as t on c.teacher_id=t.id left join teachers as t2 on c.second_teacher_id=t2.id where c.name = '{}';".format(entity)
    course_teacher = IntentResponse._select_query(query)
    for (name, first_name, last_name, gender, title, first_name_2, last_name_2, gender_2, title_2,) in course_teacher:
      if last_name:
        response = "The course " + name + " is taught by "
        if title == 'laboratory teaching staff':
          if gender == 'F':
            title_teacher = "Mrs"
          else:
            title_teacher = "Mr"
        else:
          title_teacher = "the " + title
        response += title_teacher + " " + first_name + " " + last_name + " "
      if last_name_2:
        response += "and "
        if title_2 == 'laboratory teaching staff':
          if gender_2 == 'F':
            title_teacher = "Mrs "
          else:
            title_teacher = "Mr "
        else:
          title_teacher = "the " + title_2
        response += title_teacher + " " + first_name_2 + " " + last_name_2
      if not last_name and not last_name_2:
        response = "The course is taught from a teacher that belongs to another department." 
    if not course_teacher:
      response = "The course is not taught in the department or the teacher is from another department." 
    return response

  def isRequired_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select c.name as course, c2.name as required from required_courses rc inner join courses c on c.id = rc.course_id left join courses c2 on c2.id = rc.course_required_id where c2.name = '{}' and rc.requirement_status = 'required'".format(entity)
    course_required = IntentResponse._select_query(query)
    response = ''
    for (course,is_required_course,) in course_required:
      response += "The " + is_required_course + " is required course for " + course + '\n'
    if not course_required:
      response = "The course is not taught in the department or it isn't a required course." 
    return response
  
  def hasRequired_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select c.name as course, c2.name as required from required_courses rc inner join courses c on c.id = rc.course_id left join courses c2 on c2.id = rc.course_required_id where c.name = '{}' and rc.requirement_status = 'required';".format(entity)
    course_required = IntentResponse._select_query(query)
    response = ''
    for (course,has_required_course,) in course_required:
      response += "The " + course + " has required course the course " + has_required_course + '\n'
    if not course_required:
      response = "The course is not taught in the department or it doesn't have any required courses." 
    return response    

  def isRecommended_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select c.name as course, c2.name as recommended from required_courses rc inner join courses c on c.id = rc.course_id left join courses c2 on c2.id = rc.course_required_id where c2.name = '{}' and rc.requirement_status = 'recommended';".format(entity)
    course_recommended = IntentResponse._select_query(query)
    response = ''
    for (course,is_recommended_course,) in course_recommended:
      response += "The " + is_recommended_course + " is recommended course for " + course + '\n'
    if not course_recommended:
      response = "The course is not taught in the department or it is't a recommended course." 
    return response

  def hasRecommended_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select c.name as course, c2.name as recommended from required_courses rc inner join courses c on c.id = rc.course_id left join courses c2 on c2.id = rc.course_required_id where c.name = '{}' and rc.requirement_status = 'recommended';".format(entity)
    course_recommended = IntentResponse._select_query(query)
    response = ''
    for (course,has_recommended_course,) in course_recommended:
      response += "The " + course + " has required course the course " + has_recommended_course + '\n'
    if not course_recommended:
      response = "The course is not taught in the department or it doesn't have any recommended courses." 
    return response   

  def type_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, type from courses where name = '{}';".format(entity)
    course = IntentResponse._select_query(query)
    for (name,course_type,) in course:
      response = "The course " + name + " belongs to " + course_type
    if not course:
      response = "The course is not taught in the department." 
    return response

  def announcements_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select an.announcement_text, date(an.announcement_date) from eclass_announcements an inner join courses c on an.course_id = c.id where c.name = '{}';".format(entity)
    announcement = IntentResponse._select_query(query)
    if not announcement:
      response = "The course {} has no announcements so far." .format(entity)
    else:
      response = "The announcements of {} and their dates are:\n" .format(entity)
    for (text,date,) in announcement:
      response += text + ' (' + str(date) + ')' + '\n'
    return response    

  def semester_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, semester from courses where name = '{}';".format(entity)
    course_semester = IntentResponse._select_query(query)
    for (name,semester,) in course_semester:
      response = "The course " + name + " belongs to " + str(semester) + " semester."
    if not course_semester:
      response = "The course is not taught in the department." 
    return response

  def code_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, code from courses where name = '{}';".format(entity)
    course_code = IntentResponse._select_query(query)
    for (name,code,) in course_code:
      response = "The code of the course " + name + " is " + code
    if not course_code:
      response = "The course is not taught in the department." 
    return response

  def website_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, link from courses where name = '{}';".format(entity)
    course_website = IntentResponse._select_query(query)
    for (name,link,) in course_website:
      if link:
        response = "The link of the course " + name + " is: " + link
      else:
        response = "The course " + name + " doesn't have a website link." 
    if not course_website:
      response = "The course is not taught in the department." 
    return response
    
  def eclass_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, eclass_link from courses where name = '{}';".format(entity)
    course_eclass = IntentResponse._select_query(query)
    for (name,link,) in course_eclass:
      if link:
        response = "The e-class link of the course " + name + " is: " + link
      else:
        response = "The course " + name + " doesn't have e-class link."    
    if not course_eclass:
      response = "The course is not taught in the department." 
    return response

  def theoryHours_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, theory_class_hours from courses where name = '{}';".format(entity)
    course_theory = IntentResponse._select_query(query)
    for (name,theory,) in course_theory:
      if theory:
        response = "The hours of theory of the course " + name + " are " + str(theory)
      else:
        response = "The course " + name + " doesn't include theory hours."
    if not course_theory:
      response = "The course is not taught in the department." 
    return response

  def seminarHours_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, seminar_class_hours from courses where name = '{}';".format(entity)
    course_seminar = IntentResponse._select_query(query)
    for (name,seminar,) in course_seminar:
      if seminar:
        response = "The hours of seminar of the course " + name + " are " + str(seminar)
      else:
        response = "The course " + name + " doesn't include seminar hours."
    if not course_seminar:
      response = "The course is not taught in the department." 
    return response

  def laboratoryHours_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    query = "select name, laboratory_class_hours from courses where name = '{}';".format(entity)
    course_laboratory = IntentResponse._select_query(query)
    for (name,laboratory,) in course_laboratory:
      if laboratory:
        response = "The hours of laboratory of the course " + name + " are " + str(laboratory)
      else:
        response = "The course " + name + " doesn't include laboratory hours."
    if not course_laboratory:
      response = "The course is not taught in the department." 
    return response

  def totalTeachingHours_course(entity):
    if entity == '':
      return "please specify the course you would like to learn about and rephrase your question."
    total_hours = 0
    query = "select theory_class_hours from courses where name = '{}';".format(entity)
    theory_hours = IntentResponse._select_query(query)
    for (hour,) in theory_hours:
      if hour:
        total_hours += int(hour)
    query = "select seminar_class_hours from courses where name = '{}';".format(entity)
    seminar_hours = IntentResponse._select_query(query) 
    for (hour,) in seminar_hours:
      if hour:
        total_hours += int(hour)
    query = "select laboratory_class_hours from courses where name = '{}';".format(entity)
    laboratory_hours = IntentResponse._select_query(query) 
    for (hour,) in laboratory_hours:
      if hour:
        total_hours += int(hour)
    response = "The total hours of the course " + entity + " per week are " + str(total_hours) 
    if total_hours == 0:
      response = "The course is not taught in the department." 
    return response

  def contact_teacher(entity):
    if entity == '':
      return "please specify the teacher you would like to learn about and rephrase your question."
    query = "select telephone,email,first_name,last_name,gender,title from teachers where last_name = '{}';".format(entity)
    teacher_contact = IntentResponse._select_query(query)
    for (telephone,email,first_name,last_name,gender,title,) in teacher_contact:
      if last_name:
        if title == 'laboratory teaching staff':
          if gender == 'F':
            title_teacher = "mrs"
          else:
            title_teacher = "mr"
        else:
          title_teacher = "the " + title
        response = "The contact details of " + title_teacher + " " + first_name + " " + last_name + " are: " + str(telephone) + ", " + email
    if not teacher_contact:
      response = "This teacher isn't teaching in the department of Informatics and Telecommuunications." 
    return response
 
  def subject_teacher(entity):
    if entity == '':
      return "please specify the teacher you would like to learn about and rephrase your question."
    query = "select c.name,t.first_name, t.last_name, t.gender, t.title, t2.first_name, t2.last_name,t2.gender, t2.title from courses as c  inner join teachers as t on c.teacher_id=t.id left join teachers as t2 on c.second_teacher_id=t2.id where t.last_name = '{last_name1}' or t2.last_name = '{last_name2}';".format(last_name1=entity,last_name2=entity)
    teacher_subject = IntentResponse._select_query(query)
    
    if not teacher_subject:
      return "This teacher isn't teaching in the department of Informatics and Telecommunications."     
    
    courses_taught = []
    for (name,first_name,last_name,gender,title,first_name2,last_name2,gender2,title2) in teacher_subject:
      if last_name or last_name2:
        if last_name == entity: 
          if title == 'laboratory teaching staff':
            if gender == 'F':
              title_teacher = "mrs"
            else:
              title_teacher = "mr"
          else:
            title_teacher = "the " + title
        if last_name2 == entity: 
          if title2 == 'laboratory teaching staff':
            if gender2 == 'F':
              title_teacher = "mrs"
            else:
              title_teacher = "mr"
          else:
            title_teacher = "the " + title2
        courses_taught.append(name)

    if len(courses_taught) > 1:
        response = "The courses that " + title_teacher + " " + first_name + " " + last_name + " is teaching are: "
    else:
        response = "The course that " + title_teacher + " " + first_name + " " + last_name + " is teaching is: "
    response += ", ".join(courses_taught)

    return response

  def office_teacher(entity):
    if entity == '':
      return "please specify the teacher you would like to learn about and rephrase your question."
    query = "select office,first_name,last_name,gender,title from teachers where last_name = '{}';".format(entity)
    teacher_office = IntentResponse._select_query(query)
    for (office,first_name,last_name,gender,title,) in teacher_office:
      if last_name:
        if title == 'laboratory teaching staff':
          if gender == 'F':
            title_teacher = "mrs"
          else:
            title_teacher = "mr"
        else:
          title_teacher = "the " + title
        response = "The office of " + title_teacher + " " + first_name + " " + last_name + " is " + office
    if not teacher_office:
      response = "This teacher isn't teaching in the department of Informatics and Telecommuunications." 
    return response

  def website_teacher(entity):
    if entity == '':
      return "please specify the teacher you would like to learn about and rephrase your question."
    query = "select personal_website,first_name,last_name,gender,title from teachers where last_name = '{}';".format(entity)
    teacher_website = IntentResponse._select_query(query)
    for (personal_website,first_name,last_name,gender,title,) in teacher_website:
      if last_name:
        if title == 'laboratory teaching staff':
          if gender == 'F':
            title_teacher = "mrs"
          else:
            title_teacher = "mr"
        else:
          title_teacher = "the " + title
        if personal_website == '-':
          response = title_teacher.capitalize() + " " + first_name + " " + last_name + " doesn't have a website."
        else:
          response = "The personal website of " + title_teacher + " " + first_name + " " + last_name + " is: " + personal_website
    if not teacher_website:
      response = "This teacher isn't teaching in the department of Informatics and Telecommuunications." 
    return response