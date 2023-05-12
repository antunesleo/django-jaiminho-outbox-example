import json
import sys

from jaiminho.send import save_to_outbox
from kafka import KafkaProducer

from outboxexample import settings

import signal

producer = KafkaProducer(bootstrap_servers=[settings.KAFKA_HOST])


def close_producer(signal, frame):
    print("Closing Kafka producer connection...")
    producer.close()
    print("Kafka producer connection closed.")
    sys.exit(0)


signal.signal(signal.SIGTERM, close_producer)


def dispatch_to_kafka(topic, message):
    encoded_message = json.dumps(message).encode("utf-8")
    producer.send(topic, encoded_message)
    producer.flush()
    print(f"{message['name']} event published to Kafka")


NOTES_TOPIC = "notes"


@save_to_outbox
def publish_note_created(note_dict):
    message = {
        "name": "note-created",
        "note": note_dict,
    }
    dispatch_to_kafka(NOTES_TOPIC, message)
