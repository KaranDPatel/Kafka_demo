🚀 Real-Time API Hit Count Tracking with Kafka, Flask, and Python 🚀

This project demonstrates a high-level implementation of real-time API hit count tracking using Kafka, integrated with a Flask-based Python application. The system captures API interactions (GET, POST, PUT requests) in real-time, processes them via Kafka, and displays the results on a live dashboard.


📋 Project Overview

Key Components:


Flask API: Handles API requests and updates the in-memory data store.

Kafka Producer: Sends API hit data to the Kafka Broker.

Kafka Broker: Stores the API hit data in a dedicated topic (api-usage).

Kafka Consumer: Retrieves and processes the data from the Kafka Broker.

Dashboard: Visualizes the API hit counts, showing real-time updates.

**Key Features:**

Real-Time Tracking: Monitors API hit counts as they happen.

Python Integration: Compatible with Flask, Django, and FastAPI frameworks.

Scalability: Easily adaptable to different use cases and scalable based on requirements.

Flexible Setup: The system can be customized to fit specific project needs.


🔧 Setup and Installation
**Prerequisites:**
-Python 3.7+

-Apache Kafka

-Virtual environment (optional but recommended)

**Installation Steps:**

Clone the Repository:

git clone https://github.com/your-username/repo-name.git


Set Up the Virtual Environment:

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Dependencies:


pip install -r requirements.txt

Start Kafka and Zookeeper:

Start Zookeeper:

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

Start Kafka:

.\bin\windows\kafka-server-start.bat .\config\server.properties

Create the Kafka Topic:

.\bin\windows\kafka-topics.bat --create --topic api-usage --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Run the Flask Application:

python app.py

Start the Kafka Consumer:

python consumer.py

Access the Dashboard:

Visit http://localhost:5000/dashboard to view the real-time API hit counts.

🛠 How It Works

User Request: A user sends a GET, POST, or PUT request to the Flask API.

API Processing: The Flask API processes the request, updating the data and producing a message to Kafka.

Kafka Broker: The message is sent to the Kafka Broker, which stores it in the api-usage topic.

Kafka Consumer: A Kafka Consumer retrieves the data from the topic and updates the in-memory statistics.

Dashboard Visualization: The dashboard displays the real-time API hit counts based on the consumer’s data.

