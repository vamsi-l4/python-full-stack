students = {}  # Dictionary to store student data

def add_student():
    name = input("Enter the student name: ")
    subject = input("Enter the subject name: ")
    marks = list(map(int, input("Enter the marks: ").split()))
    
    if name not in students:
        students[name] = {}  # Initialize a nested dictionary for the student
    
    students[name][subject] = marks
    print(f"Added {name} -> {subject}: {marks}")

def avg_student():
    name = input("Enter the student name: ")
    
    if name in students:
        total_marks = []
        for subject in students[name].values():
            total_marks.extend(subject)  # Collect all subject marks
        
        avg = sum(total_marks) / len(total_marks)
        print(f"{name}'s overall average marks: {avg:.2f}")
    else:
        print("Student not found.")


def search_student():
    name_to_search = input("Enter the student name: ")
    
    if name_to_search in students:
        print(f"{name_to_search}: {students[name_to_search]}")
    else:
        print("Student not found.")

def update_student():
    name_to_update = input("Enter the student name: ")
    subject = input("Enter the subject to update: ")
    marks = list(map(int, input("Enter the new marks: ").split()))
    
    if name_to_update in students and subject in students[name_to_update]:
        students[name_to_update][subject] = marks
        print(f"Updated {name_to_update}'s {subject} marks: {marks}")
    else:
        print("Student or subject not found.")

def remove_student():
    student_name = input("Enter the student to remove: ")
    
    if student_name in students:
        del students[student_name]
        print(f"Removed student: {student_name}")
    else:
        print("Student not found.")
