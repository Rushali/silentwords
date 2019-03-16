from twilio.rest import Client
from urllib2 import urlopen
import wget

account_sid = process.env.ACCOUNT_SID
auth_token = process.env.AUTH_TOKEN

client = Client(account_sid, auth_token)
recordings = client.recordings.list()
for record in recordings:
	print(record.sid)
	fileUrl = 'https://api.twilio.com/2010-04-01/Accounts'+str(account_sid)+'/Recordings'+str(record.sid)
	print(fileUrl)
	urllib.request.urlretrieve(fileUrl, str(record.sid)+'.wav')
	#fileName = wget.download(fileUrl)
	#len(recordings)!=len(set(recordings))
