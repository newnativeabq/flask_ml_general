"""
Database
    Initialize and create connection control flow for database.
    Datase parameters must be set in config.py or directly in app.py
"""


from sqlalchemy import create_engine

import click
from flask import current_app, g
from flask.cli import with_appcontext

import logging


def get_db():
    """
    Returns current database connection.  If connection not present,
    initiates connection to configured database.  Default is non-authenticated SQL.
    Modifty g.db = *connect to match intended database connection.
    """
    db_logger = logging.getLogger(__name__ + '.getdb')
    if 'db' not in g:
        db_logger.info('DB connection not found. Attempting connection.')
        try:
            engine = create_engine(current_app.config['DATABASE'])
            g.db = engine.connect()

        except:
            db_logger.error('Could not establish connection.  Aborting.')
            raise ConnectionError

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

def query_database(query_string):
    """
    General function for querying matching data from predictors.
    """
    raise NotImplementedError