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

    def EclassAnnouncements(self):
        cursor = self.mydb.cursor()
        with open('populate_eclass_announcements_data.sql','r') as file:
            result_iterator = cursor.execute(file.read(), multi=True)
        cursor.close()
        self.mydb.close()


if __name__ == "__main__":
    populate_DB().EclassAnnouncements()
