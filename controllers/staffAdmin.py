# from flask import Blueprint, jsonify
# from connect import conn
    
# staff_admin_bp = Blueprint('staff_admin_bp', __name__)

# @staff_admin_bp.route('/staff_admin', methods=['POST'])
# def create_staff_admin():
#     # SQL query to insert a new staff admin
#     sql = """
#     INSERT INTO StaffAdmin (staff_number, first_name, last_name, email,
#                            work_phone_number, hire_date, position, department, status)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
#     """
#     # Execute the SQL query with the relevant values
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, ('SA123456', 'John', 'Doe', 'johndoe@email.com', '1234567890', '2021-01-01', 'Manager', 'IT', 'active'))
#     return 'Created a new staff admin'

# @staff_admin_bp.route('/staff_admin/<int:id>', methods=['GET'])
# def get_staff_admin(id):
#     # SQL query to get staff admin by id
#     sql = "SELECT * FROM StaffAdmin WHERE id = %s;"
#     # Execute the SQL query and get the result
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     record = cursor.execute(sql, (id,))
#     res = {
#         'id': record.id,
#         'staff_number': record.staff_number,
#         'first_name': record.first_name,
#         'last_name': record.last_name,
#     }
#     return jsonify(res)

# @staff_admin_bp.route('/staff_admin/<int:id>', methods=['PUT'])
# def update_staff_admin(id):
#     # SQL query to update a staff admin
#     sql = """
#     UPDATE StaffAdmin
#     SET first_name = %s, last_name = %s, email = %s, work_phone_number = %s,
#         position = %s, department = %s, status = %s
#     WHERE id = %s;
#     """
#     # Execute the SQL query with the new values
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, ('Jane', 'Doe', 'janedoe@email.com', '0987654321', 'Assistant Manager', 'HR', 'inactive', id))
#     return 'Updated staff admin'

# @staff_admin_bp.route('/staff_admin/<int:id>', methods=['DELETE'])
# def delete_staff_admin(id):
#     # SQL query to delete a staff admin
#     sql = "DELETE FROM StaffAdmin WHERE id = %s;"
#     # Execute the SQL query
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, (id,))
#     return 'Deleted staff admin'