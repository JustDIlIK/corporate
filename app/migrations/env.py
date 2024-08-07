import sys
from logging.config import fileConfig
from os.path import dirname, abspath

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.database import Base, DATABASE_URL

from app.achievement.model import Achievement
from app.calculation.model import Calculation
from app.client.model import Client
from app.company.model import Company
from app.direction.model import Direction
from app.employee.model import Employee
from app.feature.model import Feature
from app.feedback.model import Feedback
from app.lang.model import Lang
from app.link.model import Link
from app.project.model import Project
from app.service.model import Service
from app.technology.model import Technology
from app.user.models import User
from app.visitor.model import Visitor
from app.statistic.model import Statistic
from app.consideration.model import Consideration

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", f"{DATABASE_URL}?async_fallback=True")
# Interpret the config.py file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config.py, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.py.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
