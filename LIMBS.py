#Personal details
name = input("Enter your good name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
role = input("Enter your role (Student/Faculty): ")
#Book details input
programme = input("Enter the programme in which your book\nmay be found (B. Tech., M. Tech., Ph.D.): ")
field = input("Enter the field in which the subject is found: ")
print("Enter the year relevant to the subject.")
if programme=="B.Tech." or programme=="B. Tech.":
    year = int(input("'1' for FY, '2' for SY, '3' for TY or '4' for LY.\nYear: ")) 
elif programme=="M.Tech." or programme=="M. Tech.":
    year = int(input("'1' for FY, '2' for LY.\nYear: "))
elif programme=="Ph.D." or programme=="PhD":
    year = int(input("Enter a number indicating the number of years you have been doing this course.\nYear: "))
subject = input("Enter the subject of the book which you want to issue: ")
def btech():
    pass
def mtech():
    pass
def phd():
    pass
#search algorithm for books - use in-built function
#file handling
