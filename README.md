# Sendgrid Email Spoofer

This program uses Sendgrid to send spoofed emails. Simply go to the Sendgrid website, create and account, and copy your api key into this code. 

#### A few things to keep in mind...

- Sendgrid limits the number of emails you send each day and the more rejected emails you send (ie: bounceback, marked as spam) the lower your "score" with Sendgrid gets.

- The header in the recipient's inbox shows a "via" message (ie: "From: "Test Name'(test@example.com) via Sendgrid.net")

- The header **_ALSO shows YOUR OUTGOING IP ADDRESS_**. **_DO NOT use this program unless you want your public IP broadcast_**. However, sending while connected to a VPN does mask the IP but the email history on your Sendgrid account still shows.

- You can (and I have) simply set the code to read from an html file, print the raw text, and then reformat it for html for the email body. By literally copy/pasting the HTML code from a legit steam email and changing a few lines of text, I sent a near-perfectly spoofed alert email. I also have sent the complete bee movie script to an unlucky few.

- _Sometimes_ the emails go to spam. This can be due to a lot of things, so be careful.

#### DISCLAIMER
Have fun and **_PLEASE don't use for malicious purposes_**. This code is basically taken directly from SendGrid's examples but nowhere have I found it used as a email spoofer.

#### Social Media
Github.com/nickdrones, Twitter @nickdronesguy, YouTube @ Nick The Drone Guy
