# Amazon Dash Button MQTT

[![Build Status](https://travis-ci.org/vergissberlin/amazon-dash-mqtt.svg?branch=master)](https://travis-ci.org/vergissberlin/amazon-dash-mqtt) [![Greenkeeper badge](https://badges.greenkeeper.io/vergissberlin/amazon-dash-mqtt.svg)](https://greenkeeper.io/)

> Send a MQTT message when someone presses your configured dash buttons.

## Installation

### Dependencies

- libpcap
```bash
sudo apt install libpcap
```
- NodeJS (>= 8.0.0)

### 1. Get the code

```bash
git clone https://github.com/vergissberlin/amazon-dash-mqtt.git
cd amazon-dash-mqtt
npm install
```

### 2. Configure

- Copy the dist file ```cp config.dist.json config.json```
- Add your MQTT credentials in the *config.json*.
- Add the buttons, the message and the feed where to publish the MQTT message in the *config.json*.
- If you're using a broker without need for a token just leave it empty

```json
{
    "settings": {
        "broker": "mqtt://<YOUR_BROKER>",
        "username": "<YOUR_USERNAME>",
        "token": "<YOUR_TOKEN>"
    },

    "devices": [
        {
            "mac": "<MAC_ADRESS>",
            "feed": "<FEED>",
            "message": "<MESSAGE>"
        }
    ]
}
```

    NOTE: If you're using Adafruit IO, then use
          "mqtt://io.adafruit.com" as "broker", and in "feed" use "<USERNAME>/feeds/<FEED>".

### 3. Start the application

```bash
sudo nano app.js
```
