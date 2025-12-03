import re
from datetime import datetime

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_string(value, min_length=1, max_length=255):
    if not isinstance(value, str):
        return False
    return min_length <= len(value.strip()) <= max_length

def validate_task_data(data):
    errors = []
    
    if not data:
        errors.append('Data is required')
        return False, errors
    
    if 'title' not in data:
        errors.append('Title is required')
    
    if 'title' in data and not is_valid_string(data['title'], 1, 200):
        errors.append('Title must be between 1 and 200 characters')
    
    return len(errors) == 0, errors

def validate_user_data(data):
    errors = []
    
    if not data:
        errors.append('Data is required')
        return False, errors
    
    if 'name' not in data:
        errors.append('Name is required')
    
    if 'email' not in data:
        errors.append('Email is required')
    elif not is_valid_email(data['email']):
        errors.append('Invalid email format')
    
    if 'name' in data and not is_valid_string(data['name'], 1, 100):
        errors.append('Name must be between 1 and 100 characters')
    
    return len(errors) == 0, errors

def sanitize_input(text):
    if not isinstance(text, str):
        return str(text)
    return text.strip()

