#Personal details
name = input("Enter your good name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
role = input("Enter your role (Student/Faculty): ")
role=role.upper()
#Book details input
programme = input("Enter the programme in which your book\nmay be found (B. Tech., M. Tech., Ph.D.): ")
programme=programme.upper()

field = input("Enter the field in which the subject is found: ")
print("Enter the year relevant to the subject: ")
if programme=="B.TECH." or programme=="B. TECH.":
    year = int(input("'1' for FY, '2' for SY, '3' for TY or '4' for LY.\nYear: ")) 
elif programme=="M.TECH." or programme=="M. TECH.":
    year = int(input("'1' for FY, '2' for SY.\nYear: "))
elif programme=="PH.D." or programme=="PHD":
    year = int(input("Enter a number indicating the number of years you have been doing this course.\nYear: "))
        
if role=="FACULTY":
    print("As a Faculty, You can not access this system!!")
elif age<18:
    print("Only people of age 18 and above can access this system.")
else:
    if programme=="B. TECH.":
        def btech():
            if year==1:
                b_l = open('FY_BTECH_BOOKS.csv', 'r')
                print(b_l.read())
            elif year==2:
                if field=="Computer Engineering" or "COMPS":
                    b_l = open('SY_BTECH_COMPS.csv', 'r')
                    print(b_l.read(), end = "\t\t")
                elif field=="Electronics Engineering" or "ETRX":
                    b_l = open('SY_BTECH_ETRX.csv', 'r')
                    print(b_l.read())
                elif field=="Electronics and Telecommunications Engineering" or "EXTC":
                    b_l = open('SY_BTECH_EXTC.csv', 'r')
                    print(b_l.read())
                elif field=="Information Technology" or "IT":
                    b_l = open('SY_BTECH_IT.csv', 'r')
                    print(b_l.read())
                elif field=="Mechanical Engineering" or "MECH":
                    b_l = open('SY_BTECH_MECH.csv', 'r')
                    print(b_l.read())
            elif year==3:
                print("Not Available!")
            elif year==4:
                print("Not Available!")
            else:
                print("Sorry! Wrong year has been entered!")
        btech()
    elif programme=="M. TECH.":
        def mtech():
            print("Not Available!")        
        mtech()
    elif programme=="PH. D.":
        def phd():
            print("Not Available!")
        phd()
    else:
        print("The entered programme does not exist.")

#search algorithm for books - use in-built function
#file handling
b_i = open('BOOKS_ISSUE.csv', '\ta')
b_i.write(input("Enter the subject of the book which you want to issue: "))
b_i.close()
b_i = open('BOOKS_ISSUE.csv', 'r')
print(b_i.read())
