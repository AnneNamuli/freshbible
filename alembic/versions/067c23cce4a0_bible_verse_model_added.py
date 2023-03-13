"""bible verse model added

Revision ID: 067c23cce4a0
Revises: 314a0cbb454e
Create Date: 2021-11-05 10:19:43.693931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067c23cce4a0'
down_revision = '314a0cbb454e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bible_verse',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('book_id', sa.Integer(), nullable=True),
                    sa.Column('chapter_id', sa.Integer(), nullable=True),
                    sa.Column('verse_number', sa.Integer(), nullable=True),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['book_id'], ['bible_book.id'], ),
                    sa.ForeignKeyConstraint(['chapter_id'], ['bible_chapter.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_bible_verse_book_id'),
                    'bible_verse', ['book_id'], unique=False)
    op.create_index(op.f('ix_bible_verse_chapter_id'),
                    'bible_verse', ['chapter_id'], unique=False)
    op.create_index(op.f('ix_bible_verse_id'), 'bible_verse', ['id'], unique=False)
    op.create_index(op.f('ix_bible_verse_verse_number'),
                    'bible_verse', ['verse_number'], unique=False)
    op.add_column('bible_book', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('bible_chapter', sa.Column(
        'created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bible_chapter', 'created_at')
    op.drop_column('bible_book', 'created_at')
    op.drop_index(op.f('ix_bible_verse_verse_number'), table_name='bible_verse')
    op.drop_index(op.f('ix_bible_verse_id'), table_name='bible_verse')
    op.drop_index(op.f('ix_bible_verse_chapter_id'), table_name='bible_verse')
    op.drop_index(op.f('ix_bible_verse_book_id'), table_name='bible_verse')
    op.drop_table('bible_verse')
    # ### end Alembic commands ###
