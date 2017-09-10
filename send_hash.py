#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('myuser', 'mypass')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='test.fanout', exchange_type='fanout' )

channel.basic_publish(exchange='test.fanout',
                      routing_key=sys.argv[1],
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
