# TaskFlow

A comprehensive Google Cloud Platform (GCP) project featuring a RESTful API for task and user management, deployable on App Engine and Cloud Functions.

## Features

- RESTful API with Flask
- Task Management System (CRUD operations)
- User Management with validation
- Background Task Worker Queue
- Google Cloud Storage Integration
- Cloud Functions support
- Input validation and error handling
- Logging and monitoring
- Configuration management

## Project Structure

```
.
├── api.py                 # Main Flask API application
├── app_engine.py          # Simple App Engine Flask app
├── main.py               # Cloud Functions entry point
├── cloud_function.py     # Additional Cloud Functions
├── models.py             # User and Task data models
├── handlers.py           # API request handlers
├── worker.py             # Background task worker
├── config.py             # Configuration management
├── validator.py          # Input validation utilities
├── utils.py              # Helper functions
├── storage_service.py    # Google Cloud Storage wrapper
├── logger.py             # Logging utilities
├── app.yaml              # App Engine configuration
├── function_config.yaml  # Cloud Function configuration
└── deploy.sh             # Deployment script
```

## API Endpoints

### Service Info
- `GET /` - Service information and status
- `GET /health` - Health check endpoint

### Data Management
- `GET /api/data` - Get all data items
- `POST /api/data` - Create new data item
- `GET /api/data/<task_id>` - Get specific data item
- `DELETE /api/data/<task_id>` - Delete data item

### User Management
- `POST /api/users` - Create new user
- `GET /api/users` - Get all users
- `GET /api/users/<user_id>` - Get specific user

### Task Management
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/<task_id>` - Get specific task
- `PUT /api/tasks/<task_id>` - Update task status
- `DELETE /api/tasks/<task_id>` - Delete task

### Worker
- `GET /api/worker/status` - Get worker queue status
- `POST /api/worker/process` - Process next task in queue

### Configuration
- `GET /api/config` - Get application configuration
- `GET /api/stats` - Get system statistics

## Setup

### Prerequisites

- Python 3.9+
- Google Cloud SDK installed
- GCP project with billing enabled

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Amitommiter/TaskFlow.git
cd TaskFlow
```

2. Install dependencies:
```bash
pip install Flask==2.3.3 gunicorn==21.2.0 google-cloud-storage==2.10.0 google-cloud-logging==3.8.0
```

3. Set up Google Cloud:
```bash
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

### Environment Variables

Set the following environment variables:

```bash
export GCP_PROJECT_ID=your-project-id
export GCP_REGION=us-central1
export ENVIRONMENT=production
export BUCKET_NAME=your-bucket-name
export LOG_LEVEL=INFO
```

## Deployment

### App Engine Deployment

1. Update `app.yaml` with your project settings

2. Deploy using the script:
```bash
chmod +x deploy.sh
./deploy.sh YOUR_PROJECT_ID
```

Or deploy manually:
```bash
gcloud app deploy app.yaml
```

### Cloud Functions Deployment

1. Deploy individual functions:
```bash
gcloud functions deploy hello_world \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated \
  --source .
```

## Usage Examples

### Create a Task
```bash
curl -X POST http://your-app-url/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete project", "description": "Finish the GCP project"}'
```

### Create a User
```bash
curl -X POST http://your-app-url/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Get All Tasks
```bash
curl http://your-app-url/api/tasks
```

### Update Task Status
```bash
curl -X PUT http://your-app-url/api/tasks/<task_id> \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

## Cloud Functions

### hello_world
Simple greeting function that accepts a name parameter.

**Trigger:** HTTP
**Parameters:** `name` (optional)

### process_data
Processes numeric arrays and returns sum and count.

**Trigger:** HTTP POST
**Request Body:**
```json
{
  "data": [1, 2, 3, 4, 5]
}
```

## Configuration

The application uses environment-based configuration managed through `config.py`:

- `GCP_PROJECT_ID` - Your GCP project ID
- `GCP_REGION` - Deployment region
- `ENVIRONMENT` - Environment (development/production)
- `BUCKET_NAME` - Cloud Storage bucket name
- `LOG_LEVEL` - Logging level (DEBUG/INFO/WARNING/ERROR)

## Features in Detail

### Task Management
- Create, read, update, and delete tasks
- Status tracking (pending, in_progress, completed)
- Automatic timestamp generation
- Unique task IDs

### User Management
- User creation with email validation
- Unique user IDs
- Timestamp tracking

### Background Worker
- Queue-based task processing
- Status monitoring
- Task state management

### Storage Integration
- File upload/download
- List bucket contents
- File existence checking
- Delete operations

## License

This project is open source and available for use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

