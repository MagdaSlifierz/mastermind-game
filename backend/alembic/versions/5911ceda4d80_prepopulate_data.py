"""prepopulate data

Revision ID: 5911ceda4d80
Revises: 3ab95d24435b
Create Date: 2024-04-24 21:40:58.807993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column

# revision identifiers, used by Alembic.
revision: str = '5911ceda4d80'
down_revision: Union[str, None] = '3ab95d24435b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add data to difficulties table."""
    difficulties_table = table(
        'difficulties',
        column('id', sa.Integer),
        column('name', sa.Text),
        column('label', sa.Text),
        column('max_attempts', sa.Integer),
        column('code_length', sa.Integer),
        column('minimum_number', sa.Integer),
        column('maximum_number', sa.Integer),
        column('is_duplicate_allowed', sa.Boolean),
    )
    op.bulk_insert(
        difficulties_table,
        [
            {'id': 1, 'name': 'easy', 'label': 'Easy', 'max_attempts': 10, 'code_length': 4, 'minimum_number': 0,
             'maximum_number': 7, 'is_duplicate_allowed': False},
            {'id': 2, 'name': 'medium', 'label': 'Medium', 'max_attempts': 9, 'code_length': 5, 'minimum_number': 0,
             'maximum_number': 8, 'is_duplicate_allowed': True},
            {'id': 3, 'name': 'hard', 'label': 'Hard', 'max_attempts': 8, 'code_length': 6, 'minimum_number': 0,
             'maximum_number': 9, 'is_duplicate_allowed': True},
        ]
    )


def downgrade() -> None:
    """Remove data from difficulties table."""
    op.drop_table('difficulties')
