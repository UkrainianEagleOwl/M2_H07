
# Advanced Academic Database with SQLAlchemy

## Overview
This project extends the previous academic database project by integrating it with PostgreSQL using Docker and implementing SQLAlchemy models. It includes data migration with Alembic and a Python script (`seed.py`) for populating the database with random data using Faker. The project also features a `my_select.py` file containing functions for executing specific SQL queries using SQLAlchemy sessions.

## Features
- **SQLAlchemy Models**:
  - Models for students, groups, teachers, subjects, and grades tables.
- **Database Migration**:
  - Alembic for managing database schema changes.
- **Data Seeding**:
  - `seed.py` script to populate the database with random data (30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, up to 20 grades per student).
- **Custom Query Functions**:
  - `my_select.py` containing functions `select_1` to `select_10` for specific database queries.
- **Docker Integration**:
  - Instructions for setting up a PostgreSQL database in a Docker container.
