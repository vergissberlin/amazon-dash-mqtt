#!/usr/bin/python

from Adafruit_IO import MQTTClient
import sys

class MQTTAdafruit:

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
