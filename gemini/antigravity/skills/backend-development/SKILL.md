---
name: backend-development
description: Generic backend development skill for building REST APIs, working with databases, authentication, and server-side logic. Covers patterns, best practices, and common patterns for backend applications.
---

# Backend Development Instructions

This skill provides general guidance for backend development across various projects. Use this when working with server-side applications, APIs, and database integrations.

## General Principles

### API Design
- Use RESTful conventions for resource-based endpoints
- Use proper HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE (delete)
- Return appropriate status codes: 200, 201, 204, 400, 401, 403, 404, 500
- Use versioning in URLs: /api/v1/resource

### Security
- Never expose sensitive data in responses
- Validate and sanitize all inputs
- Use parameterized queries to prevent SQL injection
- Implement proper authentication and authorization
- Use HTTPS in production

### Error Handling
- Return meaningful error messages
- Log errors appropriately
- Handle exceptions gracefully
- Use consistent error response format

## RESTful API Patterns

### Endpoint Structure
```
GET    /api/v1/users          # List users
GET    /api/v1/users/:id      # Get single user
POST   /api/v1/users          # Create user
PUT    /api/v1/users/:id      # Update user
DELETE /api/v1/users/:id      # Delete user
```

### Response Format
```json
// Success response
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John"
  }
}

// Error response
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format"
  }
}

// List response with pagination
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100
  }
}
```

## Database Patterns

### SQLite (Simple Projects)
```python
import sqlite3

def get_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

def query_users(limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ?", (limit,))
    return cursor.fetchall()
```

### PostgreSQL (Production)
```python
import psycopg2
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="user",
        password="password"
    )
    try:
        yield conn
    finally:
        conn.close()
```

### ORM Patterns (SQLAlchemy)
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)

def create_user(name, email):
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    return user
```

## Authentication

### JWT Token
```python
import jwt
import datetime

SECRET_KEY = "your-secret-key"

def create_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
```

### Password Hashing
```python
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
```

## FastAPI Patterns

### Basic Endpoint
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1

@app.post("/api/items")
def create_item(item: Item):
    # Process item
    return {"id": 1, **item.dict()}

@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

### Dependency Injection
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def list_users(db = Depends(get_db)):
    return db.query(User).all()
```

### Middleware
```python
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Flask Patterns

### Basic App
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.create(**data)
    return jsonify(user), 201
```

### Error Handling
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
```

## Common Tasks

### File Upload
```python
from fastapi import UploadFile, File

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
```

### Background Tasks
```python
from fastapi import BackgroundTasks

def process_data(data):
    # Long-running task
    pass

@app.post("/process")
async def process(background_tasks: BackgroundTasks, data: dict):
    background_tasks.add_task(process_data, data)
    return {"status": "processing"}
```

### Pagination
```python
@app.get("/items")
def get_items(page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    items = db.query(Item).offset(offset).limit(limit).all()
    total = db.query(Item).count()
    return {
        "data": items,
        "page": page,
        "limit": limit,
        "total": total
    }
```

## Testing

### Unit Tests
```python
def test_create_user():
    user = create_user("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
```

### API Tests
```python
def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert "data" in response.json()
```

## Deployment

### Environment Variables
```bash
# .env file
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=your-secret-key
DEBUG=false
```

### Production Server
```bash
# Using gunicorn with uvicorn workers
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# Using uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

## Performance Tips

- Use connection pooling for databases
- Implement caching (Redis, in-memory)
- Optimize queries (indexes, select specific columns)
- Use async/await for I/O operations
- Profile code to find bottlenecks
