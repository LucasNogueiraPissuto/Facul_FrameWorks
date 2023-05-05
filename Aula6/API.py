from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/mensagem')
def home():
    return "teste"

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        'id': 2,
        'name': "task2",
        "description": "This is task 2"
    }
]


@app.route('/api/tasks/')
def get_task():
    tasksJSON = jsonify(tasks)
    tasksJSON.headers.add("Access-Control-Allow-Origin", "*")
    tasksJSON.headers.add("Content-Type", "application/json")
    return tasksJSON

if __name__=='__main__':
    app.run()