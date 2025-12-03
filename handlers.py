from flask import request, jsonify
from datetime import datetime
from worker import TaskWorker
from models import User, Task
from validator import validate_task_data, validate_user_data
import json

worker = TaskWorker()
users = {}
tasks = {}

def handle_task_request():
    if request.method == 'POST':
        data = request.get_json()
        is_valid, errors = validate_task_data(data)
        if not is_valid:
            return jsonify({'error': 'Validation failed', 'errors': errors}), 400
        
        task = Task(data.get('title'), data.get('description'))
        tasks[task.id] = task
        return jsonify(task.to_dict()), 201
    
    task_list = [task.to_dict() for task in tasks.values()]
    return jsonify({'tasks': task_list, 'count': len(task_list)})

def handle_task_by_id(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    if request.method == 'PUT':
        data = request.get_json()
        if data.get('status') == 'completed':
            task.mark_complete()
        elif data.get('status') == 'in_progress':
            task.mark_in_progress()
        return jsonify(task.to_dict())
    
    if request.method == 'DELETE':
        del tasks[task_id]
        return jsonify({'message': 'Task deleted'}), 200
    
    return jsonify(task.to_dict())

def handle_user_request():
    if request.method == 'POST':
        data = request.get_json()
        is_valid, errors = validate_user_data(data)
        if not is_valid:
            return jsonify({'error': 'Validation failed', 'errors': errors}), 400
        
        user = User(data.get('name'), data.get('email'))
        users[user.id] = user
        return jsonify(user.to_dict()), 201
    
    user_list = [user.to_dict() for user in users.values()]
    return jsonify({'users': user_list, 'count': len(user_list)})

def handle_worker_status():
    status = worker.get_status()
    return jsonify(status)

def handle_process_task():
    task = worker.process_next()
    if task:
        return jsonify(task), 200
    return jsonify({'message': 'No tasks in queue'}), 404

