import json
import time
from datetime import datetime
from confluent_kafka import Producer

def create_producer():
    return Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def send_messages(producer, topic):
    test_message = {'message': 'Test message to check if consumer is running', 'timestamp': str(datetime.now())}
    producer.produce(topic, value=json.dumps(test_message), callback=delivery_report)
    producer.flush()
    print(f'Sent: {test_message}')

    for i in range(1, 11):
        live_message = {'message': f'Live message {i}', 'timestamp': str(datetime.now())}
        producer.produce(topic, value=json.dumps(live_message), callback=delivery_report)
        print(f'Sent: {live_message}')
        time.sleep(1)

if __name__ == "__main__":
    topic = 'test-topic'
    producer = create_producer()
    send_messages(producer, topic)
