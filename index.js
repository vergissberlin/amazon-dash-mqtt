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

let buttonBlugento = new DashButton(process.env.BUTTON_BLUGENTO)
let buttonChuckNorris = new DashButton(process.env.BUTTON_CHUCK_NORRIS)

buttonChuckNorris.addListener(async () => {
  let jokeRequest = {
    url: 'http://api.icndb.com/jokes/random',
    method: 'GET'
  }

  request(jokeRequest, function(error, response) {
    if (!error && (response.statusCode === 200)) {
      let joke = JSON.parse(response.body).value.joke;
      sendToSlack(joke, 'Chuck Norris', 'https://pm1.narvii.com/6037/494011a5f5cbdc6fe7f515a3b8f2c464c6c5f5e5_128.jpg', null, '@ala')
    } else {
      return false;
      console.log('joke: error, code == ' + response.statusCode + ', ' + response.body + '.\n')
    }
  })
})


buttonBlugento.addListener(async () => {
    sendToSlack('New release is out!', 'Blugento', 'https://s3.amazonaws.com/f6s-public/profiles/1384760_original.jpg', null, '@ala')
})
