#!/usr/bin/env python

from scapy.all import sniff
import logging

# Create logger
log = logging.getLogger('amazon-dash-mqtt.amazondash')

class AmazonDash:

    # Constructor
    def __init__(self, buttons=None, mqtt=None):
        if buttons is None:
            log.error('Please setup buttons in the config.yml!')
            raise ValueError('Please setup buttons in the config.yml!')
        if mqtt is None:
            raise ValueError('Please setup mqtt client!')

    @staticmethod
    def arp_detect(pkt):
        if pkt['ARP'].hwsrc == "6c:56:97:da:b8:41":
            # client.publish('dash.blugento', 1)
            log.info('Button is detected')
            return "Blugento button detected!"


    # Set listener and send MQQT
    def setListener(self, buttons):
        # Loop throug all MQTT groups
        for groupKey, group in buttons.items():
            print(groupKey)
            # Loop through all MQTT buttons
            for buttons in group:
                for buttonKey, button in buttons.items():
                    print(
                        'Button: ', button, 
                        'ButtonKey: ', buttonKey, 
                        'Data id: ', buttons[buttonKey]['id'], 
                        'Data title: ', buttons[buttonKey]['title'])

   