import sqlite3
import numpy as np
from tabulate import tabulate
con = sqlite3.connect("academicControl.db")
cursor = con.cursor()
role=""
data=[]
def ManageInfo1():

    while True:
        print("1. Add Instructor Info")
        print("2. Manage Instructor Info")
        print("3. Back to Main Menu")
        ch2=input("Enter your choice:")
        if(ch2==1):
            logid1 = input("Enter login id: ")
            name1 = input("Enter  name: ")
            prog1 = input("Enter Programid: ")
            add1 = input("Enter Address ")
            r1='I'
            query1=("INSERT INTO tb_instructor(login_id,name,program_id,address)values('" + logid1 + "','" + name1 + "','" + prog1 + "','" + add1 + "');")
            cursor.execute(query1)
            que = ("INSERT INTO tb_login (username,role) values ('" + logid1 + "','" + r1+ "');")
            cursor.execute(que)
            cursor.execute("COMMIT;")
        elif(ch2==2):
            que1 = ("SELECT * FROM tb_Instructor ;")
            cursor.execute(que1)
            result=cursor.fetchall()
            for row in result:
                for col in row:
                    print(col, end='')
                print()

                instructor = input("Enter the instructor id to modify its info: ")
                name1 = input("Enter your name: ")
                prog1 = input("Enter Programid: ")
                add1 = input("Enter your Address ")

                if name1:
                    que2 = ("UPDATE tb_instructor SET name='" + name1 + "'WHERE id='" + instructor + "';")
                    cursor.execute(que2)
                if prog1:
                    que3 = ("UPDATE tb_instructor SET program_id='" + prog1 + "'WHERE id='" + instructor + "';")
                    cursor.execute(que3)
                if add1:
                    que4 = ("UPDATE tb_instructor SET address='" + add1 + "'WHERE id='" + instructor + "';")
                cursor.execute(que4)
                cursor.execute("COMMIT;")

        elif(ch2 == '3'):
             break
def assignDetails1():
    q7=("Select * from tb_login")
    cursor.execute(q7)
    res=cursor.fetchall()
    for row in res:
        for col in row:
            print(col, end=' ')
        print()
    instructorid=input("Please select the instructor id to share its Username and Password")
    usrname1 = input("Enter Username: ")
    pwd1 = input("Enter Password to assign")
    if login:
        que5 = ("UPDATE tb_login SET username='" + usrname1 + "'WHERE id='" + instructorid + "';")
        cursor.execute(que5)
    if pwd:
        que6 = ("UPDATE tb_login SET password='" + pwd1 + "'WHERE id='" + instructorid + "';")
        cursor.execute(que6)
    cursor.execute("COMMIT;")
    print('Login Details updated and shared with Student')
    que7 = ("Select * from tb_course1")
    cursor.execute(que7)
    res1 = cursor.fetchall()
    for row in res1:
        for col in row:
            print(col, end=' ')
        print()
    programid = input("Please enter program id to enter assign courses to instructor")
    que8 = ("UPDATE tb_instructor SET program_id='" + programid + "'WHERE id='" + instructorid + "';")
    cursor.execute(que8)
    cursor.execute("COMMIT;")
    que9 = ("SELECT * FROM tb_instructor WHERE id ='" + instructorid + "';")
    cursor.execute(que9)
    res2 = cursor.fetchone()
    print(res2)

