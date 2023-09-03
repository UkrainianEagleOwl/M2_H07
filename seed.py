from connect_db import session
from generator_data import *


def generate_fake_data():
    # Generate and add groups
    groups = generate_groups()
    session.add_all(groups)
    session.flush()  # Flush to get generated IDs

    # Generate and add subjects
    subjects = generate_subjects()
    session.add_all(subjects)
    session.flush()  # Flush to get generated IDs

    # Generate and add students
    students = generate_students(groups)
    session.add_all(students)
    session.flush()  # Flush to get generated IDs

    # Generate and add teachers
    teachers = generate_teachers(subjects) 
    session.add_all(teachers)
    session.flush()  # Flush to get generated IDs

    # Generate and add grades
    session.add_all(generate_grades(students,subjects))
    session.commit()

# Insert data to the database
def insert_data_to_db(students, groups, subjects, teachers, grades) -> None:
    try:
        # Insert groups, subjects, students, teachers, and grades into the session
        session.add_all(groups)
        session.add_all(subjects)
        session.add_all(students)
        session.add_all(teachers)
        session.add_all(grades)

        # Commit the changes to the database
        session.commit()
    except Exception as e:
        # Handle any exceptions that may occur during the insertion
        session.rollback()
        raise e
    finally:
        # Close the session
        session.close()
        
def clear_database():
    try:
        # Delete all records from each table
        session.query(Grade).delete()
        session.query(Student).delete()
        session.query(Teacher).delete()
        session.query(Subject).delete()
        session.query(Group).delete()

        # Commit the changes to the database
        session.commit()
    except Exception as e:
        # Handle any exceptions that may occur during deletion
        session.rollback()
        raise e
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    clear_database()   
    generate_fake_data()
