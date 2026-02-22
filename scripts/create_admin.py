import sys
import os
import sqlite3

# Add the project root to sys.path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database import get_db_connection

def create_admin(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if user:
        print(f"User {email} found. Promoting to admin...")
        cursor.execute("UPDATE users SET is_admin = 1 WHERE email = ?", (email,))
    else:
        print(f"User {email} not found. Creating default admin account...")
        # Default password is 'admin123'
        cursor.execute(
            "INSERT INTO users (email, password, fullname, is_admin) VALUES (?, ?, ?, ?)",
            (email, "admin123", "System Admin", 1)
        )
    
    conn.commit()
    conn.close()
    print(f"Admin setup complete for {email}")

if __name__ == "__main__":
    target_email = "admin@test.com"
    create_admin(target_email)
