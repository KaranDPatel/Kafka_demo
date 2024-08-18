from confluent_kafka import Consumer, KafkaError
import json
from collections import defaultdict  # Add this import

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'dashboard-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['api-usage'])

api_usage = defaultdict(list)

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    event = json.loads(msg.value().decode('utf-8'))
    endpoint = event['endpoint']
    action = event['action']
    timestamp = event['timestamp']
    previous_data = event['previous_data']
    new_data = event['new_data']
    api_usage[(endpoint, action)].append({
        'timestamp': timestamp,
        'previous_data': previous_data,
        'new_data': new_data
    })
    print(f"Updated stats: {dict(api_usage)}")

consumer.close()
