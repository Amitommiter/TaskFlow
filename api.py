from flask import Flask, jsonify, request
from datetime import datetime
import os
import hashlib
from handlers import handle_task_request, handle_task_by_id, handle_user_request, handle_worker_status, handle_process_task
from config import Config

app = Flask(__name__)

tasks = []
user_data = {}

@app.route('/')
def index():
    return jsonify({
        'service': 'TaskFlow',
        'version': '1.0.0',
        'status': 'running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        data['id'] = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]
        data['created_at'] = datetime.now().isoformat()
        tasks.append(data)
        return jsonify(data), 201
    
    return jsonify({
        'tasks': tasks,
        'count': len(tasks)
    })

@app.route('/api/data/<task_id>', methods=['GET', 'DELETE'])
def handle_task(task_id):
    task = next((t for t in tasks if t.get('id') == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    if request.method == 'DELETE':
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'}), 200
    
    return jsonify(task)

@app.route('/api/stats')
def stats():
    return jsonify({
        'total_tasks': len(tasks),
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('ENVIRONMENT', 'production')
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id') or hashlib.md5(data.get('name', '').encode()).hexdigest()[:8]
    user_data[user_id] = {
        'id': user_id,
        'name': data.get('name'),
        'email': data.get('email'),
        'created_at': datetime.now().isoformat()
    }
    return jsonify(user_data[user_id]), 201

@app.route('/api/users/<user_id>')
def get_user(user_id):
    user = user_data.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/api/config')
def get_config():
    return jsonify(Config.to_dict())

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks_endpoint():
    return handle_task_request()

@app.route('/api/tasks/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_by_id_endpoint(task_id):
    return handle_task_by_id(task_id)

@app.route('/api/worker/status')
def worker_status():
    return handle_worker_status()

@app.route('/api/worker/process', methods=['POST'])
def process_worker_task():
    return handle_process_task()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.APP_ENGINE_PORT, debug=True)

