#!/usr/bin/env python
import pika
# Example taken from https://pika.readthedocs.io/en/stable/modules/parameters.html

credentials = pika.PlainCredentials('brandmeisterclient1', 'test1234')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='dapnetdc2.db0sda.ampr.org', credentials=credentials))
channel = connection.channel()

bm_queue = channel.queue_declare(queue='brandmeister_queue')
channel.queue_bind(exchange="thirdparty.brandmeister", queue=bm_queue)
channel.basic_consume(queue=bm_queue, on_message_callback=callback)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
