import json
import os
from datetime import datetime
from google.cloud import storage
from google.cloud import logging as cloud_logging

def process_request(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    name = request_json.get('name', '') if request_json else request_args.get('name', 'World')
    
    result = {
        'greeting': f'Hello, {name}!',
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('ENVIRONMENT', 'production'),
        'method': request.method
    }
    
    return json.dumps(result), 200, {'Content-Type': 'application/json'}

def storage_handler(request):
    bucket_name = os.environ.get('BUCKET_NAME', 'default-bucket')
    
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        
        blobs = list(bucket.list_blobs(max_results=10))
        file_list = [blob.name for blob in blobs]
        
        response = {
            'bucket': bucket_name,
            'files': file_list,
            'count': len(file_list),
            'timestamp': datetime.now().isoformat()
        }
        
        return json.dumps(response), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json'}

def data_processor(request):
    if request.method != 'POST':
        return json.dumps({'error': 'Method not allowed'}), 405, {'Content-Type': 'application/json'}
    
    request_json = request.get_json(silent=True)
    if not request_json:
        return json.dumps({'error': 'Invalid JSON'}), 400, {'Content-Type': 'application/json'}
    
    data = request_json.get('data', [])
    processed = {
        'sum': sum(data) if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data) else 0,
        'count': len(data) if isinstance(data, list) else 0,
        'processed_at': datetime.now().isoformat()
    }
    
    return json.dumps(processed), 200, {'Content-Type': 'application/json'}

