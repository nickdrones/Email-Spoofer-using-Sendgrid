import sendgrid
from sendgrid.helpers import mail

api = sendgrid.SendGridAPIClient(apikey='INSERT API KEY HERE')

recipient = mail.Email('recipient@example.com')
sender = mail.Email('sender@example.com','Sender Name')
subject = 'Email Subject'
body = mail.Content('text/html','Email Body Here')

email = mail.Mail(sender, subject, recipient, body)
response = api.client.mail.send.post(request_body=email.get())

print(response.status_code)
print(response.body)
print(response.headers)
