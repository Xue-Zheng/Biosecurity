import json
import os

from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import re
from flask_hashing import Hashing

from connect import conn

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    hashing = Hashing(app)
    test_config = {
        'SECRET_KEY': 'dev',
    }
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # Output message if something goes wrong...
        msg = ''
        # Check if "username" and "password" POST requests exist (user submitted form)
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # Create variables for easy access
            username = request.form['username']
            password = request.form['password']
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM User WHERE username = %s', (username,))
            # Fetch one record and return result
            account = cursor.fetchone()
            if account is not None:
                db_password = account[2]
                if hashing.check_value(db_password, password):
                # If account exists in accounts table 
                # Create session data, we can access this data in other routes
                    session['loggedin'] = True
                    session['id'] = account[0]
                    session['username'] = account[1]
                    session['email'] = account[3]
                    session['role'] = account[4]
                    # Redirect to home page
                    if session['role'] == 'Admin':
                        return redirect(url_for('page', name='admin'))
                    elif session['role'] == 'PestController':
                        return redirect(url_for('page', name='pestController'))
                    elif session['role'] == 'Staff':
                        return redirect(url_for('page', name='staff'))
                    else:
                        return redirect(url_for('page', name='index'))
                else:
                    #password incorrect
                    msg = 'Incorrect password!'
            else:
                # Account doesnt exist or username incorrect
                msg = 'User {} was not found'.format(username)
        # Show the login form with message (if any)
        return render_template('login.html', msg=msg)

    # http://localhost:5000/register - this will be the registration page, we need to use both GET and POST requests
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        # Output message if something goes wrong...
        msg = ''
        # Check if "username", "password" and "email" POST requests exist (user submitted form)
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            # Create variables for easy access
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            role = request.form.get('role', '')
            first_name = request.form.get('first_name', '')
            last_name = request.form.get('last_name', '')
            pest_controller_id_number = request.form.get('pest_controller_id_number', '')
            
            # Check if account exists using MySQL
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM User WHERE username = %s', (username,))
            account = cursor.fetchone()
            # If account exists show error and validation checks
            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            elif not username or not password or not email:
                msg = 'Please fill out the form!'
            else:
                # create profile first
                if role == 'PestController':
                    pass
                    # cursor.execute('INSERT INTO PestController VALUES (NULL, %s, %s, %s, %s)', (first_name, last_name, pest_controller_id_number, email,))
                else:
                    import random
                    staff_number = random.randint(100000, 999999)
                    # cursor.execute('INSERT INTO StaffAdmin VALUES (NULL, %s, %s, %s, %s)', (staff_number, first_name, last_name, email,))
                conn.commit()
                lastrowid = cursor.lastrowid
                    
                # Account doesnt exists and the form data is valid, now insert new account into accounts table
                hashed_password = hashing.hash_value(password)
                cursor.execute('INSERT INTO User(username, password, email, role)  VALUES (%s, %s, %s, %s)', (username, hashed_password, email, role))
                # cursor.execute('INSERT INTO User VALUES (NULL, %s, %s, %s, %s)', (username, hashed_password, role))
                conn.commit()
                msg = 'You have successfully registered!'
        elif request.method == 'POST':
            # Form is empty... (no POST data)
            msg = 'Please fill out the form!'
        # Show registration form with message (if any)
        return render_template('register.html', msg=msg)

    # http://localhost:5000/logout - this will be the logout page
    @app.route('/logout')
    def logout():
        # Remove session data, this will log the user out
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        session.pop('email', None)
        # Redirect to login page
        return redirect(url_for('page', name='login'))
    
    @app.route('/')
    def home():
        return redirect(url_for('page', name='index'))
    
    @app.route('/page/<name>')
    def page(name):
        data = request.args
        # User is loggedin show them the home page
        if name == 'profile':
            userinfo = {
                'id': session['id'],
                'username': session['username'],
                'email': session['email'],
                'role': session['role']
            }
            return render_template('profile.html', userinfo=userinfo)
        elif name == 'pest':
            animal_id = data.get('animal_id')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM AnimalPest WHERE animal_id = %s', (animal_id,))
            pest = cursor.fetchone()
            data = {
                'pest': pest
            }
            return render_template('{}.html'.format(name), data=data)
        elif name == 'index':
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM AnimalPest limit 30')
            rows = cursor.fetchall()
            pests = [
                {
                    'animal_id': row[0],
                    'description': row[1],
                    'size': row[2],
                    'image':row[8]
                } for row in rows
            ]
            data = {
                'pests': pests,
                'userinfo': session
            }
        elif name == 'admin':
            if 'loggedin' not in session:
                return redirect(url_for('page', name='login'))
            cur = conn.cursor()
            cur.execute('select * from User limit 50')
            rows = cur.fetchall()
            users = [
                {
                    'id': row[0],
                    'username': row[1],
                    'email': row[3],
                    'role': row[4],
                } for row in rows
            ]
            data = {
                'users': users,
            }
        elif name == 'pestController':
            if 'loggedin' not in session:
                return redirect(url_for('page', name='login'))
            cur = conn.cursor()
            cur.execute('select * from AnimalPest limit 50')
            rows = cur.fetchall()
            pests = [
                {
                    'animal_id': row[0],
                    'description': row[1],
                    'size': row[2],
                } for row in rows
            ]
            data = {
                'pests': pests,
            }
        elif name == 'staff':
            if 'loggedin' not in session:
                return redirect(url_for('page', name='login'))
            cur = conn.cursor()
            cur.execute('select * from User where role = %s limit 50', ('PestController',))
            rows = cur.fetchall()
            users = [
                {
                    'id': row[0],
                    'username': row[1],
                    'email': row[3],
                    'role': row[4],
                } for row in rows
            ]
            data = {
                'users': users,
            }
        return render_template('{}.html'.format(name), data=data)
        # User is not loggedin redirect to login page
        return redirect(url_for('page', name='login'))
    
    @app.route('/initdb')
    def init():
        if not conn:
            return 'Unable to connect to database'
        cursor = conn.cursor()
        with app.open_resource('schema.sql', 'r') as f:
            sqls = f.read().split(';')
            for sql in sqls:
                if sql and len(sql) > 10:
                    cursor.execute(sql)
                    conn.commit()
        with app.open_resource('init.sql', 'r') as f:
            sqls = f.read().split(';')
            for sql in sqls:
                if sql and len(sql) > 10:
                    cursor.execute(sql)
                    conn.commit()
        return 'success'

    from controllers.animalPest import animal_pest_bp
    from controllers.pestController import pest_controller_bp
    from controllers.staffAdmin import staff_admin_bp
    from controllers.user import user_bp
    app.register_blueprint(animal_pest_bp, url_prefix='/animal_pest')
    app.register_blueprint(pest_controller_bp, url_prefix='/pest_controller')
    app.register_blueprint(staff_admin_bp, url_prefix='/staff_admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

if __name__ == "__main__":
    global app
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
