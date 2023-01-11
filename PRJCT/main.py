# STUDENT MANAGEMENT SYSTEM
import mysql.connector as ms

print("""
        ================================
        W E L C O M E  T O  L U M I N A R 
        ================================
""")

cn = ms.connect(host="localhost", user="root", passwd="Jas@123")
cur = cn.cursor()
cur.execute("create database if not exists management_system")
cur.execute("use management_system")
cur.execute("CREATE TABLE if not exists mentors (id INT PRIMARY KEY, name VARCHAR(30), course VARCHAR(30))")
cur.execute("CREATE TABLE if not exists students (id INT PRIMARY KEY, name VARCHAR(30), course VARCHAR(30))")
cur.execute("CREATE TABLE if not exists users (username VARCHAR(30) PRIMARY KEY, password VARCHAR(30))")
cur.execute("CREATE TABLE if not exists admin (username VARCHAR(30) PRIMARY KEY, password VARCHAR(30))")
u = "admin"
p = "007"
cur.execute("insert ignore into admin values('" + u + "','" + p + "')")

# SIGNUP AND LOGIN
print("1. SIGNUP")
print("2. LOGIN AS ADMINISTRATOR")
print("3. LOGIN AS USER")
choice = int(input("Enter your choice : "))
# CHOICE 1
if choice == 1:
    print("""
                ============================================
                        Please enter new user details
                ============================================
                                                        """)
    un = input("Enter New User Name : ")
    ps = input("Enter password : ")
    cur.execute("insert into users values('" + un + "','" + ps + "')")
    cn.commit()
    print("""
                ========================================================
                        Congratulations!! New User Created !!
                ========================================================
                                                            """)
# CHOICE 2
elif choice == 2:
    print("""
                ==========================================================
                            Login as Administrator
                ==========================================================
                                                            """)
    usr = input("Username : ")
    psd = input("Password : ")
    cur.execute("select password from admin where username='" + usr + "'")
    rec = cur.fetchall()
    for i in rec:
        a = list(i)
        if a[0] == str(psd):
            print("""
                    ==========================================================
                                        W E L C O M E
                    ==========================================================
                                                                """)
            # MAIN MENU
            print("""
                     1. TASKS
                     2. LOG OUT
                                            """)
            a = int(input("Enter your choice : "))
            if a == 1:
                print("""
                        1. VIEW DETAILS
                        2. ADD DETAILS
                        3. DELETE
                        4. EXIT
                                            """)
                b = int(input("Enter your choice : "))
                if b == 1:
                    print("""
                            1. STUDENTS
                            2. MENTORS
                                            """)
                    c = int(input("Enter your choice : "))
                    if c == 1:
                        cur.execute("select * from students")
                        rec = cur.fetchall()
                    elif c == 2:
                        cur.execute("select * from mentors")
                        rec = cur.fetchall()
                    else:
                        print("INVALID INPUT")
                elif b == 2:
                    pass

                else:
                    pass
            else:
                pass
    else:
        print("INCORRECT!!")
        print("ENTER CORRECT DETAILS FOR ADMIN !!")
# CHOICE 3
elif choice == 3:
    user = input("Username : ")
    psw = input("Password : ")
    cur.execute("select password from users where username='" + user + "'")
    rec = cur.fetchall()
    for i in rec:
        a = list(i)
        if a[0] == str(psw):
            while True:
                print("""
                        ==========================================================
                                            W E L C O M E
                        ==========================================================
                                                                    """)
                break
    else:
        print("INCORRECT USERNAME OR PASSWORD!")
else:
    print("INVALID INPUT")
