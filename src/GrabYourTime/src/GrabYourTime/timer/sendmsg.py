import json
from math import ceil

from twilio.base import values
from twilio.base.exceptions import TwilioRestException

from twilio.rest import Client
from twilio.rest import TwilioRestClient
# Your Account SID from twilio.com/console
account_sid = "ACf189908875e4874cfaf2eb9cdc54a9ddd8"
# Your Auth Token from twilio.com/console
auth_token  = "a5a953bfce441f3fe2b01b3bd842eefa"

client = Client(account_sid, auth_token)

try:
    client.api.account.messages.create(
        to="+14127732586", 
        from_="+17243052567",
        body="Hello from Python!")
    #print(message.sid)
except TwilioRestException as ex:
    print(ex)

