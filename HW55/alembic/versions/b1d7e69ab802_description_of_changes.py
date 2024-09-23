"""Description of changes

Revision ID: b1d7e69ab802
Revises: 0fb9b9348dd0
Create Date: 2024-09-21 21:30:50.557547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1d7e69ab802'
down_revision: Union[str, None] = '0fb9b9348dd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts', 'content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts', 'author_id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               nullable=False)
    op.drop_index('ix_posts_id', table_name='posts')
    op.drop_index('ix_posts_title', table_name='posts')
    op.alter_column('users', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    op.create_index('ix_posts_title', 'posts', ['title'], unique=False)
    op.create_index('ix_posts_id', 'posts', ['id'], unique=False)
    op.alter_column('posts', 'author_id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               nullable=True)
    op.alter_column('posts', 'content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    # ### end Alembic commands ###