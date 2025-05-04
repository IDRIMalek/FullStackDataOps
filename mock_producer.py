from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    message = {
        "site_id": random.randint(1000, 1005),
        "power": round(random.uniform(100.0, 500.0), 2),
        "timestamp": time.time()
    }
    producer.send("mock_photovoltaic", message)
    print("Sent:", message)
    time.sleep(2)