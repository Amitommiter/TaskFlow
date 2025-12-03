from datetime import datetime
import hashlib

class User:
    def __init__(self, name, email):
        self.id = hashlib.md5(f"{name}{email}".encode()).hexdigest()[:8]
        self.name = name
        self.email = email
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now().isoformat()

class Task:
    def __init__(self, title, description=None):
        self.id = hashlib.md5(f"{title}{datetime.now()}".encode()).hexdigest()[:8]
        self.title = title
        self.description = description
        self.status = 'pending'
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def mark_complete(self):
        self.status = 'completed'
        self.updated_at = datetime.now().isoformat()
    
    def mark_in_progress(self):
        self.status = 'in_progress'
        self.updated_at = datetime.now().isoformat()

