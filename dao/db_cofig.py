import sqlite3
import psycopg2

# path / url de conexão

DB_PATH = "postgresql://neondb_owner:npg_lRJMfSvI96QW@ep-solitary-lake-b81m7mfu-pooler.c-14.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
     conn = psycopg2.connect(DB_PATH)
     return conn