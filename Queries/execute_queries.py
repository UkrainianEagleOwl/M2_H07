import sqlite3
from prettytable import PrettyTable


def connect_to_data_base(data_base, query_file_name) -> list():
    # Connect to the database
    conn = sqlite3.connect(data_base)
    cursor = conn.cursor()

    # Read the SQL queries from the file
    with open(query_file_name, "r") as query_file:
        queries = query_file.read().split(';')

    # Execute each query
    for query in queries:
        if query.strip():
            cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results



def create_prettytable(header_first, header_second, data_base_results):
    # Create a PrettyTable instance
    table = PrettyTable()
    if header_second:
        table.field_names = [header_first, header_second]
    else:
        table.field_names = [header_first]

    # Add rows to the table
    for row in data_base_results:
        table.add_row(row)

    return table


def first_query():
    con_result = connect_to_data_base("study.db", "Queries/query_one.sql")
    print(create_prettytable("Student", "Average GPA", con_result))


def second_query():
    con_result = connect_to_data_base("study.db", "Queries/query_two.sql")
    print(create_prettytable("Student", "Average GPA in Mathematics", con_result))


def third_query():
    con_result = connect_to_data_base("study.db", "Queries/query_three.sql")
    print(create_prettytable("Group number", "Average GPA in Chemistry", con_result))
    
def fourth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_four.sql")
    print(create_prettytable("Average GPA in all Stream", None, con_result))
    
def fifth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_five.sql")
    print(create_prettytable("Teacher", "Subject", con_result))
    
def sixth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_six.sql")
    print(create_prettytable("Student's from group 4 ", None , con_result))
    
def seventh_query():
    con_result = connect_to_data_base("study.db", "Queries/query_seven.sql")
    print(create_prettytable("Student's from group 7", "History Grade" , con_result))
    
def eighth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_eight.sql")
    print(create_prettytable("Teacher", "Average GPA given in German", con_result))
    
def ninth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_nine.sql")
    print(create_prettytable("Subjects of Melanie Lara", None, con_result))
    
def tenth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_ten.sql")
    print(create_prettytable("Subject", None, con_result))
    
def eleventh_query():
    con_result = connect_to_data_base("study.db", "Queries/query_eleven.sql")
    print(create_prettytable("Average GPA given by Teresa Bennett to Michael Valdez", None, con_result))
    
def twelfth_query():
    con_result = connect_to_data_base("study.db", "Queries/query_twelve.sql")
    print(create_prettytable("Student of group 3", "Grades of Ukrainian on last lesson", con_result))

if __name__ == "__main__":
    # first_query()
    # second_query()
    #third_query()
    #fourth_query()
    #fifth_query()
    #sixth_query()
    #seventh_query()
    #eighth_query()
    # ninth_query()
    #tenth_query()
    #eleventh_query()
    twelfth_query()
    
