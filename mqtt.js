/**
 * Send slack message
 *
 * @category
 * @author   Andre Lademann <vergissberlin@googlemail.com>
 * @license  MIT
 */

const mqtt = require('mqtt')
var client  = mqtt.connect(
{
        host: 'io.adafruit.com',
        port: 1883,
        username: 'vergissberlin',
        password: 'ad755b7b9d994e4abe62bc0ace181023'
    }
)

client.on('connect', function () {
  client.subscribe('vergissberlin/feeds/dash', function (err) {
    if (!err) {
      client.publish('vergissberlin/feeds/dash', 'Hello mqtt')
    }
  })
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})
