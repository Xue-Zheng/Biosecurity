from flask import Blueprint, jsonify, render_template
from connect import conn
    
pest_controller_bp = Blueprint('pest_controller_bp', __name__)


@pest_controller_bp.route('/pest_controller', methods=['POST'])
def create_pest_controller():
    # SQL query to insert a new pest controller
    sql = """
    INSERT INTO PestController (first_name, last_name, pest_controller_id_number, address,
                                email, phone_number, date_joined, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    # Execute the SQL query with the relevant values
    cursor = None
    if conn:
        cursor = conn.cursor()
    cursor.execute(sql, ('John', 'Doe', 'PC123456', '123 Main St', 'johndoe@email.com', '1234567890', '2021-01-01', 'active'))
    return 'Created a new pest controller'

@pest_controller_bp.route('/pest_controller/<int:id>', methods=['GET'])
def get_pest_controller(id):
    # SQL query to get pest controller by id
    sql = "SELECT * FROM PestController WHERE id = %s;"
    # Execute the SQL query and get the result
    cursor = None
    if conn:
        cursor = conn.cursor()
    record = cursor.execute(sql, (id,))
    res = {
        'id': record.id,
        'first_name': record.first_name,
        'last_name': record.last_name,
    }
    return render_template('pest.html', pest=res)

@pest_controller_bp.route('/pest_controller/<int:id>', methods=['PUT'])
def update_pest_controller(id):
    # SQL query to update a pest controller
    sql = """
    UPDATE PestController
    SET first_name = %s, last_name = %s, address = %s, email = %s, phone_number = %s,
        status = %s
    WHERE id = %s;
    """
    # Execute the SQL query with the new values
    cursor = None
    if conn:
        cursor = conn.cursor()
    cursor.execute(sql, ('Jane', 'Doe', '456 Elm St', 'janedoe@email.com', '0987654321', 'inactive', id))
    return 'Updated pest controller'

@pest_controller_bp.route('/pest_controller/<int:id>', methods=['DELETE'])
def delete_pest_controller(id):
    # SQL query to delete a pest controller
    sql = "DELETE FROM PestController WHERE id = %s;"
    # Execute the SQL query
    cursor = None
    if conn:
        cursor = conn.cursor()
    cursor.execute(sql, (id,))
    return 'Deleted pest controller'