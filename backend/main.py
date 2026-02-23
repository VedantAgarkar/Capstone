import subprocess
import sys
import logging
import os
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, EmailStr
from backend.database import get_db_connection, init_db
import sqlite3
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Lazy load routes to avoid loading incompatible models at startup
# from backend.routes import heart 
# from backend.routes import bot 
# from backend.routes import parkinsons 
# from backend.routes import diabetes 

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    fullname: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@app.post("/api/register")
async def register(user: UserRegister):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Normalize email to lowercase
        email_normalized = user.email.strip().lower()
        
        cursor.execute(
            "INSERT INTO users (email, password, fullname) VALUES (?, ?, ?)",
            (email_normalized, user.password, user.fullname)
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already registered")
    finally:
        conn.close()

@app.post("/api/login")
async def login(user: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Parameterized query to prevent SQL injection
    # Normalize email
    email_normalized = user.email.strip().lower()
    
    cursor.execute(
        "SELECT * FROM users WHERE LOWER(email) = ? AND password = ?",
        (email_normalized, user.password)
    )
    db_user = cursor.fetchone()
    conn.close()
    
    if db_user:
        return {
            "message": "Login successful",
            "user": {
                "email": db_user["email"],
                "fullname": db_user["fullname"],
                "is_admin": bool(db_user["is_admin"])
            }
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")

@app.get("/api/admin/stats")
async def get_admin_stats(email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if user is admin
    cursor.execute("SELECT is_admin FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if not user or not user["is_admin"]:
        conn.close()
        raise HTTPException(status_code=403, detail="Access denied")
    
    # Get total user count
    cursor.execute("SELECT COUNT(*) as count FROM users")
    user_count = cursor.fetchone()["count"]
    
    # Get recent predictions
    cursor.execute("""
        SELECT p.*, IFNULL(u.fullname, 'Guest User') as fullname 
        FROM predictions p 
        LEFT JOIN users u ON p.user_id = u.id 
        ORDER BY timestamp DESC LIMIT 10
    """)
    recent_predictions = [dict(row) for row in cursor.fetchall()]
    
    # Get prediction breakdown
    cursor.execute("SELECT type, COUNT(*) as count FROM predictions GROUP BY type")
    breakdown = {row["type"]: row["count"] for row in cursor.fetchall()}
    
    conn.close()
    
    return {
        "total_users": user_count,
        "recent_predictions": recent_predictions,
        "prediction_breakdown": breakdown
    }

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Store process handles for cleanup
_streamlit_processes = []


@app.on_event("startup")
def startup_event():
    """Initialize database and start Streamlit apps."""
    init_db()
    launch_streamlit_apps()

def launch_streamlit_apps():
    """Start multiple Streamlit apps at different ports with error handling."""
    apps_to_launch = [
        ("backend/routes/heart.py", 8501),
        ("backend/routes/diabetes.py", 8502),
        ("backend/routes/parkinsons.py", 8503),
        ("backend/routes/bot.py", 8504)
    ]
    for app_path, port in apps_to_launch:
        try:
            logger.info(f"Starting Streamlit app: {app_path} on port {port}")
            process = subprocess.Popen([
                sys.executable, "-m", "streamlit", "run", app_path,
                "--server.port", str(port),
                "--server.headless", "true"
            ])
            _streamlit_processes.append(process)
        except Exception as e:
            logger.error(f"Failed to start {app_path}: {str(e)}")

@app.on_event("shutdown")
def shutdown_streamlit_apps():
    """Clean up Streamlit processes on shutdown."""
    for process in _streamlit_processes:
        try:
            process.terminate()
            process.wait(timeout=5)
            logger.info("Streamlit process terminated gracefully")
        except subprocess.TimeoutExpired:
            process.kill()
            logger.warning("Streamlit process killed")
        except Exception as e:
            logger.error(f"Error terminating process: {str(e)}")
