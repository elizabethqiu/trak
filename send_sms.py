from decouple import config
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = config('USER')
# Your Auth Token from twilio.com/console
auth_token = config('KEY')
# Phone Number (US Only)
phone_number = "+1" + input("enter your phone number (numbers only): ")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=phone_number,
    from_="+14232502023",
    body=
    "Hi!! This is Elizabeth on Twilio! hacking at Technica 2021 this weekend lolol"
)

print(message.sid)