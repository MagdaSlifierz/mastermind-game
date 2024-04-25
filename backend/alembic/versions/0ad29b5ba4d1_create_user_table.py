"""create user table

Revision ID: 0ad29b5ba4d1
Revises: 
Create Date: 2024-04-23 19:47:54.061370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0ad29b5ba4d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade database."""

    # You may need to ensure that the UUID extension is enabled in PostgreSQL
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("unique_id", sa.UUID(as_uuid=True), unique=True, nullable=False,
                  server_default=sa.text("uuid_generate_v4()")),
        sa.Column("username", sa.Text, unique=True, index=True),
    )


def downgrade() -> None:
    """Downgrade database."""
    op.drop_table("users")
