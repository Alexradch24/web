import pika
import dickpic_pb2 

def callback(ch, method, properties, body):
    received_message = dickpic_pb2.Length()
    received_message.ParseFromString(body)
    print(f"Lenght - {received_message.i}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='info')

channel.basic_consume('info', callback, auto_ack=True)

print('Для выхода нажмите Ctrl+C')
channel.start_consuming()