# FastAPI Hello World Application

A simple Hello World API built with FastAPI.

## Features

- Root endpoint that returns a Hello World message
- Dynamic greeting endpoint that takes a name parameter
- Automatic API documentation with Swagger UI

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Setup Instructions

Follow these steps to set up and run the FastAPI application:

### 1. Clone the repository

```bash
git clone https://github.com/xxradar/mcp-test-repo.git
cd mcp-test-repo
```

### 2. Create a virtual environment (optional but recommended)

```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The application will start and be available at http://127.0.0.1:8000

Alternatively, you can run the application directly with Python:

```bash
python main.py
```

## API Endpoints

- `GET /`: Returns a simple Hello World message
- `GET /hello/{name}`: Returns a personalized greeting with the provided name
- `GET /docs`: Swagger UI documentation
- `GET /redoc`: ReDoc documentation

## Example Usage

### Using curl

```bash
# Get Hello World message
curl http://127.0.0.1:8000/

# Get personalized greeting
curl http://127.0.0.1:8000/hello/John
```

### Using a web browser

- Open http://127.0.0.1:8000/ in your browser for the Hello World message
- Open http://127.0.0.1:8000/hello/John in your browser for a personalized greeting
- Open http://127.0.0.1:8000/docs for the Swagger UI documentation

## Development

To make changes to the application, edit the `main.py` file. The server will automatically reload if you run it with the `--reload` flag.
