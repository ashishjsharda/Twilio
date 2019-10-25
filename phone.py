'''
Created on Oct 25, 2019
Do random phone calls using Twilio
@author: asharda
'''
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='tonumber',
                        from_='fromnumber'
                    )

print(call.sid)
