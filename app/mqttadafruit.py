#!/usr/bin/python

from Adafruit_IO import MQTTClient
import sys
import logging

# Create logger
log = logging.getLogger('amazon-dash-mqtt.amazondash')


class MQTTAdafruit:
    
    # Constructor
    def __init__(self, settings=None):
        if settings is None:
            log.critical('Please setup buttons in the config.yml!')
            raise ValueError('Please setup the MQTT settings in the config.yml!')
        else:
            print(settings['MQTT_BROKER'])

            # Create an MQTT client instance.
            self.__client = MQTTClient(settings['MQTT_USERNAME'], settings['MQTT_TOKEN'])

            # Setup the callback functions defined above.
            self.__client.on_connect    = MQTTAdafruit.connected
            self.__client.on_disconnect = MQTTAdafruit.disconnected
            self.__client.on_message    = MQTTAdafruit.message

            # Connect to the Adafruit IO server.
            self.__client.connect()

            # Now the program needs to use a client loop function to ensure messages are
            # sent and received. There are a few options for driving the message loop,
            # depending on what your program needs to do.

            # The first option is to run a thread in the background so you can continue
            # doing things in your program.
            self.__client.loop_background()

            
    def getClient(self):
        return self.__client

    # Define callback functions which will be called when certain events happen.
    @staticmethod
    def connected(client):
        # Connected function will be called when the client is connected to Adafruit IO.
        # This is a good place to subscribe to feed changes.  The client parameter
        # passed to this function is the Adafruit IO MQTT client so you can make
        # calls against it easily.
        print('Connected to Adafruit IO!  Listening for dash/# changes...')
        client.subscribe('dash/#')

    @staticmethod
    def disconnected(client):
        # Disconnected function will be called when the client disconnects.
        print('Disconnected from Adafruit IO!')
        sys.exit(1)

    @staticmethod
    def message(client, feed_id, payload):
        # Message function will be called when a subscribed feed has a new value.
        # The feed_id parameter identifies the feed, and the payload parameter has
        # the new value.
        print('Feed {0} received new value: {1}'.format(feed_id, payload))
