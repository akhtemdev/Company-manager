"""fix department migration

Revision ID: 8619348feeb1
Revises: 
Create Date: 2024-08-25 14:05:43.068036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8619348feeb1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'company_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'departments', 'companies', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.alter_column('departments', 'company_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
