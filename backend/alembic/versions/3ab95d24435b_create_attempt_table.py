"""create attempt table

Revision ID: 3ab95d24435b
Revises: 12fdd7d996c2
Create Date: 2024-04-23 19:48:24.452364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3ab95d24435b'
down_revision: Union[str, None] = '12fdd7d996c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade database."""

    # You may need to ensure that the UUID extension is enabled in PostgreSQL
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    op.create_table(
        "attempts",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("game_id", sa.Integer, sa.ForeignKey("games.id")),
        sa.Column(
            "unique_id",
            sa.UUID(as_uuid=True),
            unique=True,
            nullable=False,
            server_default=sa.text("uuid_generate_v4()")),
        sa.Column("number_of_attempts", sa.Integer, nullable=False, default=1),
        sa.Column("guess", sa.Text, nullable=False),
        sa.Column("feedback", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
    )


def downgrade() -> None:
    """Downgrade database."""
    op.drop_table("attempts")
