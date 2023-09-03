from models import Grade,Group,Student,Teacher,Subject
from faker import Faker
from random import randint, choice

# Constants
NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5

# Define a list of subjects
RANDOM_SUBJECTS = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "English",
    "Literature",
    "Computer Science",
    "Ukrainian",
    "German"
    # Add more subjects as needed
]

fake_data = Faker()

def generate_groups() -> list():
    unique_groups = set()
    groups = list()
    
    while len(groups) < NUMBER_GROUPS:
        group_number = fake_data.random_int(min=1, max=10)
        if group_number not in unique_groups:
            unique_groups.add(group_number)
            groups.append(Group(group_number=group_number))
    return groups

def generate_subjects() -> list():
    unique_subjects = set()
    subjects = list()
    
    while len(subjects) < NUMBER_SUBJECTS:
        subject_name = choice(RANDOM_SUBJECTS)
        if subject_name not in unique_subjects:
            unique_subjects.add(subject_name)
            subjects.append(Subject(name=subject_name))
    return subjects

def generate_students(groups) -> list():
    unique_students = set()
    students =list()
    
    while len(students) < NUMBER_STUDENTS:
        student_name = fake_data.name()
        group_id = choice(groups).id
        student_key = (student_name, group_id)
        if student_key not in unique_students:
            unique_students.add(student_key)
            students.append(Student(name=student_name, group_id=group_id))
    return students

def generate_teachers(subjects) -> list():  
    unique_teachers = set()
    teachers = list()
    
    while len(teachers) < NUMBER_TEACHERS:
        teacher_name = fake_data.name()
        subject_id = choice(subjects).id
        teacher_key = (teacher_name, subject_id)
        if teacher_key not in unique_teachers:
            unique_teachers.add(teacher_key)
            teachers.append(Teacher(name=teacher_name, subject_id=subject_id))
    return teachers

def generate_grades(students,subjects):
    grades = list()
    for student in students:
        for subject in subjects:
            for _ in range(randint(1, 20)):
                date_of = fake_data.date_between(start_date="-1y", end_date="today")
                grade = randint(50, 100)
                grades.append(Grade(student_id=student.id, subject_id=subject.id, date_of=date_of, grade=grade))
    return grades
