/**
 * Send slack message
 *
 * @category
 * @author   Andre Lademann <vergissberlin@googlemail.com>
 * @license  MIT
 */

const request = require('request')
const DashButton = require('dash-button')
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

let button = new DashButton(process.env.DASH_BUTTON_DEPLOY)

button.addListener(async () => {
    sendToSlack('... is calling you', 'The Boss', 'http://beardstyle.net/wp-content/uploads/2016/06/hipster-mustaches-11.jpg', null, '@ala')
})
