import pika
import os

class mqConsumer(mqConsumerInterface):


    def __init__(self, consumer_queue, consumer_exchange,routing_key ):
        self.consumer_queue = consumer_queue
        self.consumer_exchange = consumer_queue
        self.routing_key = routing_key

    def setupRMQConnection(self):
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection
        # Establish Channel
        channel = connection.channel()
        # Create Queue if not already present
        
        self.consumer_queue = channel.queue_declare(queue="consumer_queue")

        # Create the exchange if not already present
        self.consumer_exchange = channel.exchange_declare(exchange="consumer_exchange")
        # Bind Binding Key to Queue on the exchange
        channel.queue_bind(
        queue= self.consumer_queue,
        routing_key= self.routing_key,
        exchange= self.consumer_exchange,)
        # Set-up Callback function for receiving messages
        self.channel.basic_consume(
        "consumer_queue", self.setupRMQConnection, auto_ack=False
        )
        
