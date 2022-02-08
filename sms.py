from twilio.rest import Client

account_sid = '[AccountSidNumber]'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='[TwilioNumber]',
    body='It works.',
    to='[MyNumber]'
  )
print(message.sid)
