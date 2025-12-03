import os
from datetime import datetime, timedelta
import json

def get_environment_config():
    return {
        'project_id': os.environ.get('GCP_PROJECT_ID', 'my-gcp-project'),
        'region': os.environ.get('GCP_REGION', 'us-central1'),
        'environment': os.environ.get('ENVIRONMENT', 'production')
    }

def format_timestamp(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()

def calculate_time_difference(start_time, end_time=None):
    if end_time is None:
        end_time = datetime.now()
    
    if isinstance(start_time, str):
        start_time = datetime.fromisoformat(start_time)
    if isinstance(end_time, str):
        end_time = datetime.fromisoformat(end_time)
    
    difference = end_time - start_time
    return {
        'total_seconds': difference.total_seconds(),
        'days': difference.days,
        'hours': difference.seconds // 3600,
        'minutes': (difference.seconds % 3600) // 60
    }

def validate_json(data):
    try:
        if isinstance(data, str):
            json.loads(data)
        return True
    except:
        return False

def generate_response(data, status_code=200):
    return {
        'data': data,
        'status': 'success' if status_code < 400 else 'error',
        'timestamp': format_timestamp()
    }

