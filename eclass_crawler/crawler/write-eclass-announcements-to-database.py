import json
import mysql.connector

from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs

fullpath_filename = './announcements_data.json'
database_courses_path = '../db/populate_eclass_announcements_data.sql'


def _convert_to_datetime(date):
    date = date[2:-2]
    greek_months = {
        "Ιανουαρίου": "January",
        "Φεβρουαρίου": "February",
        "Μαρτίου": "March",
        "Απριλίου": "April",
        "Μαΐου": "May",
        "Ιουνίου": "June",
        "Ιουλίου": "July",
        "Αυγούστου": "August",
        "Σεπτεμβρίου": "September",
        "Οκτωβρίου": "October",
        "Νοεμβρίου": "November",
        "Δεκεμβρίου": "December",
    }
    
    greek_days = {
        "Δευτέρα": "Monday",
        "Τρίτη": "Tuesday",
        "Τετάρτη": "Wednesday",
        "Πέμπτη": "Thursday",
        "Παρασκευή": "Friday",
        "Σάββατο": "Saturday",
        "Κυριακή": "Sunday",
    }

    greek_timeslots = {
        'π.μ.': 'AM',
        'μ.μ.': 'PM'
    }

    recent_greek_dates = {
        'σήμερα': (datetime.today()).strftime("%A, %d %B %Y"),
        'χθες': (datetime.today() - timedelta(days=1)).strftime("%A, %d %B %Y"),
        'προχθές': (datetime.today() - timedelta(days=2)).strftime("%A, %d %B %Y")
    }

    for greek, english in greek_months.items():
        date = date.replace(greek, english)
    
    for greek, english in greek_days.items():
        date = date.replace(greek, english)
    
    for greek, english in greek_timeslots.items():
        date = date.replace(greek, english)

    for recent_greek_date in list(recent_greek_dates.keys()):
        if recent_greek_date in date:
            date = date.replace(recent_greek_date, recent_greek_dates[recent_greek_date])
            break
     
    date_format = "%A, %d %B %Y - %I:%M %p"

    return datetime.strptime(date, date_format)

def _post_process_announcement(announcement):
    clean_data_announcement = {}
    for k in announcement:
        data = None
        if k == 'text':
            data = announcement[k][0].strip()
        else:
            data = announcement[k].strip()

        if k == 'date':
            data = _convert_to_datetime(data)

        clean_data_announcement[k] = data
    return clean_data_announcement

def _get_courses():
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="root",
        database="DiBot"
    )
    cursor = mydb.cursor()
    query = "SELECT id, eclass_link FROM courses WHERE eclass_link LIKE 'https://eclass.uoa.gr/courses/%'"
    cursor.execute(query)

    courses = {}
    for (id, eclass_link,) in cursor:
        code_lesson = None
        if eclass_link[-1] != '/':
            code_lesson = eclass_link.split('/')[-1]
        else:
            code_lesson = eclass_link.split('/')[-2]    
        courses[code_lesson] = id
    cursor.close()
    mydb.close()
    return courses

def _get_course_id_by_announcement_link(announcement_link, available_courses):
    parsed_url = urlparse(announcement_link)
    announcement_course = parse_qs(parsed_url.query)['course'][0]
    return available_courses[announcement_course]

def _generate_sql_announcements_inserts(data):
    courses = _get_courses()
    sql_string = ""
    for row in data:
        sql_string += """
INSERT IGNORE INTO eclass_announcements
(announcement_text, announcement_date, course_id)
VALUES (
'{announcement_text}', '{announcement_date}', {course_id}
);
        """.format(
            announcement_text=row['text'], announcement_date=row['date'],
            course_id = _get_course_id_by_announcement_link(row['announcement_link'], courses)
        )
    return sql_string

def generate_database_query():
    with open(fullpath_filename) as data_file:
        data = json.load(data_file)
        clean_data = []
        for announcement in data:
            clean_data.append(_post_process_announcement(announcement))

        sql_inserts = _generate_sql_announcements_inserts(clean_data)
        return sql_inserts

def write_eclass_announcements_to_database(query):
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="root",
        database="DiBot"
    )
    mydb.autocommit = True
    cursor = mydb.cursor()
    cursor.execute(query, multi=True)
    cursor.close()
    mydb.close()

if __name__ == "__main__":
    write_eclass_announcements_to_database(query = generate_database_query())