import sqlite3
import psycopg2

# path / url de conexão

DB_PATH = "postgresql://neondb_owner:npg_Larl9MGKF2Rd@ep-old-band-bccp15fe-pooler.c-16.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
     conn = psycopg2.connect(DB_PATH)
     return conn