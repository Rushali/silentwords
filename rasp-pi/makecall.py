from twilio.rest import Client

account_sid = process.env.ACCOUNT_SID
auth_token = process.env.AUTH_TOKEN

client = Client(account_sid, auth_token)
