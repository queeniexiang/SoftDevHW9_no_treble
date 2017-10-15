"""
Queenie Xiang
SoftDev1 pd7
HW09 - No Treble 
2017-10-15
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f = "students_courses.db"
db = sqlite3.connect(f) 
c = db.cursor() 

courses = csv.DictReader(open("courses.csv"))
students = csv.DictReader(open("peeps.csv"))

#Create the Students table with columns ID, Name, Age 
command_create = "CREATE TABLE Students (ID INTEGER, Name TEXT, Age INTEGER)"
c.execute(command_create) 

#Iterating through the dictionary created from peeps.csv
for row in students:
    #Grabs ID of student
    ID = int(row['id'])

    #Grabs name of student 
    name = str(row['name'])

    #Grabs age of student 
    age = int(row['age'])

    #print("Student ID: %d, Name: %s, Age: %d" % (ID, name, age))

    #Insert obtained info into the table 
    c.execute("INSERT INTO Students VALUES (?, ?, ?)", (ID, name, age))

#Create the Courses table with columns ID, (course) Code, (Mark of the course)Grade 
command_create = "CREATE TABLE Courses (ID INTEGER, Code TEXT, Grade INTEGER)"
c.execute(command_create)

#Iterating through the dictionary created from courses.csv
for row in courses:
    #Grabs ID of student 
    ID = int(row['id'])

    #Grabs course that a student is taking 
    code = str(row['code'])

    #Grabs mark/grade a student is receiving 
    mark = int(row['mark'])

    #print("Student ID: %d, Name: %s, Age: %d" % (ID, name, age))

    #Insert obtained info into the table  
    c.execute("INSERT INTO Courses VALUES (?, ?, ?)", (ID, code, mark))

    
db.commit() #save changes
db.close()  #close database

