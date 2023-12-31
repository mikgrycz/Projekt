"""Db migration does it work  ufhr4eiufhirtghiruthgiurtg irtghuitgigt

Revision ID: d367337f769e
Revises: 53dfd9d77601
Create Date: 2023-12-03 00:11:57.538668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd367337f769e'
down_revision: Union[str, None] = '53dfd9d77601'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'PictureLink2')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('PictureLink2', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
