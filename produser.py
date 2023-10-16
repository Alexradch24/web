import pika
from dickpic_pb2 import Length
import random as rm


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='info')

for j in range(20):
    message = Length(i = rm.randint(10,30))

    message = message.SerializeToString()

    channel.basic_publish(exchange='', routing_key="info", body=message)

connection.close()