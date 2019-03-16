'use strict';

const express = require('express');
const twilio = require('twilio');
// const VoiceResponse = twilio.twiml.VoiceResponse;
// const Agent = require('../models/agent');
// const router = new express.Router();

const app = express();

// Returns TwiML which prompts the caller to record a message 
app.post('/record', (request, response) => {
  // Use the Twilio Node.js SDK to build an XML response
  //console.log('')
  const twiml = new twilio.twiml.VoiceResponse();
  // console.log(twiml.root);
  twiml.say('Hello. Please leave a message after the beep.');

  // Use <Record> to record and transcribe the caller's message
  twiml.record({transcribe: true, maxLength: 30});

  // End the call with <Hangup>
  twiml.hangup();

  // Render the response as XML in reply to the webhook request
  response.type('text/xml');
  response.send(twiml.toString());
});

// Create an HTTP server and listen for requests on port 3000
app.listen(3000, () => console.log('Server listening on port 3000!'));
