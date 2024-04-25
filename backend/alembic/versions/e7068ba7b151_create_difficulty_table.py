"""create difficulty table

Revision ID: e7068ba7b151
Revises: 0ad29b5ba4d1
Create Date: 2024-04-23 19:48:09.506350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e7068ba7b151'
down_revision: Union[str, None] = '0ad29b5ba4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade database."""
    op.create_table(
        "difficulties",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("label", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("max_attempts", sa.Integer, nullable=False),
        sa.Column("code_length", sa.Integer, nullable=False),
        sa.Column("minimum_number", sa.Integer, nullable=False),
        sa.Column("maximum_number", sa.Integer, nullable=False),
        sa.Column("is_duplicate_allowed", sa.Boolean),
    )

    def downgrade() -> None:
        """Downgrade database."""
        op.drop_table("difficulties")
