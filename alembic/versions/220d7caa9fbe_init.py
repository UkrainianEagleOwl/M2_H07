"""Init

Revision ID: 220d7caa9fbe
Revises: 9a3477afda1d
Create Date: 2023-09-03 19:09:13.652179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '220d7caa9fbe'
down_revision: Union[str, None] = '9a3477afda1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('grade', sa.Integer(), nullable=False))
    op.drop_column('grades', 'total')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('grades', 'grade')
    # ### end Alembic commands ###
