"""empty message

Revision ID: 42c45e74752b
Revises: osmus2
Create Date: 2023-03-29 09:07:55.771834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "42c45e74752b"
down_revision = "osmus2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("application_keys", schema=None) as batch_op:
        batch_op.alter_column("id", existing_type=sa.INTEGER(), type_=sa.BigInteger())

    with op.batch_alter_table("priority_areas", schema=None) as batch_op:
        batch_op.create_geospatial_index(
            "idx_priority_areas_geometry",
            ["geometry"],
            unique=False,
            postgresql_using="gist",
            postgresql_ops={},
        )

    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.create_geospatial_index(
            "idx_tasks_geometry",
            ["geometry"],
            unique=False,
            postgresql_using="gist",
            postgresql_ops={},
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.drop_geospatial_index(
            "idx_tasks_geometry", postgresql_using="gist", column_name="geometry"
        )

    with op.batch_alter_table("priority_areas", schema=None) as batch_op:
        batch_op.drop_geospatial_index(
            "idx_priority_areas_geometry",
            postgresql_using="gist",
            column_name="geometry",
        )

    with op.batch_alter_table("application_keys", schema=None) as batch_op:
        batch_op.alter_column("id", existing_type=sa.BigInteger(), type_=sa.INTEGER())

    # ### end Alembic commands ###
