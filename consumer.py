import pika, json, os
from queue import Queue

message_queue = Queue(maxsize=100)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"📩 Received: {data}")
    if message_queue.full():
        message_queue.get()
    message_queue.put(data)

def start_consumer():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST", "localhost"),
        virtual_host=os.getenv("RABBITMQ_VHOST", "/"),
        credentials=pika.PlainCredentials(
            os.getenv("RABBITMQ_USER", "guest"),
            os.getenv("RABBITMQ_PASS", "guest")
        )
    )
)

    channel = connection.channel()
    channel.queue_declare(queue='order_events')
    channel.basic_consume(queue='order_events', on_message_callback=callback, auto_ack=True)
    print("📡 Analytics consumer waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
