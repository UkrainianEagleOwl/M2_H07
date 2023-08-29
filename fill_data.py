from faker import Faker
import sqlite3
from random import randint, choice
from datetime import datetime

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


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open("study.sql", "r") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect("study.db") as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


# Function to generate fake data
def generate_fake_data(
    number_students, number_groups, number_subjects, number_teachers
) -> tuple():
    fake_students = set()
    fake_groups = set()
    fake_subjects = set()
    fake_teachers_names = set()
    fake_teachers = list()

    while len(fake_students) < number_students:
        fake_students.add(fake_data.name())
        
    while len(fake_groups) < number_groups:
        fake_groups.add(fake_data.random_int(min=1, max=10))

    while len(fake_subjects) < number_subjects:
        fake_subjects.add(choice(RANDOM_SUBJECTS))
        
    while len(fake_teachers_names) < number_teachers:
        fake_teachers_names.add(fake_data.name())
        
    for name in fake_teachers_names:
        fake_teachers.append((name, choice(range(1, number_subjects + 1))))

    return fake_students, fake_groups, fake_subjects, fake_teachers


# Prepare data
def prepare_data(students, groups, subjects, teachers) -> tuple():
    for_students = []
    for student in students:
        group_id = randint(1, NUMBER_GROUPS)
        for_students.append((student, group_id))

    for_groups = [
        (group,) for group in groups
    ]  # Adjusting the data format for executemany

    for_subjects = [
        (subject,) for subject in subjects
    ]  # Adjusting the data format for executemany

    for_teachers = []

    for teacher in teachers:
        teacher_name, teacher_subject_id = teacher
        for_teachers.append((teacher_name, teacher_subject_id))

    for_grades = []

    for student_id in range(1, len(students) + 1):
        for subject_id in range(1, len(subjects) + 1):
            for _ in range(randint(1, 20)):
                date_of = fake_data.date_between(start_date="-1y", end_date="today")
                grade = randint(50, 100)
                for_grades.append((student_id, subject_id, date_of, grade))

    return for_students, for_groups, for_subjects, for_teachers, for_grades


# Insert data to the database
def insert_data_to_db(students, groups, subjects, teachers, grades) -> None:
    with sqlite3.connect("study.db") as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student, group_id)
                             VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_groups = """INSERT INTO groups(group_number)
                            VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = """INSERT INTO subjects(subject)
                             VALUES (?)"""

        cur.executemany(sql_to_subjects, subjects)

        sql_to_teachers = """INSERT INTO teachers(teacher, subject_id)
                             VALUES (?, ?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = """INSERT INTO student_grades(student_id, subject_id, date_of, grade)
                           VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    create_db()
    students, groups, subjects, teachers = generate_fake_data(
        NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS
    )
    insert_data_to_db(*prepare_data(students, groups, subjects, teachers))
