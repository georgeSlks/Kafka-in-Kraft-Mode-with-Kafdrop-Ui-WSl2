# Kafka in KRaft mode Server with Kafdrop UI using Docker (WSL Compatible)

## Overview
This repository provides a easy-to-use **Kafka Raft** server (instead of zookeeper) setup running inside a **Docker container** on Windows **(WSL)**. Also, includes **Kafdrop**, a web UI for managing Kafka topics, messages, and brokers.
Finally, you can view a **connectivityTestScript.py** file which you can use for testing the connectivity with your Kafka server.

### Why?
For a quick functional solution setup for everyone needs a quick, functional environment on Windows.
This configuration removes the windows setup complexity by using **Docker Compose** inside linux enviroment.

## Technical Details
- **Kafka Raft Mode**
- **Docker & WSL:** Runs seamlessly on Windows through WSL 2 and Docker.
- **Kafdrop UI:** Provides a web interface for visualizing Kafka topics and messages.
- **Persistence:** Kafka logs are stored in a volume (`kafka-data`) to ensure data is retained across restarts.

## Configuration Breakdown
Below is a detailed explanation of each configuration setting in the `docker-compose.yml` file:

| Configuration Line | Explanation |
|-----------------|-----------------------|
| `image: apache/kafka:latest` | Uses the latest Apache Kafka Docker image. |
| `KAFKA_NODE_ID=1` | Assigns a unique ID to this Kafka node. |
| `KAFKA_PROCESS_ROLES=controller,broker` | Enables Kafka Raft mode by combining the broker and controller roles (no Zookeeper needed). |
| `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT` | Defines different listener security protocols. |
| `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092` | Specifies how clients and internal processes connect to Kafka. |
| `KAFKA_LISTENERS=PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092,CONTROLLER://localhost:9093` | Configures Kafka listeners for external clients and internal processes. |
| `KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT` | Defines how brokers communicate internally. |
| `KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER` | Specifies which listener is used for controller communication. |
| `KAFKA_LOG_DIRS=/var/lib/kafka/data` | Defines the directory where Kafka logs are stored. |
| `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1` | Sets the replication factor for Kafka offset topics (1 since there is only one broker). |
| `KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1` | Defines the minimum number of in-sync replicas for transaction logs. |
| `KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1` | Sets replication factor for transaction logs (1 for a single-node setup). |
| `KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:9093` | Specifies controller election settings for Kafka Raft. |
| `KAFKA_AUTO_CREATE_TOPICS_ENABLE=true` | Allows Kafka to automatically create topics when needed. |
| `KAFKA_CONFLUENT_SUPPORT_METRICS_ENABLE=false` | Disables Confluent telemetry collection. |
| `ports: "9092:9092"` | Exposes Kafka’s port to the host system. |
| `volumes: kafka-data:/var/lib/kafka/data` | Ensures data persistence between container restarts. |
| `image: obsidiandynamics/kafdrop` | Uses Kafdrop as the web UI for Kafka. |
| `KAFKA_BROKERCONNECT=kafka:29092` | Connects Kafdrop to the Kafka broker inside Docker. |
| `ports: "9000:9000"` | Exposes Kafdrop’s web UI on port 9000. |

## How to Use
1. **Ensure Docker & WSL 2 are installed on your system (you can use Docker Desktop too).**
1. **Create a directory in your linux enviroment with your project(optional)** 
1. **Move the docker-compose.yml file to your directory or create a new one and copy-paste my configuration**
2. **Run the following command in your linux terminal:**
   ```sh
   docker-compose up -d
   ```
3. **Test connectivity with the server:** Using my connectivityTestScript.py script on localhost port 9092.
4. **Access Kafka through Kafdrop UI:** Open your browser and go to [http://localhost:9000](http://localhost:9000).
4. **Start Producing & Consuming Messages ;)**

## Troubleshooting
- **Issue: "Kafka connection refused on port 9092"**  
  ✅ Make sure Docker is running and that no other process is using port 9092.



