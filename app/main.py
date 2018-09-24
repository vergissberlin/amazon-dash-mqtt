#!/usr/bin/python

# https://www.raspberrypi.org/magpi/hack-amazon-dash-button-raspberry-pi/
# pip3 install scapy adafruit-io pyyaml
# pip3 install -U python-dotenv
# sudo python3 app/listen.py

from amazondash import AmazonDash
from mqttadafruit import MQTTAdafruit
from scapy.all import sniff

# Create an MQTT client instance.
# client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
# client.on_connect    = MQTTAdafruit.connected
# client.on_disconnect = MQTTAdafruit.disconnected
# client.on_message    = MQTTAdafruit.message

# Connect to the Adafruit IO server.
# client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
# client.loop_background()

def arp_detect(pkt):
    if pkt['ARP'].hwsrc == "6c:56:97:da:b8:41":
        # client.publish('dash.blugento', 1)
        return "Blugento button detected!"


print(sniff(prn=arp_detect, filter="arp", store=0))
