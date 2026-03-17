import os

DB_HOST = os.getenv("DB_HOST", "hospitaldb.cgv8yukoeqoa.us-east-1.rds.amazonaws.com")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin1234")
DB_NAME = os.getenv("DB_NAME", "hospital")
