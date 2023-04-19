from django.shortcuts import render
import requests
from . import pool

def callindex(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def timetable(request):
    return render(request, 'timetable.html')

def program(request):
    return render(request, 'program.html')

def faculty(request):
    return render(request, 'faculty.html')

def subject(request):
    return render(request, 'subject.html')

def lecture(request):
    return render(request, 'lecture.html')

def lab(request):
    return render(request, 'lab.html')

def generate(request):
    return render(request, 'generate.html')

def output(request):
    return render(request, 'output.html')

def view_course(request):
    return render(request, 'view_course.html')

def view_faculty(request):
    return render(request, 'view_faculty.html')

def view_labRoom(request):
    return render(request, 'view_labRoom.html')

def view_lectureRoom(request):
    return render(request, 'view_lectureRoom.html')

def view_program(request):
    return render(request, 'view_program.html')



def loginadmin(request):
    username = request.POST["username"]
    password = request.POST["password"]

    print(username, password)

    dbe, cmd = pool.ConnectionPool()
    q = "select * from admin where username = '{}' and password = '{}'".format(username, password)
    cmd.execute(q)
    result = cmd.fetchone()
    dbe.close()
    print(result)
    if(result):
        return render(request, 'timetable.html', {"msg": ""})
    else:
        return render(request, 'login.html', {"msg": "Invalid Username or Password !", 'result' : result})


def callsignin(request):
    name = request.POST['name']
    email = request.POST['email']
    username = request.POST["username"]
    password = request.POST["password"]

    print(username, password)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO admin (name, email, username, password) VALUES ('{}', '{}', '{}', '{}')".format(name, email, username, password)
    cmd.execute(q)
    dbe.commit()
    # result = cmd.fetchone()
    dbe.close()
    # print(result)

    return render(request, 'login.html', {"msg": "Registration Successfull"})

def callprogram(request):
    programs = request.POST['programs']
    semesters = request.POST['semesters']

    print(programs, semesters)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO Program (Program_name, semester_id) VALUES ('{}', '{}')".format(programs, semesters)
    cmd.execute(q)
    dbe.commit()
    dbe.close()
    # print(result)

    return render(request, 'program.html', {"msg": "Program Added"})


def callsubjects(request):
    course = request.POST.get('course', False)
    course_n = request.POST.get('course_n', False)
    frequency = request.POST.get("frequency", False)
    program_name = request.POST.get("program_name", False)
    semester_id = request.POST.get("semester_id", False)
    s = int(semester_id)
    print(course, course_n, frequency, program_name, semester_id)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO courses (course_code, course_name, frequency, Program_name, semester_id) VALUES ('{}', '{}', '{}', '{}', '{}')".format(course, course_n, frequency, program_name, s)
    cmd.execute(q)
    dbe.commit()
    # result = cmd.fetchone()
    dbe.close()
    # print(result)

    return render(request, 'subject.html', {"msg": "Course Added"})

def callview_program(request):
    dbe, cmd = pool.ConnectionPool()
    q = "select * from timetable.Program"
    cmd.execute(q)
    dbe.commit()
    programs = cmd.fetchall()
    dbe.close()
    print(programs)

    return render(request, 'view_program.html', {"programs": programs})



def callview_course(request):

    dbe, cmd = pool.ConnectionPool()
    q = "select * from timetable.courses"
    cmd.execute(q)
    dbe.commit()
    courses = cmd.fetchall()
    dbe.close()
    print(courses)

    return render(request, 'view_course.html', {"courses": courses})


def calllecture(request):
    lecture_id = request.POST.get('lecture_id', False)
    lecture_capacity = request.POST.get('lecture_capacity', False)

    s = int(lecture_capacity)
    print(lecture_id, lecture_capacity)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO lecture (lecture_id, lecture_capacity) VALUES ('{}', '{}')".format(lecture_id, s)
    cmd.execute(q)
    dbe.commit()
    # result = cmd.fetchone()
    dbe.close()
    # print(result)
    return render(request, 'lecture.html', {"msg": "Lecture Room Added"})


def callview_lectureRoom(request):
    dbe, cmd = pool.ConnectionPool()
    q = "select * from timetable.lecture"
    cmd.execute(q)
    dbe.commit()
    lectures = cmd.fetchall()
    dbe.close()
    print(lectures)

    return render(request, 'view_lectureRoom.html', {"lectures": lectures})


def calllab(request):
    lab_id = request.POST.get('lab_id', False)
    lab_capacity = request.POST.get('lab_capacity', False)

    s = int(lab_capacity)
    print(lab_id, lab_capacity)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO Lab (Lab_id, Lab_capacity) VALUES ('{}', '{}')".format(lab_id, s)
    cmd.execute(q)
    dbe.commit()
    # result = cmd.fetchone()
    dbe.close()
    # print(result)
    return render(request, 'lab.html', {"msg": "Lab Room Added"})


def callview_labRoom(request):
    dbe, cmd = pool.ConnectionPool()
    q = "select * from timetable.Lab"
    cmd.execute(q)
    dbe.commit()
    labs = cmd.fetchall()
    dbe.close()
    print(labs)

    return render(request, 'view_labRoom.html', {"labs": labs})


def callfaculty(request):
    Professor_id = request.POST.get('Professor_id', False)
    Professor_name = request.POST.get('Professor_name', False)
    course_code = request.POST.get("course_code", False)
    Phone_number = request.POST.get("Phone_number", False)
    Email_ID = request.POST.get("Email_ID", False)
    s = int(Phone_number)
    print(Professor_id, Professor_name, course_code, Phone_number, Email_ID)

    dbe, cmd = pool.ConnectionPool()
    q = "INSERT INTO Professor (Professor_id, Professor_name, course_code, Phone_number, Email_ID) VALUES ('{}', '{}', '{}', '{}', '{}')".format(Professor_id, Professor_name, course_code, s, Email_ID)
    cmd.execute(q)
    dbe.commit()
    # result = cmd.fetchone()
    dbe.close()
    # print(result)

    return render(request, 'faculty.html', {"msg": "Faculty Added"})

def callview_faculty(request):

    dbe, cmd = pool.ConnectionPool()
    q = "select * from timetable.Professor"
    cmd.execute(q)
    dbe.commit()
    Professors = cmd.fetchall()
    dbe.close()
    print(Professors)

    return render(request, 'view_faculty.html', {"Professors": Professors})
