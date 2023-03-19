# Importing necessary libraries
import mysql.connector
import pandas as pd
import numpy as np
import math
import random

# Connecting SQL with Python
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rakesh@1968",
    database = "TimeTable"
)
cur2 = mydb.cursor() #COURSES


print("Enter the Program: ")
Program = input()

print("Enter the Semester: ")
Semester = int(input())

cur2.execute(f"SELECT * FROM Courses WHERE semester_id = {Semester} AND Program_name = '{Program}'")

d = 0
lst = []

for row in cur2.fetchall():
    sub = row[0]
    freq = row[2]
    d = d + freq
    for i in range(0, freq):
        lst.append(sub)

if (d > 40):
    print("invalid input")
else:
    for i in range(0, 40 - d):
        ele = "?"
        lst.append(ele)


# adding inputs for lecture halls and batches
lecture = int(input("Enter number of lecture halls avilable: "))
num_batches = int(input("Enter the number of batches: "))

# Creating groups
group = math.ceil(num_batches/lecture)
print("Total groups formed for lectures: ",group)
print("\n \n")

# TIMETABLE CODE for lectures
# Defining Rows(time) and columns(days) of matrix
R = 8
C = 5
print("Timetable for each lecture hall \n")



for p in range(group):
    lst1 = []
    matrix = []
    m = []
    time = ["08:30-09:25       ", "09:30-10:25       ", "10:40-11:35       ", "11:40-12:35       ", "01:30-02:25       ", "02:25-03:30       ", "03:40-04:35       ", "04:35-05:30       "]
    
    # This loop runs R times, creating a row of the matrix by taking the first C items from the list lst,
    #  removing them from lst, and appending them to the list a. It then appends the list a to the list matrix.
    for i in range(R):
        a = []
        for j in range(C):
            item = lst[0]
            a.append(item)
            lst.remove(item)
            lst1.append(item)
        matrix.append(a)

        # These lines create a 2D numpy array m from the list matrix,
        #  and then transpose it to create a new array matrix1.
        m = np.array(matrix)
        matrix1 = m.T

        # This loop shuffles the elements in each row of matrix1 using the shuffle
        #  function from the random module, and then transposes
        for e in range(5):
            random.shuffle(matrix1[e])
        m1 = np.array(matrix1)
        matrix2 = m1.T

    # Printing the borders of timetable formed
    for m in range(40):
        lst.append(lst1[m])
    print("-----------Time Table ", end="")
    print(p + 1, end="")
    print("-----------")
    print("    TIME         MON       TUE      WED      THU      FRI")


    # Printing the matrix and forming a timetable
    for i in range(R):
        print(time[i], end="")
        for j in range(C):
            print(matrix2[i][j], end="         ")
        print()



