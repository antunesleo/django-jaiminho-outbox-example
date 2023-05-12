import json

from kafka import KafkaConsumer

from outboxexample import settings

print("starting consumer", settings.KAFKA_HOST)

NOTES_TOPIC = "notes"

consumer = KafkaConsumer(
    NOTES_TOPIC,
    bootstrap_servers=[settings.KAFKA_HOST],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)

for message in consumer:
    print(message.value)
