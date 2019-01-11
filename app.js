const dash_button = require('node-dash-button');
const mqtt = require('mqtt');
const configuration = require('./config.json');

console.log(JSON.stringify(configuration, null, 2));
let client;

if (configuration.settings.token === "") {
    client = mqtt.connect(configuration.settings.broker);
} else {
    client = mqtt.connect(configuration.settings.broker, 
        {
            username: configuration.settings.username,
            password: configuration.settings.token
        });
}



client.on('connect', function () {
    console.log("Connected!");

    configuration.devices.forEach(i => {
        console.log("I: " + i);

        let dash = dash_button(i.mac, null, null, 'all');
        dash.on("detected", function (){
            console.log("Dash button " + i.message + " detected!");
            client.publish(i.feed, i.message);
        });
    });

});
