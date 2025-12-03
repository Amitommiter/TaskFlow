import json
import time
from datetime import datetime

class TaskWorker:
    def __init__(self):
        self.queue = []
        self.completed = []
    
    def add_task(self, task_data):
        task = {
            'id': f"task_{int(time.time())}",
            'data': task_data,
            'status': 'pending',
            'created_at': datetime.now().isoformat()
        }
        self.queue.append(task)
        return task
    
    def process_next(self):
        if not self.queue:
            return None
        
        task = self.queue.pop(0)
        task['status'] = 'processing'
        task['started_at'] = datetime.now().isoformat()
        
        time.sleep(0.1)
        
        task['status'] = 'completed'
        task['completed_at'] = datetime.now().isoformat()
        self.completed.append(task)
        
        return task
    
    def get_status(self):
        return {
            'pending': len([t for t in self.queue if t['status'] == 'pending']),
            'processing': len([t for t in self.queue if t['status'] == 'processing']),
            'completed': len(self.completed),
            'total': len(self.queue) + len(self.completed)
        }
    
    def get_task(self, task_id):
        all_tasks = self.queue + self.completed
        return next((t for t in all_tasks if t['id'] == task_id), None)

