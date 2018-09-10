/**
 * Send slack message
 *
 * @category
 * @author   Andre Lademann <vergissberlin@googlemail.com>
 * @license  MIT
 */

const DashButton = require('dash-button')
const request = require('request')
const mqtt = require('mqtt')


require('dotenv').config()

function sendToSlack(s, theUsername, theIconUrl, theIconEmoji, theChannel) {
  let payload = {
    text: s
  }
  if (theUsername !== undefined) {
    payload.username = theUsername
  }
  if (theIconUrl !== undefined) {
    payload.icon_url = theIconUrl
  }
  if (theIconEmoji !== undefined) {
    payload.icon_emoji = theIconEmoji
  }
  if (theChannel !== undefined) {
    payload.channel = theChannel
  }
  let theRequest = {
    url: process.env.SLACK_URL,
    method: 'POST',
    json: payload
  }
  request(theRequest, function(error, response) {
    if (!error && (response.statusCode === 200)) {
      console.log('sendToSlack: ' + s)
    } else {
      console.log('sendToSlack: error, code == ' + response.statusCode + ', ' + response.body + '.\n')
    }
  })
}

function sendMqtt(feed, message) {
  let client = mqtt.connect({
    host: process.env.MQTT_BROKER,
    port: 1883,
    username: process.env.MQTT_USERNAME,
    password: process.env.MQTT_TOKEN
  })
  client.publish(feed, message)
  client.end()
}

let button = new DashButton(process.env.DASH_BUTTON_DEPLOY)

button.addListener(async () => {
  let jokeRequest = {
    url: 'http://api.icndb.com/jokes/random',
    method: 'GET'
  }

  request(jokeRequest, function(error, response) {
    if (!error && (response.statusCode === 200)) {
      let joke = JSON.parse(response.body).value.joke;
      sendToSlack(joke, 'Chuck Norris', 'https://f1.blick.ch/img/incoming/origs7200249/430014937-w980-h653/News-Norris-B150.jpg', null, '@ala')
      sendMqtt('vergissberlin/feeds/dash', joke)

    } else {
      return false;
      console.log('joke: error, code == ' + response.statusCode + ', ' + response.body + '.\n')
    }
  })
})