def assignCourseDetails1():
    while True:
        print(" 1.Assign Course to instructor")
        print(" 2.Assign Course to student")
        print(" 3.Back to Previous Menu")

        chf = input("\nEnter your Choice :")

        if (chf == '1'):
            que10 = ("Select * from tb_course1")
            cursor.execute(que10)
            res1 = cursor.fetchall()
            for row in res1:
                for col in row:
                    print(col, end=' ')
                print()
            courseid = input("Please Enter Course Id:-")
            ch2=input('Do you want to create new Instructor (Y/N)')
            if ch2=='Y':
                insid=input('Enter Login Id:')
                insusr=input('Enter username')
                inspwd=input('Enter Password:')
                insname = input('Enter Name:')
                insadd = input('Enter Address:')
                rl='I'
                que11 = ("INSERT INTO tb_instructor1 (login_id,name,course_id,address) values ('" + insid + "','" + insname + "','" + courseid + "','" + insadd + "');")
                cursor.execute(que11)
                que12 = ("INSERT INTO tb_login (id,username,password,role) values ('" + insid + "','" + insusr + "','" + inspwd + "','" + rl + "');")
                cursor.execute(que12)
                cursor.execute('COMMIT;')
                que13 = ("Select * from tb_instructor1")
                cursor.execute(que13)
                res1 = cursor.fetchall()
                for row in res1:
                    for col in row:
                        print(col, end=' ')
                    print()
            elif ch2=='N':
                que14= ("Select * from tb_instructor1")
                cursor.execute(que14)
                res1 = cursor.fetchall()
                for row in res1:
                    for col in row:
                        print(col, end=' ')
                    print()
                instid = input('Enter Instructor Id:')
                que15 = ("SELECT login_id,name,address FROM tb_instructor1 WHERE id ='" + instid + "';")
                ans = cursor.execute(que15)
                answer = cursor.fetchone()
                res = np.asarray(answer)
                inslog=res[0]
                insnm = res[1]
                insad = res[2]
                que16 = ("INSERT INTO tb_instructor1 (login_id,name,course_id,address) values ('" + inslog + "','" + insnm + "','" + courseid + "','" + insad + "');")
                cursor.execute(que16)
                cursor.execute('COMMIT;')


        elif (chf== '2'):
            que17 = ("Select * from tb_course1")
            cursor.execute(que17)
            res1 = cursor.fetchall()
            for row in res1:
                for col in row:
                    print(col, end=' ')
                print()
            courseid = input("Please Enter Course Id:-")
            ch2 = input('Do you want to create new Program (Y/N)')
            if ch2 == 'Y':
                progid = input('Enter Program Id:')
                prognm = input('Enter Program name')
                progyr = input('Enter Program year:')
                que18 = ("INSERT INTO tb_program (name,year) values ('" + prognm + "','" + progyr + "');")
                cursor.execute(que18)
                que19 = ("UPDATE tb_course1 SET program_id='" + progid + "'WHERE course_id='" + courseid + "';")
                cursor.execute(que19)
                cursor.execute('COMMIT;')
            elif ch2 == 'N':
                que20 = ("Select * from tb_program")
                cursor.execute(que20)
                res1 = cursor.fetchall()
                for row in res1:
                    for col in row:
                        print(col, end=' ')
                    print()
                proid = input('Enter Program Id:')
                que21 = ("UPDATE tb_course1 SET program_id='" + proid + "'WHERE course_id='" + courseid + "';")
                cursor.execute(que21)
                cursor.execute('COMMIT;')
            elif (chf == '3'):
                break

def schedule1(tb=None):
        pid = input('Enter Program ID to display schedule')
        que22 = (
                    "SELECT tb_course1.course_id,tb_course1.name,tb_course1.program_id,tb_instructor1.name,tb_timetable1.date,tb_timetable1.time FROM tb_course1 INNER JOIN tb_timetable1 ON tb_course1.course_id=tb_timetable1.course_id JOIN tb_instructor1 ON tb_course1.course_id=tb_instructor1.course_id WHERE tb_course1.program_id='" + pid + "';")
        cursor.execute(que22)

        data = np.asarray(cursor.description)
        # print('Cursor Description', data)
        i = 0
        for x in data:
            print(x[0], end=' ')
        print()

        res3 = cursor.fetchall()
        for row in res3:
            for col in row:
                print(col, end=' ')
                print(tabulate(tb))
            print()
def login1():

    username=input("Enter your username")
    password=input("Enter your password")
    que23= ("SELECT role FROM tb_login WHERE username ='" +username +"'AND Password='"+password+"';")
    role = cursor.execute(que23)
    role=cursor.fetchone()
    data = np.asarray(role)
    print(role)
    if role:
        return data[0]
    else:
        return False

while True:
    print("1.Login")
    print("2.Exit")
    ch1=input("Enter your choice")
    if (ch1=='1'):

        login_sucess = login1()
        if login_sucess:

            if login_sucess == 'AI':
                while True:
                    print(" 1.Add and Manage Instructor Status and Info")
                    print(" 2.Assign Login Details and Courses to instructor")
                    print(" 3.Release Class schedule as per course")
                    print(" 4.Back to Main Menu")

                    ch1 = input("Enter your Choice :")

                    if (ch1== '1'):
                        ManageInfo1()
                    elif (ch1 == '2'):
                        assignDetails1()
                    elif (ch1 == '3'):
                        schedule1()
                    elif (ch1 == '4'):
                        break

                    elif login_sucess == 'I':
                        print("Abab write your code for Instructor ")
                    elif login_sucess == 'S':
                        print("Nikita write your code")
    else:
        break