#!/usr/bin/env python

from yaml import load, dump
import yaml

class AmazonDash:

    configurationFile = 'app/config.yml'

    # Constructor
    def __init__(self, configurationFile=None):
        if configurationFile is not None:
            self.configurationFile = configurationFile
        # Load configuration
        self.data=self.getConfiguration()
        self.settings=self.data['settings']
        self.buttons=self.data['buttons']

    # Set listener and send MQQT
    def setListener(self):
        # Loop throug all MQTT groups
        for groupKey, group in self.buttons.items():
            print(groupKey)
            # Loop through all MQTT buttons
            for buttons in group:
                for buttonKey, button in buttons.items():
                    print(
                        'Button: ', button, 
                        'ButtonKey: ', buttonKey, 
                        'Data id: ', buttons[buttonKey]['id'], 
                        'Data title: ', buttons[buttonKey]['title'])

    # Get the configuration from a given YAML file
    def getConfiguration(self):
        with open(self.configurationFile, 'r') as stream:
            try:
                data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return data

# Example calls
ad = AmazonDash()
print(ad.moo())