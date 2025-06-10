student={}
def add_student():
    name=input("enter the student name :")
    sub=input("enter the subject name :")
    marks=list(map(int , input("enter the marks:").split(" ")))
    student[sub]=marks
def avg_student():
     name = input("Enter the student name: ")
     sub = input("Enter the subject name: ")
    
     if name in student and sub in student[name]:
        marks = student[name][sub]
        avg = sum(marks) / len(marks)
        print(f"{name}'s average marks in {sub}: {avg:.2f}")
     else:
        print("Student or subject not found.")
def search_student():
    name_to_search=input("enter the student: ")
    if name_to_search in student:
        print(f"{name_to_search}: {student[name_to_search]}")
    else:
        print("Student not found")
def update_student():
    name_to_update=input("enter the your update student:")
    marks=int(input("enter the marks:"))
    student[name_to_update]=marks
def remove_student():
    student_name=input("enter the remove sudent:")
    del student[student_name] 
    print("after removing",student_name)       