import base64
import json
import pymysql
from datetime import datetime

def process_pubsub(event, context):
    data = base64.b64decode(event["data"]).decode("utf-8")
    record = json.loads(data)

    conn = pymysql.connect(
        host="136.113.141.38",
        user="root",
        password="Admin123@",
        database="hybriddb"
    )

    cursor = conn.cursor()

    ts = datetime.utcnow().isoformat()

    sql = """
    INSERT INTO records (id, name, course, processed_timestamp)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (
        record["id"],
        record["name"],
        record["course"],
        ts
    ))

    conn.commit()
    conn.close()

    print("Inserted into Cloud SQL")