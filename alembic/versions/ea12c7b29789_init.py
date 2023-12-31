"""Init

Revision ID: ea12c7b29789
Revises: f04e3e7e2b51
Create Date: 2023-09-03 19:50:47.133141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea12c7b29789'
down_revision: Union[str, None] = 'f04e3e7e2b51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('grades_subject_id_fkey', 'grades', type_='foreignkey')
    op.drop_constraint('grades_student_id_fkey', 'grades', type_='foreignkey')
    op.create_foreign_key(None, 'grades', 'subjects', ['subject_id'], ['id'])
    op.create_foreign_key(None, 'grades', 'students', ['student_id'], ['id'])
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'groups', ['group_id'], ['id'])
    op.drop_constraint('teachers_subject_id_fkey', 'teachers', type_='foreignkey')
    op.create_foreign_key(None, 'teachers', 'subjects', ['subject_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teachers', type_='foreignkey')
    op.create_foreign_key('teachers_subject_id_fkey', 'teachers', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_group_id_fkey', 'students', 'groups', ['group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.create_foreign_key('grades_student_id_fkey', 'grades', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('grades_subject_id_fkey', 'grades', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
