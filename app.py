from flask import Flask, request, jsonify, render_template
from confluent_kafka import Producer
import json
import datetime
from collections import defaultdict

app = Flask(__name__)

producer = Producer({'bootstrap.servers': 'localhost:9092'})

data_storage = {"key": "initial_value"}

# In-memory storage for API usage stats
api_usage = defaultdict(list)

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "GET request received", "current_data": data_storage}
    event = {
        'endpoint': 'GET',
        'action': 'fetch',
        'previous_data': data_storage,
        'new_data': data_storage,
        'timestamp': get_timestamp()
    }
    producer.produce('api-usage', key='GET', value=json.dumps(event), callback=acked)
    producer.flush()
    api_usage[('GET', 'fetch')].append(event)
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    received_data = request.json
    previous_data = data_storage.copy()
    data_storage.update(received_data)

    event = {
        'endpoint': 'POST',
        'action': 'create',
        'previous_data': previous_data,
        'new_data': received_data,
        'timestamp': get_timestamp()
    }
    producer.produce('api-usage', key='POST', value=json.dumps(event), callback=acked)
    producer.flush()
    api_usage[('POST', 'create')].append(event)
    return jsonify({"message": "POST request received", "new_data": received_data, "previous_data": previous_data})

@app.route('/api/data', methods=['PUT'])
def put_data():
    received_data = request.json
    previous_data = data_storage.copy()
    data_storage.update(received_data)

    event = {
        'endpoint': 'PUT',
        'action': 'update',
        'previous_data': previous_data,
        'new_data': received_data,
        'timestamp': get_timestamp()
    }
    producer.produce('api-usage', key='PUT', value=json.dumps(event), callback=acked)
    producer.flush()
    api_usage[('PUT', 'update')].append(event)
    return jsonify({"message": "PUT request received", "new_data": received_data, "previous_data": previous_data})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', stats=dict(api_usage))

if __name__ == '__main__':
    app.run(debug=True)
