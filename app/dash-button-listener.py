#!/usr/bin/env python

# https://www.raspberrypi.org/magpi/hack-amazon-dash-button-raspberry-pi/
# pip3 install scapy adafruit-io pyyaml
# pip3 install -U python-dotenv
# sudo python3 app/listen.py

from Adafruit_IO import MQTTClient
from dotenv import load_dotenv
from scapy.all import *
from yaml import load, dump

load_dotenv()
import os


# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = os.getenv('MQTT_USERNAME')

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = os.getenv('MQTT_TOKEN')

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for dash/# changes...')
    client.subscribe('dash/#')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()

def arp_detect(pkt):
	if pkt[ARP].hwsrc == "6c:56:97:da:b8:41":
		client.publish('dash.blugento', 1)
		return "Blugento button detected!"


print(sniff(prn=arp_detect, filter="arp", store=0))
