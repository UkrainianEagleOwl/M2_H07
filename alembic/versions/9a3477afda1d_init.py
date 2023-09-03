"""Init

Revision ID: 9a3477afda1d
Revises: f9c664e23442
Create Date: 2023-09-03 19:01:18.829872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a3477afda1d'
down_revision: Union[str, None] = 'f9c664e23442'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('subject_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'grades', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    op.add_column('students', sa.Column('name', sa.String(length=255), nullable=False))
    op.drop_constraint('students_student_key', 'students', type_='unique')
    op.create_unique_constraint(None, 'students', ['name'])
    op.drop_column('students', 'student')
    op.add_column('subjects', sa.Column('name', sa.String(length=255), nullable=False))
    op.drop_constraint('subjects_subject_key', 'subjects', type_='unique')
    op.create_unique_constraint(None, 'subjects', ['name'])
    op.drop_column('subjects', 'subject')
    op.add_column('teachers', sa.Column('name', sa.String(length=255), nullable=False))
    op.drop_constraint('teachers_teacher_key', 'teachers', type_='unique')
    op.create_unique_constraint(None, 'teachers', ['name'])
    op.drop_column('teachers', 'teacher')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teachers', sa.Column('teacher', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'teachers', type_='unique')
    op.create_unique_constraint('teachers_teacher_key', 'teachers', ['teacher'])
    op.drop_column('teachers', 'name')
    op.add_column('subjects', sa.Column('subject', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'subjects', type_='unique')
    op.create_unique_constraint('subjects_subject_key', 'subjects', ['subject'])
    op.drop_column('subjects', 'name')
    op.add_column('students', sa.Column('student', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'students', type_='unique')
    op.create_unique_constraint('students_student_key', 'students', ['student'])
    op.drop_column('students', 'name')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_column('grades', 'subject_id')
    # ### end Alembic commands ###
