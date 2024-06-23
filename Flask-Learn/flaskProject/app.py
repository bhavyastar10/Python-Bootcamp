from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'test',
}

# making connection and initialise conn object
db_conn = pymysql.connect(**db_config)
cursor = db_conn.cursor()


# Get call for items inside infos
@app.route('/infos', methods=['GET'])
def get_items():
    try:
        cursor.execute('Select * from infos')
        items = [{'id': id, 'name': name, 'surname': surname} for id, name, surname in cursor.fetchall()]
        return jsonify(items)
    except Exception as e:
        return jsonify({'error': str(e)})


# Post call to insert name and surname into table
@app.route('/infos', methods=['POST'])
def insert_items():
    try:
        data = request.get_json()
        # id = data.get('id')
        name = data.get('name')
        surname = data.get('surname')
        cursor.execute('INSERT INTO infos (name, surname) VALUES (%s, %s)', (name, surname))
        db_conn.commit()
        return jsonify({'message': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Put call to update name inside table
@app.route('/infos/<int:id>', methods=['PUT'])
def update_items(id):
    try:
        data = request.get_json()
        name = data.get('name')
        cursor.execute('UPDATE infos SET name = %s WHERE id = %s', (name, id))
        db_conn.commit()
        return jsonify({'message': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Delete call to delete row with specific id
@app.route('/infos/<int:id>', methods=['DELETE'])
def delete_items(id):
    try:
        cursor.execute('DELETE * FROM infos WHERE id = %s', (id))
        db_conn.commit()
        return jsonify({'message': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})


#
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
