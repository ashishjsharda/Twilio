from twilio.rest import Client
account_sid='youraccountsid'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the from twilio ,testing',
         from_='twilio number shown',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='phone number to be sent'
     )

print(message.sid)
print(message.body)
