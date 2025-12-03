from google.cloud import storage
import os
import json

class StorageService:
    def __init__(self, bucket_name=None):
        self.bucket_name = bucket_name or os.environ.get('BUCKET_NAME', 'default-bucket')
        self.client = storage.Client()
        self.bucket = self.client.bucket(self.bucket_name)
    
    def list_files(self, prefix=None, max_results=100):
        try:
            blobs = self.bucket.list_blobs(prefix=prefix, max_results=max_results)
            return [{
                'name': blob.name,
                'size': blob.size,
                'content_type': blob.content_type,
                'created': blob.time_created.isoformat() if blob.time_created else None
            } for blob in blobs]
        except Exception as e:
            return {'error': str(e)}
    
    def upload_file(self, file_content, destination_blob_name, content_type='application/octet-stream'):
        try:
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_string(file_content, content_type=content_type)
            return {
                'success': True,
                'blob_name': destination_blob_name,
                'bucket': self.bucket_name
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def download_file(self, source_blob_name):
        try:
            blob = self.bucket.blob(source_blob_name)
            return blob.download_as_text()
        except Exception as e:
            return {'error': str(e)}
    
    def delete_file(self, blob_name):
        try:
            blob = self.bucket.blob(blob_name)
            blob.delete()
            return {'success': True, 'deleted': blob_name}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def file_exists(self, blob_name):
        blob = self.bucket.blob(blob_name)
        return blob.exists()

