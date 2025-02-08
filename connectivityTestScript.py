########## A SIMPLE TCP/IP SOCKET SCRIPT FOR TESTING CONNECTION WITH THE KAFKA RAFT SERVER ######################
##########       REMINDER: THE KAFDROP PORT IS DIFFERENT THAN THE KAFKA PORT (9092)        ######################
##########        YOU CAN ALSO FIND YOUR KAFDROP UI APPLICATION ON localhost:9000          ######################

import socket

def test_kafka_connection(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(f"Connected to Kafka at {host}:{port}")
    except Exception as e:
        print(f"Failed to connect to Kafka: {e}")

# Test Kafka connection
test_kafka_connection("localhost", 9092)
