from flask import Flask, request
import json

app = Flask(__name__)

task = [
    {
        "id": 0,
        "tarefa": "Jogar o lixo fora",
        "status": "Não Concluido",
        "responsavel": "Jorge"
    }
]

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        data = json.loads(request.data)
        data["id"] = len(task)
        task.append(data)
        return "OK!"
    elif request.method == "GET":
        return json.dumps(task)

@app.route("/tasks/<int:id>", methods=["GET", "PUT", "DELETE"])
def control_tasks(id):
    if request.method == "GET":
        try:
            return task[id]
        except IndexError:
            return "No task with this id."
    elif request.method == "PUT":
        try:
            data = json.loads(request.data)
            if "status" in data and data["status"] != task[id]["status"] :
                task[id]["status"] = data["status"]
                return "OK!"
            else:
                return "No change is expected unless \"status\"."
        except IndexError:
            return "No task with this id."
    elif request.method == "DELETE":
        try:
            task.pop(id)
            return "OK!"
        except IndexError:
            return "No task with this id."

if __name__ == '__main__':
    app.run(debug=True)