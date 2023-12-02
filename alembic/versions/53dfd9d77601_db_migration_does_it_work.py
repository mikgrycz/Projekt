"""Db migration does it work

Revision ID: 53dfd9d77601
Revises: ec38c641c51a
Create Date: 2023-12-03 00:11:07.919402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53dfd9d77601'
down_revision: Union[str, None] = 'ec38c641c51a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('PictureLink2', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'PictureLink2')
    # ### end Alembic commands ###
