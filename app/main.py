#!/usr/bin/python

# https://www.raspberrypi.org/magpi/hack-amazon-dash-button-raspberry-pi/
# pip3 install scapy adafruit-io pyyaml
# pip3 install -U python-dotenv
# sudo python3 app/listen.py

from amazondash import AmazonDash
from configurationyaml import ConfigurationYaml
from mqttadafruit import MQTTAdafruit

# 1. Configuration
cy = ConfigurationYaml()
settings = cy.getSettings()
buttons = cy.getButtons()
# print('Settings: ', settings)
# print('Buttons: ', buttons)


# 2. MQTT sender
mq = MQTTAdafruit(settings)
mqttClient = mq.getClient()

# 3. AmazonDash listner
ad = AmazonDash(buttons, mqttClient)


# print(sniff(prn=arp_detect, filter="arp", store=0))
