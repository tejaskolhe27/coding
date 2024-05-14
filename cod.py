import psycopg2
from psycopg2 import OperationalError

def create_database(db_name, db_user, db_password, db_host, db_port):
    try:
        # Connect to the default 'postgres' database first
        conn = psycopg2.connect(
            dbname='postgres',
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Create the new database
        cursor.execute(f"CREATE DATABASE {db_name}")

        print(f"Database '{db_name}' created successfully")

    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Provide your Redshift credentials and configuration
db_name = "your_database_name"
db_user = "your_redshift_user"
db_password = "your_redshift_password"
db_host = "your_redshift_host"
db_port = "your_redshift_port"

# Call the function to create the database
create_database(db_name, db_user, db_password, db_host, db_port)
