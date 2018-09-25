#!/usr/bin/env python

from yaml import load, dump
import yaml
import logging

# Create logger
log = logging.getLogger('amazon-dash-mqtt.configuration')

class ConfigurationYaml:

    configurationFile = 'app/config.yml'

    # Constructor
    def __init__(self, configurationFile=None):
        if configurationFile is not None:
            self.configurationFile = configurationFile

    # Extract the settings from configuration file
    def getSettings(self):
        return self.__getConfiguration()['settings']

    # Extract the buttons from configuration file
    def getButtons(self):
        return self.__getConfiguration()['buttons']

    # Get the configuration from a given YAML file
    def __getConfiguration(self):
        with open(self.configurationFile, 'r') as stream:
            try:
                data = yaml.load(stream)
            except yaml.YAMLError as exc:
                log.critical(exc)
        return data

