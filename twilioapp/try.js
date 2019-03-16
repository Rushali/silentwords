var accountSid = '';
var authToken = "";
var client = require('twilio')(accountSid, authToken);

client.calls.create({
    url: "http://demo.twilio.com/docs/voice.xml",
    to: "+19175284685",
    from: "+12289018399 "
}, function(err, call) {
    console.log(call.sid);
});