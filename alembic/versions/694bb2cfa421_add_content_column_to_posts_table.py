"""add content column to posts table

Revision ID: 694bb2cfa421
Revises: 508ba2b99567
Create Date: 2024-01-23 13:28:08.484195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '694bb2cfa421'
down_revision: Union[str, None] = '508ba2b99567'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
