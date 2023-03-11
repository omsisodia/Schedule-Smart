# Importing necessary libraries
import random
import numpy as np
import math

# Taking inputs from the user
days = int(input("Enter the number of days in a week: "))
hours = int(input("Enter the number of Hours in a day: "))
tot_sub = int(input("Enter total subjects in semester: "))


d = 0
lst = []
# Adding subjects and frequency of classes
for i in range(0, tot_sub):
    sub = input("Enter name of the subject :")
    f = int(input("Enter number of classes in a week :"))
    d = d + f
    for i in range(0, f):
        lst.append(sub)

# Filling the empty spaces with '?'
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
        for e in range(days):
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

