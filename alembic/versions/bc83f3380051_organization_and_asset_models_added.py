"""organization and asset models added

Revision ID: bc83f3380051
Revises: 067c23cce4a0
Create Date: 2021-11-08 23:02:22.435218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc83f3380051'
down_revision = '067c23cce4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_organization_id'),
                    'organization', ['id'], unique=False)
    op.create_table('broadcast',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('subtitle', sa.String(), nullable=True),
                    sa.Column('thumbnail', sa.LargeBinary(
                        length=4294967295), nullable=True),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('scheduled_time', sa.DateTime(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_broadcast_author_id'),
                    'broadcast', ['author_id'], unique=False)
    op.create_index(op.f('ix_broadcast_id'), 'broadcast', ['id'], unique=False)
    op.create_table('organization_user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('organization_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['organization_id'], [
                                            'organization.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_organization_user_id'),
                    'organization_user', ['id'], unique=False)
    op.create_index(op.f('ix_organization_user_organization_id'),
                    'organization_user', ['organization_id'], unique=False)
    op.create_index(op.f('ix_organization_user_user_id'),
                    'organization_user', ['user_id'], unique=False)
    op.create_table('asset',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('broadcast_id', sa.Integer(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['broadcast_id'], ['broadcast.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_asset_broadcast_id'), 'asset',
                    ['broadcast_id'], unique=False)
    op.create_index(op.f('ix_asset_id'), 'asset', ['id'], unique=False)
    op.create_table('broadcast_stats',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('broadcast_id', sa.Integer(), nullable=True),
                    sa.Column('views', sa.Integer(), nullable=True),
                    sa.Column('likes', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['broadcast_id'], ['broadcast.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_broadcast_stats_broadcast_id'),
                    'broadcast_stats', ['broadcast_id'], unique=False)
    op.create_index(op.f('ix_broadcast_stats_id'),
                    'broadcast_stats', ['id'], unique=False)
    op.create_table('broadcasts_queue',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('broadcast_id', sa.Integer(), nullable=True),
                    sa.Column('scheduled_time', sa.DateTime(), nullable=True),
                    sa.Column('audience', sa.String(), nullable=True),
                    sa.Column('is_broadcast', sa.Boolean(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['broadcast_id'], ['broadcast.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_broadcasts_queue_broadcast_id'),
                    'broadcasts_queue', ['broadcast_id'], unique=False)
    op.create_index(op.f('ix_broadcasts_queue_id'),
                    'broadcasts_queue', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_broadcasts_queue_id'),
                  table_name='broadcasts_queue')
    op.drop_index(op.f('ix_broadcasts_queue_broadcast_id'),
                  table_name='broadcasts_queue')
    op.drop_table('broadcasts_queue')
    op.drop_index(op.f('ix_broadcast_stats_id'), table_name='broadcast_stats')
    op.drop_index(op.f('ix_broadcast_stats_broadcast_id'),
                  table_name='broadcast_stats')
    op.drop_table('broadcast_stats')
    op.drop_index(op.f('ix_asset_id'), table_name='asset')
    op.drop_index(op.f('ix_asset_broadcast_id'), table_name='asset')
    op.drop_table('asset')
    op.drop_index(op.f('ix_organization_user_user_id'),
                  table_name='organization_user')
    op.drop_index(op.f('ix_organization_user_organization_id'),
                  table_name='organization_user')
    op.drop_index(op.f('ix_organization_user_id'),
                  table_name='organization_user')
    op.drop_table('organization_user')
    op.drop_index(op.f('ix_broadcast_id'), table_name='broadcast')
    op.drop_index(op.f('ix_broadcast_author_id'), table_name='broadcast')
    op.drop_table('broadcast')
    op.drop_index(op.f('ix_organization_id'), table_name='organization')
    op.drop_table('organization')
    # ### end Alembic commands ###
