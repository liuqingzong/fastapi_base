"""empty message

Revision ID: e2beabea644f
Revises: 
Create Date: 2024-11-22 00:10:22.609950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2beabea644f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sys_user',
    sa.Column('id', sa.String(length=32), nullable=False, comment='主键id'),
    sa.Column('username', sa.String(length=20), nullable=False, comment='用户名'),
    sa.Column('create_user', sa.String(length=20), nullable=False, comment='创建人'),
    sa.Column('update_user', sa.String(length=20), nullable=False, comment='修改人'),
    sa.Column('create_time', sa.DateTime(), nullable=False, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=False, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sys_user_id'), 'sys_user', ['id'], unique=False)
    op.create_index(op.f('ix_sys_user_username'), 'sys_user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sys_user_username'), table_name='sys_user')
    op.drop_index(op.f('ix_sys_user_id'), table_name='sys_user')
    op.drop_table('sys_user')
    # ### end Alembic commands ###