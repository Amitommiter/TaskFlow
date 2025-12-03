import os

class Config:
    PROJECT_ID = os.environ.get('GCP_PROJECT_ID', 'my-gcp-project')
    REGION = os.environ.get('GCP_REGION', 'us-central1')
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'production')
    BUCKET_NAME = os.environ.get('BUCKET_NAME', 'default-bucket')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    APP_ENGINE_PORT = int(os.environ.get('PORT', 8080))
    
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')
    
    MAX_REQUEST_SIZE = int(os.environ.get('MAX_REQUEST_SIZE', 10485760))
    
    @classmethod
    def to_dict(cls):
        return {
            'project_id': cls.PROJECT_ID,
            'region': cls.REGION,
            'environment': cls.ENVIRONMENT,
            'bucket_name': cls.BUCKET_NAME
        }

