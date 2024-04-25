"""create game table

Revision ID: 12fdd7d996c2
Revises: e7068ba7b151
Create Date: 2024-04-23 19:48:16.782348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '12fdd7d996c2'
down_revision: Union[str, None] = 'e7068ba7b151'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade database."""

    # You may need to ensure that the UUID extension is enabled in PostgreSQL
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    op.create_table(
        "games",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column(
            "unique_id",
            sa.UUID(as_uuid=True),
            unique=True,
            nullable=False,
            server_default=sa.text("uuid_generate_v4()")),
        sa.Column("difficulty_id", sa.Integer, sa.ForeignKey("difficulties.id")),
        sa.Column("is_multiplayer", sa.Boolean, default=False),
        sa.Column("secret_code", sa.Text),
        sa.Column("hints", sa.Text),
        sa.Column("status", sa.Text, default="in_progress"),
        sa.Column("mastermind_id", sa.Integer, sa.ForeignKey("users.id"), nullable=True),
        sa.Column("codebreaker_id", sa.Integer, sa.ForeignKey("users.id"), nullable=True),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
    )


def downgrade() -> None:
    """Downgrade database."""
    op.drop_table("games")
