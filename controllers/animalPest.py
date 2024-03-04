# from flask import Blueprint, jsonify
# from connect import conn
    
# animal_pest_bp = Blueprint('animal_pest_bp', __name__)

# @animal_pest_bp.route('/animal_pest', methods=['POST'])
# def create_animal_pest():
#     # SQL query to insert a new animal pest
#     sql = """
#     INSERT INTO AnimalPest (description, distribution, size, droppings, footprints, impacts, control_methods, images)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
#     """
#     # Execute the SQL query with the relevant values
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, ('Description of animal', 'Distribution area', 'Size of animal', 'Description of droppings', 'Description of footprints', 'Impacts', 'Control methods', 'image_url'))
#     return 'Created a new animal pest'

# @animal_pest_bp.route('/animal_pest/<int:animal_id>', methods=['GET'])
# def get_animal_pest(animal_id):
#     # SQL query to get animal pest by id
#     sql = "SELECT * FROM AnimalPest WHERE animal_id = %s;"
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     # Execute the SQL query and get the result
#     record = cursor.execute(sql, (animal_id,))
#     res = {
#         'animal_id': record.animal_id,
#         'description': record.description
#     }
#     return jsonify(res)

# @animal_pest_bp.route('/animal_pest/<int:animal_id>', methods=['PUT'])
# def update_animal_pest(animal_id):
#     # SQL query to update an animal pest
#     sql = """
#     UPDATE AnimalPest
#     SET description = %s, distribution = %s, size = %s, droppings = %s, footprints = %s,
#         impacts = %s, control_methods = %s, images = %s
#     WHERE animal_id = %s;
#     """
#     # Execute the SQL query with the new values
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, ('Updated description of animal', 'Updated distribution area', 'Updated size of animal', 'Updated description of droppings', 'Updated description of footprints', 'Updated impacts', 'Updated control methods', 'updated_image_url', animal_id))
#     return 'Updated animal pest'

# @animal_pest_bp.route('/animal_pest/<int:animal_id>', methods=['DELETE'])
# def delete_animal_pest(animal_id):
#     # SQL query to delete an animal pest
#     sql = "DELETE FROM AnimalPest WHERE animal_id = %s;"
#     # Execute the SQL query
#     cursor = None
#     if conn:
#         cursor = conn.cursor()
#     cursor.execute(sql, (animal_id,))
#     return 'Deleted animal pest'
