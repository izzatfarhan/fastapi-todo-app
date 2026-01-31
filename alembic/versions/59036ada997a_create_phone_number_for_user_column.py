"""Create phone number for user column

Revision ID: 59036ada997a
Revises: 
Create Date: 2026-01-20 12:05:02.451203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59036ada997a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users',
                  sa.Column('phone_number',
                            sa.String(20), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')

