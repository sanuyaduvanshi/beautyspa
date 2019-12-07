from twilio.rest import Client



account_sid = 'AC9e59c0f3c67ba050e8de9220fabef012'
auth_token = '8296009e858fd9c21ba0c5462a95b2d0'
client = Client(account_sid, auth_token)
message = client.messages.create(from_='+14242383634',body ='hello sandy',to ="+918919538130",)

print(message.sid)
