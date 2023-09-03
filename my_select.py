from sqlalchemy import func, desc

from connect_db import session
from models import *
from prettytable import PrettyTable
import decimal

def create_prettytable(*header, data):
    # Create a PrettyTable instance
    table = PrettyTable()
    table.field_names = header

    # Add rows to the table
    if data is not None:
        for item in data:
            table.add_row(item)

    return table

def select_1():
    # Calculate GPA using SQLAlchemy's func.avg function
    avg_grade = func.avg(Grade.grade).label("avg_grade")

    # Query to find the top 5 students with the highest GPA
    top_students = (
        session.query(Student.name, func.round(avg_grade,2))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.name)
        .order_by(avg_grade.desc())
        .limit(5)
        .all()
    )
    
    # example   
    # top_students = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
    #     .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

    return create_prettytable('Name','GPA',top_students)

def select_2(subject_name):
    # Calculate GPA using SQLAlchemy's func.avg function
    avg_grade = func.avg(Grade.grade).label("avg_grade")

  # Query to find the student with the highest GPA in the specified subject
    top_student = (
        session.query(Student.name, func.round(avg_grade,2))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.name)
        .order_by(avg_grade.desc())
        .limit(1)
        .first()
    )

    return create_prettytable('Name',f'GPA in {subject_name}',[top_student])

def select_3(subject_name):
    # Calculate GPA using SQLAlchemy's func.avg function
    avg_group_grade = func.avg(Grade.grade).label("avg_grade")

  # Query to find the student with the highest GPA in the specified subject
    avg_group_scores = (
        session.query(Group.group_number, func.round(avg_group_grade,2))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)   
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.group_number)
        .order_by(avg_group_grade.desc())
        .all()
    )

    return create_prettytable('Group Number',f'GPA in {subject_name}',avg_group_scores)

def select_4():
    # Calculate the average score across the entire scoreboard
    avg_score = func.avg(Grade.grade).label("avg_score")

    # Query to find the average score across the entire scoreboard
    average_score = (
        session.query(func.round(avg_score, 2))
        .scalar()
    )

    return create_prettytable('Average Score', data = [average_score])

def select_5(teacher_name):
    # Query to find the courses taught by a specific teacher
    courses_taught = (
        session.query(Subject.name)
        .join(Teacher, Subject.id == Teacher.subject_id)
        .filter(Teacher.name == teacher_name)
        .all()
    )

    return create_prettytable('Courses Taught', data=[course[0] for course in courses_taught])

def select_6(group_number):
    # Query to find the students in a specific group
    students_in_group = (
        session.query(Student.name)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.group_number == group_number)
        .all()
    )

    return create_prettytable('Students in Group', data=students_in_group)

def select_7(subject_name, group_number):
    # Query to find grades of all students in a specific group for a specific subject
    student_grades = (
        session.query(Student.name, Grade.date_of, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .filter(Group.group_number == group_number)
        .all()
    )

    return create_prettytable('Student Name', 'Date', 'Grade', data=student_grades)

def select_8(teacher_name):
    # Calculate the average score using SQLAlchemy's func.avg function
    avg_score = func.avg(Grade.grade).label("avg_score")

    # Query to find the average score given by a certain teacher in their subjects
    teacher_average_scores = (
        session.query(Subject.name, func.round(avg_score, 2))
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Teacher, Subject.id == Teacher.subject_id)
        .filter(Teacher.name == teacher_name)
        .group_by(Subject.name)
        .all()
    )

    return create_prettytable('Subject', 'Average Score', data=teacher_average_scores)

def select_9(student_name):
    # Query to find a list of subjects that a particular student is taking
    student_subjects = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Student.name == student_name)
        .distinct()
        .all()
    )

    return create_prettytable('Subject', data=student_subjects)

def select_10(student_name, teacher_name):
    # Query to find a list of courses taught to a specific student by a specific instructor
    student_teacher_courses = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .join(Teacher, Subject.id == Teacher.subject_id)
        .filter(Student.name == student_name)
        .filter(Teacher.name == teacher_name)
        .distinct()
        .all()
    )

    return create_prettytable('Subject', data=student_teacher_courses)

def select_11(student_name, teacher_name):
    # Calculate the average score given by the specified teacher to the specified student
    avg_teacher_student_score = (
        session.query(func.avg(Grade.grade).label("avg_score"))
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Teacher, Subject.id == Teacher.subject_id)
        .filter(Student.name == student_name)
        .filter(Teacher.name == teacher_name)
        .scalar()
    )

    return f"Average Score Given by {teacher_name} to {student_name}: {avg_teacher_student_score:.2f}"

def select_12(group_id, subject_name):
    # Query to find the grades of students in a specific group for a specific subject in the last lesson
    last_lesson_grades = (
        session.query(Student.name, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.id == group_id)
        .filter(Subject.name == subject_name)
        .order_by(desc(Grade.date_of))
        .first()
    )

    return create_prettytable('Student Name', 'Grade', data = [last_lesson_grades])

if __name__ == '__main__':
    #print(select_1())
    #print(select_2('Ukrainian'))
    #print(select_3('History'))
    #print(select_4())
    #print(select_5('Amy Huffman'))
    #print(select_6(4))
    #print(select_7("Literature", 4))
    #print(select_8("Brett Wilkerson"))
    #print(select_9("Joshua Patterson"))
    #print(select_10("Michael Harris",'Catherine Rasmussen'))
    #print(select_11("Paul Stafford",'James Hunt'))
    print(select_12(9, "Chemistry"))
    session.close()