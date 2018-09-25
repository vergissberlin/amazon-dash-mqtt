# Amazon Dash Button MQTT

Send a MQTT message when someone click on your configured dash buttons in the network.

## Installation

**1. Grab the code**
```bash
git clone git@github.com:vergissberlin/amazon-dash-mqtt.git
cd amazon-dash-mqtt
cp app/config.dist.yml app/config.yml
vim app/config.yml
```

**2. Configure**
Enter 
- your MQTT credentials in the *app/config.yml*.
- The buttons an the feed where to publish the MQTT message in the *app/config.yml*.

```yml
settings:
  MQTT_BROKER: io.adafruit.com
  MQTT_USERNAME: YOUR_USERNAME
  MQTT_TOKEN: YOUR_TOKEN
  NETWORK_INTERFACE: en1    

mqtt: 
    group-1:
        - 00:00:00:00:00:00:
            id: "dash-example"
            payload: "Hello example"
        - 00:00:00:00:00:00:
            id: "dash-example"
            payload: "Hello example"
    group-2:
        - 00:00:00:00:00:00:
            id: "dash-example"
            payload: "Hello example"

```


**3. Start the application**
```bash
sudo phyton3 app/main.py
```
