from flask import Flask, request, jsonify


@Todo.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

Todo = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 20
    },
    {
        "id": 2,
        "name": "Jane ",
        "age": 22
    },
    {
        "id": 3,
        "name": "Bob Smith",
        "age": 21
    }
]
@Todo.route('/students-list')
def students_list():
    return jsonify(students)

@Todo.route('/students/get/<int:id>')
def get_students_by_id(id):
      print(id)
      for student in students:
            if student['id'] == id:
                  return jsonify(student)
      return jsonify('student not found')
      

if __name__ == '__main__':
        Todo.run(debug=True)
