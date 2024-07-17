import mysql.connector
import time

class populate_DB:
    def __del__(self):
        self.mydb.close()

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root",
            database="DiBot"
        )
        self.mydb.autocommit = True


    def Teachers(self):
        cursor = self.mydb.cursor()
        with open('populate_teachers_data.sql','r') as file:
            result_iterator = cursor.execute(file.read(), multi=True)
        self.mydb.close()

    def Courses(self):
        cursor = self.mydb.cursor()
        with open('populate_courses_data.sql','r') as file:
            result_iterator = cursor.execute(file.read(), multi=True)
        cursor.close()
        self.mydb.close()

    def RequiredCourses(self):
        cursor = self.mydb.cursor()
        with open('populate_required_courses_data.sql','r') as file:
            result_iterator = cursor.execute(file.read(), multi=True)
        cursor.close()
        self.mydb.close()

if __name__ == "__main__":
    populate_DB().Teachers()
    time.sleep(2)
    populate_DB().Courses()
    time.sleep(2)
    populate_DB().RequiredCourses()