import RPi.GPIO as GPIO
from flask import Flask
from twilio.twiml.voice_response import Record, VoiceResponse
from twilio.rest import Client

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
#GPIO.output(18, GPIO.LOW)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
	"""Respond to incoming phone calls with a brief message."""
	GPIO.output(18, GPIO.HIGH)
	#start twiml response
	resp = VoiceResponse()
	#read a message aloud to the caller
	resp.say("Thank you for calling silent words! Please share your story at the beep. Press the star when finished", voice='alice')
	resp.record(
		timeout=10,
		finish_on_key='*',
		max_length=20,
		action='https://880aaaa2.ngrok.io/handlerecording', #change link based on ngrok
		method='GET'
	)
	return str(resp)


@app.route("/handlerecording", methods=['GET', 'POST'])
def handle_record():
	GPIO.output(18, GPIO.HIGH)
	"""respond to incoming call with recieval of note"""
	response = VoiceResponse()

	response.say("Thank you for sharing your encounter!", voice='alice')
	return str(response)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)
