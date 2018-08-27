/**
 * Send slack message
 *
 * @category
 * @author   Andre Lademann <vergissberlin@googlemail.com>
 * @license  MIT
 */

const request = require('request'),
      env     = require('dotenv').config()


function sendToSlack (s, theUsername, theIconUrl, theIconEmoji, theChannel) {
    let payload = {
        text: s
    }
    if ( theUsername !== undefined ) {
        payload.username = theUsername
    }
    if ( theIconUrl !== undefined ) {
        payload.icon_url = theIconUrl
    }
    if ( theIconEmoji !== undefined ) {
        payload.icon_emoji = theIconEmoji
    }
    if ( theChannel !== undefined ) {
        payload.channel = theChannel
    }
    let theRequest = {
        url:    process.env.SLACK_URL,
        method: 'POST',
        json:   payload
    }
    request(theRequest, function (error, response, body) {
        if ( !error && (response.statusCode == 200
        ) ) {
            console.log('sendToSlack: ' + s)
        }
        else {
            console.log('sendToSlack: error, code == ' + response.statusCode + ', ' + response.body + '.\n')
        }
    })
}

sendToSlack('Hello World', 'The Boss', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE7HiJ7383bsYyHmdU2l-MGS6sKaGE88InU63jIvFBp95A4nhX', null, 'ci')
