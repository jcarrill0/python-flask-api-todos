from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": True },
    { "label": "My second task", "done": True }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data) # decodificar el request
    todos.append(decoded_object) # Add decode_object to todoList 
    
    # Retornamos las lista con todos los elemtos del todos
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position - 1)
    # print("This is the position to delete: ", position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)