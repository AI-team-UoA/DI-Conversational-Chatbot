import mysql.connector

class DB:
    def __del__(self):
        self.mydb.close()

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="root",
            database="DiBot"
        )

    def Teachers_TABLE(self):
        cursor = self.mydb.cursor()
        with open("Teachers.sql") as file:
            cursor.execute(file.read())
        cursor.close()

    def Courses_TABLE(self):
        cursor = self.mydb.cursor()
        with open("Courses.sql") as file:
            cursor.execute(file.read())
        cursor.close()

    def Required_Courses_TABLE(self):
        cursor = self.mydb.cursor()
        with open("RequiredCourses.sql") as file:
            cursor.execute(file.read())
        cursor.close()

    def Eclass_Announcements_TABLE(self):
        cursor = self.mydb.cursor()
        with open("EclassAnnouncements.sql") as file:
            cursor.execute(file.read())
        cursor.close()


if __name__ == "__main__":
    DB().Teachers_TABLE()
    DB().Courses_TABLE()
    DB().Required_Courses_TABLE()
    DB().Eclass_Announcements_TABLE()

