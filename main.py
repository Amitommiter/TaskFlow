import json
from datetime import datetime
import os

def hello_world(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    name = request_json.get('name', '') if request_json else request_args.get('name', 'World')
    
    response_data = {
        'message': f'Hello from GCP Cloud Function, {name}!',
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'project_id': os.environ.get('GCP_PROJECT', 'unknown')
    }
    
    return json.dumps(response_data), 200, {'Content-Type': 'application/json'}

def process_data(request):
    if request.method != 'POST':
        return json.dumps({'error': 'Method not allowed'}), 405, {'Content-Type': 'application/json'}
    
    request_json = request.get_json(silent=True)
    if not request_json:
        return json.dumps({'error': 'Invalid JSON'}), 400, {'Content-Type': 'application/json'}
    
    data = request_json.get('data', [])
    result = {
        'sum': sum(data) if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data) else 0,
        'count': len(data) if isinstance(data, list) else 0,
        'processed_at': datetime.now().isoformat()
    }
    
    return json.dumps(result), 200, {'Content-Type': 'application/json'}

