from flask import Blueprint, request, jsonify, abort
from connect import conn

user_bp = Blueprint('user_bp', __name__)

# Create User
@user_bp.route('/user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    profile_id = request.json.get('profile_id')
    
    if not username or not password or not role or not profile_id:
        abort(400, 'Missing required fields')
    
    cur = conn.cursor()
    
    try:
        cur.execute("INSERT INTO User(username, password, role, profile_id) VALUES(%s, %s, %s, %s)", (username, password, role, profile_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        abort(500, str(e))
    finally:
        cur.close()
    
    return jsonify(message='User created successfully'), 201

# Retrieve User
@user_bp.route('/user/<int:user_id>', methods=['GET'])
def retrieve_user(user_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM User WHERE id = %s", (user_id,))
    
    user_data = cur.fetchone()
    cur.close()
    
    if user_data:
        user = {
            'id' : user_data[0],
            'username' : user_data[1],
            'role' : user_data[3],
            'profile_id' : user_data[4]
        }
        return jsonify(user)
    else:
        abort(404, "User not found")

# Update User
@user_bp.route('/update', methods=['POST'])
def update_user():
    print(request.form)
    userid = request.form.get('userid')
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    profile_id = request.form.get('profile_id')
    
    cur = conn.cursor()
    
    try:
        if password:
            cur.execute("UPDATE User SET password = %s WHERE id = %s", (password, userid))
        if username or role or profile_id:
            update_data = []
            update_fields = ''
            if username:
                update_fields += 'username = %s, '
                update_data.append(username)
            if role:
                update_fields += 'role = %s, '
                update_data.append(role)
            if profile_id:
                update_fields += 'profile_id = %s, '
                update_data.append(profile_id)
            update_data.append(userid)

            # Remove trailing comma
            update_fields = update_fields.rstrip(', ')

            cur.execute(f"UPDATE User SET {update_fields} WHERE id = %s", update_data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        abort(500, str(e))

    cur.close()
    return jsonify(message='User updated successfully'), 200

# Delete User
@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM User WHERE id = %s", (user_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        abort(500, str(e))
    finally:
        cur.close()
    
    return jsonify(message='User deleted successfully'), 200
