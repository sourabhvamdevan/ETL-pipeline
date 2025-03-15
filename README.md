

---

# Real-Time Data Streaming Pipeline with Kafka and PostgreSQL

## Overview
This project demonstrates a **real-time data streaming pipeline** using **Apache Kafka** for message streaming and **PostgreSQL** for data storage. It includes:
- A **Kafka producer** to generate and publish real-time messages.
- A **Kafka consumer** to ingest messages into a PostgreSQL database.
- An **ETL (Extract, Transform, Load)** process to transform and analyze the stored data.

The pipeline showcases seamless integration of **distributed systems**, **event-driven architecture**, and **data engineering** workflows.

---

## Tools and Technologies Used
- **Apache Kafka**: Distributed event streaming platform for real-time data processing.
- **PostgreSQL**: Relational database for persistent data storage.
- **Python**: Programming language for implementing the pipeline.
- **Confluent Kafka Python Client**: Library for interacting with Kafka.
- **Psycopg2**: PostgreSQL adapter for Python.
- **SQLAlchemy**: Database toolkit and ORM for Python.
- **Pandas**: Data manipulation library for ETL transformations.

---

## Features
1. **Kafka Producer**:
   - Generates and publishes real-time messages to a Kafka topic.
   - Simulates live data with timestamps.

2. **Kafka Consumer**:
   - Subscribes to the Kafka topic and consumes messages.
   - Stores messages in a PostgreSQL database.

3. **ETL Process**:
   - Extracts data from PostgreSQL into a Pandas DataFrame.
   - Performs transformations (e.g., filtering, adding derived columns).
   - Outputs the transformed data for analysis.

---

## Prerequisites
Before running the project, ensure the following are installed:
- **Python 3.x**
- **Apache Kafka** (with Zookeeper and Kafka broker running).
- **PostgreSQL** (installed and running locally).
- Required Python libraries:
  ```bash
  pip install pandas sqlalchemy psycopg2 confluent-kafka
  ```

---

## Setup and Execution

### 1. Start Kafka Services
- Run Zookeeper:
  ```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties
  ```
- Start Kafka broker:
  ```bash
  bin/kafka-server-start.sh config/server.properties
  ```

### 2. Run Kafka Producer
- Generates and sends messages to the Kafka topic:
  ```bash
  python kafka_producer.py
  ```

### 3. Run Kafka Consumer
- Consumes messages from the Kafka topic and stores them in PostgreSQL:
  ```bash
  python kafka_consumer.py
  ```

### 4. Run ETL Process
- Extracts and transforms data from PostgreSQL:
  ```bash
  python etl_process.py
  ```

---

## Example Output

### Kafka Producer Output
```plaintext
Sent: {'message': 'Test message to check if consumer is running', 'timestamp': '2024-12-18 10:00:00'}
Sent: {'message': 'Live message 1', 'timestamp': '2024-12-18 10:00:01'}
```

### Kafka Consumer Output
```plaintext
Waiting for messages...
Received message: {'message': 'Live message 1', 'timestamp': '2024-12-18 10:00:01'}
Inserted into database: (1, '2024-12-18 10:00:01', 'Live message 1')
```

### ETL Process Output
```plaintext
               timestamp  id           new_column
0  2024-12-18 10:00:01   1  Transformed Data

Data Schema:
timestamp    datetime64[ns]
id                   int64
new_column         object
dtype: object
```

---

## Project Structure
```
real-time-pipeline/
├── kafka_producer.py       # Kafka producer script
├── kafka_consumer.py       # Kafka consumer script
├── etl_process.py          # ETL transformation script
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## Future Enhancements
- Add support for **scaling Kafka consumers** for high-throughput data.
- Integrate **advanced analytics** (e.g., machine learning models) into the ETL process.
- Use **Docker** to containerize the pipeline for easy deployment.
- Implement **error handling** and **retry mechanisms** for robust data processing.

---

## Resources
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Confluent Kafka Python Client](https://github.com/confluentinc/confluent-kafka-python)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


