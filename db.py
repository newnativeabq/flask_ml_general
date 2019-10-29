"""
Database
    Initialize and create connection control flow for database.
    Datase parameters must be set in config.py or directly in app.py
"""


import sqlite3
import pandas

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Returns current database connection.  If connection not present,
    initiates connection to configured database.
    """
    if 'db' not in g:
        try:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES,
            )

        except:
            g.db = sqlite3.connect(
                current_app.config['LOCALDATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES,
            )

        g.db.row_factory = sqlite3.Row

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