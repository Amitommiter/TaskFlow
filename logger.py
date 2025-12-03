import logging
import os
from datetime import datetime

class CloudLogger:
    def __init__(self, name='gcp-app'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def log_request(self, method, path, status_code, duration_ms=None):
        log_data = {
            'method': method,
            'path': path,
            'status': status_code,
            'timestamp': datetime.now().isoformat()
        }
        if duration_ms:
            log_data['duration_ms'] = duration_ms
        
        self.info(f"Request: {method} {path} - Status: {status_code}")

logger = CloudLogger()

