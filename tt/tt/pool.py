import pymysql as mysql

def ConnectionPool():
    dbe =mysql.connect(host = "localhost", port = 3306, user = "root", password = "Rakesh@1968", db = "timetable")
    cmd = dbe.cursor()
    return (dbe, cmd)
