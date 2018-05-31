import click
import logging
from sqlalchemy import func
from alembic import command
from ether_sql.models import base, Blocks
from ether_sql.session import setup_alembic_config


logger = logging.getLogger(__name__)


@click.group()
@click.pass_context
def sql(ctx):
    """Manages the sql (create/drop/query tables)."""


@sql.command()
@click.pass_context
def create_tables(ctx):
    """Create the database tables."""
    session = ctx.obj['session']
    logger.debug("{}".format(session.db_engine.url))
    base.metadata.create_all(session.db_engine)
    logger.info('Created the tables')


@sql.command()
@click.pass_context
def drop_tables(ctx):
    """Drop the database tables."""
    session = ctx.obj['session']
    logger.debug("{}".format(session.db_engine.url))
    base.metadata.drop_all(session.db_engine)
    logger.info('Dropped the tables')


@sql.command()
@click.pass_context
def blockNumber(ctx):
    """ Gives the current highest block in database"""
    session = ctx.obj['session']
    max_block_number = session.db_session.query(func.max(Blocks.block_number)).scalar()
    click.echo("{}".format(max_block_number))


@sql.command()
@click.option('-m', default=None,
              help='Write a message specifying what changed')
@click.pass_context
def migrate(ctx, m):
    """ Alias for 'alembic revision --autogenerate'
    Run this command after changing sql tables
    """
    if m is None:
        click.echo(ctx.get_help())
    else:
        command.revision(setup_alembic_config(url=ctx.obj['session'].url),
                         message=m, autogenerate=True, sql=None)


@sql.command()
@click.pass_context
def upgrade(ctx):
    """ Alias for 'alembic upgrade head'.
    Upgrade to latest model version
    """
    command.upgrade(setup_alembic_config(url=ctx.obj['session'].url),
                    revision='head', sql=False, tag=None)
