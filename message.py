'''
Created on Oct 25, 2019

@author: asharda
'''
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "accountsid"
# Your Auth Token from twilio.com/console
auth_token  = "authtoken"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="tonum", 
    from_="fromphone",
    body="Hello from Shalu!")

print(message.sid)
