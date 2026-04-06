import time
import os
import pymysql
from app import create_app

def wait_for_db():
    while True:
        try:
            conn = pymysql.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE"),
                connect_timeout=5
            )
            conn.close()
            print("MySQL is ready!")
            break
        except Exception as e:
            print(f"Waiting for MySQL... ({e})")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()
    app = create_app()
    print("Starting Flask...")
    app.run(host="0.0.0.0", port=5000)
