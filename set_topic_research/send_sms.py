# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACa2917b3dd13fb0699457988a1a45453b"
auth_token = "94f8bb4ea3334a95fc06d094b01bc6a2"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+67078150465",
                                             from_="+14253201886",
                                             body="MALUK SIRA IMI DIAK KA LAE?")

