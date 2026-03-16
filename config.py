import os

DB_HOST = os.getenv("DB_HOST", "your-rds-endpoint")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "hospital")