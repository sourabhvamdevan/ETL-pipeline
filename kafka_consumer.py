import json
import psycopg2
from psycopg2 import sql
from confluent_kafka import Consumer, KafkaException

def create_database():
    conn = psycopg2.connect(dbname='mydatabase', user='postgres', password='khsbuPOSTGRE@1154', host='localhost', port='5432')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, message TEXT NOT NULL, timestamp TIMESTAMP NOT NULL)')
    conn.commit()
    return conn

def insert_message(conn, message):
    cursor = conn.cursor()
    cursor.execute(sql.SQL('INSERT INTO messages (message, timestamp) VALUES (%s, %s)'), (message['message'], message['timestamp']))
    conn.commit()

def create_consumer():
    consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'my-group', 'auto.offset.reset': 'earliest'})
    consumer.subscribe(['test-topic'])
    return consumer

def consume_messages(consumer, conn):
    try:
        print("Waiting for messages...")
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            message_value = json.loads(msg.value().decode('utf-8'))
            print(f'Received message: {message_value}')
            insert_message(conn, message_value)
    except KeyboardInterrupt:
        print("Consumer interrupted, shutting down...")
    finally:
        consumer.close()
        conn.close()

if __name__ == "__main__":
    conn = create_database()
    consumer = create_consumer()
    consume_messages(consumer, conn)
