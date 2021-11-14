from decouple import config
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = config('USER')
# Your Auth Token from twilio.com/console
auth_token = config('KEY')
# Phone Number (US Only)
phone_number = "+1" + input("enter your phone number (numbers only): ")

client = Client(account_sid, auth_token)


# Text user: default
def text_user():
    message = client.messages.create(
        to=phone_number,
        from_="+14232502023",
        body=
        "Hi!! This is Elizabeth and Alyssa on Twilio hacking at Technica 2021. Welcome to trak!"
    )


# Text user: custom
def text_user_custom(custom_message):
    custom_message = input("enter your message to send: ")
    message = client.messages.create(to=phone_number,
                                     from_="+14232502023",
                                     body=custom_message)


# print(message.sid)

# Create new record (call user)
# call = client.calls.create(to=phone_number,
#                            from_="+14232502023",
#                            url="http://demo.twilio.com/docs/voice.xml")

# print(call.sid)

# THIS DOES NOT WORK Get existing record (list of users called)
# call = client.calls.get(config('USER'))
# print(call.to)

# Iterate through records (list of users texted)
# for sms in client.messages.list():
#     print(sms.to)

text_user()