#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('myuser', 'mypass')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='amq.direct', exchange_type='direct', durable='true')

channel.basic_publish(exchange='amq.direct',
                      routing_key=sys.argv[1],
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
