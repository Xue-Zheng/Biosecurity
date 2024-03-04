# import json
# import sqlite3

# import click
# from flask import current_app, g
# from connect import conn
# from user import USER_INFO


# def get_db(app):
#     if 'db' not in g:
#         g.db = conn
#     return g.db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()
        
        
# def init_db(conn):
#     with current_app.open_resource('schema.sql') as f:
#         cursor = conn.cursor()
#         sql = f.read().decode('utf8')
#         cursor.execute(sql)
#         conn.commit()

# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)


# @click.command('init-db')
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     # init_data()
#     click.echo('Initialized the database.')

# def init_data(conn):
#     cursor = conn.cursor()
#     sql = """
#         INSERT INTO user (full_name, user_info) VALUES (?,?)
#     """
#     user_info = json.dumps(USER_INFO)
#     cursor.execute(sql, ('Your Full Name', user_info))
#     click.echo('Initialized user data.')
#     conn.commit()