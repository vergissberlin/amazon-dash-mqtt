const dash_button = require('node-dash-button')
const mqtt = require('mqtt')
let configuration = {}
let client

/**
 * Read the configuration
 */
try {
	configuration = require('./config.json')
} catch (error) {
	throw new Error('Please create and fill your credential file "config.json"!')
}
if (configuration.settings.token === '') {
	client = mqtt.connect(configuration.settings.broker)
} else {
	client = mqtt.connect(
		configuration.settings.broker, 
		{
			username: configuration.settings.username,
			password: configuration.settings.token
		}
	)
}

/**
 * Connect to MQTT
 */
client.on('connect', function () {
	console.log("MQTT     | Connected!");
	configuration.devices.forEach(i => {
		let dash = dash_button(i.mac, null, null, 'all')
		dash.on('detected', function () {
			console.log('listener | Dash button "' + i.message + '" detected!')
			client.publish(i.feed, i.message)
		})
	})
})
